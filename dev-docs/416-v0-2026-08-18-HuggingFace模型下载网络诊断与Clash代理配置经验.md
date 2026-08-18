# 416号 · HuggingFace模型下载网络诊断与Clash代理配置经验

**日期**：2026-08-18
**性质**：调试经验文档——记录HuggingFace模型/数据集下载过程中遇到的网络问题、Clash代理诊断方法、根因和解决方案
**触发场景**：下载`orcarouter/Qwen3.8-27B-Uncensored-MLX`模型时遇到网络超时

---

## §1 问题现象

下载HuggingFace模型时出现：
- `huggingface_hub`的`snapshot_download()`超时
- `curl https://huggingface.co`有时成功有时超时
- `curl -x http://127.0.0.1:7897 https://huggingface.co`有时成功有时超时
- 现象是**间歇性的**——同样的命令，有时0.5秒返回HTTP 200，有时10秒超时

---

## §2 诊断过程

### 2.1 Clash API确认

```
Clash版本：v1.19.20（mihomo）
API端口：9097
API secret：&tnrgN61AB@@Yy*U3HXg
混合代理端口：7897（HTTP+SOCKS）
模式：global
当前节点：DIRECT
```

Clash API正常响应（HTTP 200），Clash本身没有问题。

### 2.2 代理端口确认

Clash的mixed-port是**7897**（不是常见的7890）。系统代理已设置：
```
scutil --proxy → HTTPProxy: 127.0.0.1, HTTPPort: 7897
```

### 2.3 节点切换测试

| 节点 | huggingface.co | google.com | 结论 |
|---|---|---|---|
| DIRECT | 间歇性成功/超时 | 间歇性成功/超时 | DIRECT不是纯直连，走Clash DNS |
| Firefox VPN | SSL_ERROR_SYSCALL | - | VPN节点不稳定，SSL被中断 |

### 2.4 DNS解析诊断（关键发现）

```
系统DNS（127.0.2.2）解析huggingface.co → 18.65.14.125, 18.65.14.85, 18.65.14.87
Cloudflare DNS（1.1.1.1）解析huggingface.co → 18.65.14.87, 18.65.14.100, 18.65.14.125
```

huggingface.co使用CloudFront CDN，返回多个IP。**关键问题：这些IP中有些被墙，有些没被墙**。

### 2.5 逐IP测试（根因定位）

```
18.65.14.87  → 超时（被墙）
18.65.14.100 → 超时（被墙）
18.65.14.125 → HTTP 200, 0.7s（可用）
18.65.14.85  → HTTP 200, 0.3s（可用）
```

**根因**：系统DNS返回的IP列表中包含被墙的IP。curl默认按顺序尝试，如果第一个IP是被墙的（如18.65.14.87），就会超时。DNS返回的IP顺序是随机的（轮询），所以表现为间歇性成功/超时。

### 2.6 HF镜像测试

```
https://hf-mirror.com → HTTP 200, 0.9s（稳定可用）
```

hf-mirror.com是HuggingFace的国内镜像，稳定可用。

---

## §3 根因总结

```
系统DNS(127.0.2.2)
  → 解析huggingface.co → CloudFront CDN返回多个IP
  → IP列表中有些被墙（18.65.14.87, .100），有些没被墙（.125, .85）
  → curl/Python按顺序尝试IP
  → 如果第一个IP是被墙的 → 超时
  → 如果第一个IP是没被墙的 → 成功
  → DNS轮询导致IP顺序随机 → 间歇性成功/超时
```

**不是Clash的问题**——Clash本身正常，代理端口7897正常。
**是DNS污染+IP轮询的问题**——系统DNS返回的IP列表包含被墙IP。

---

## §4 解决方案

### 方案A：使用HF镜像（推荐，最简单）

设置环境变量`HF_ENDPOINT`指向国内镜像：

```bash
# 临时（当前session）
export HF_ENDPOINT=https://hf-mirror.com

# 永久（写入~/.zshrc或~/.bashrc）
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.zshrc

# 然后正常使用huggingface_hub
python -c "from huggingface_hub import snapshot_download; snapshot_download('orcarouter/Qwen3.8-27B-Uncensored-MLX')"
```

`huggingface_hub`库会自动读取`HF_ENDPOINT`环境变量，所有请求转向hf-mirror.com。

**优点**：零代码改动，稳定可靠，国内CDN速度快
**缺点**：镜像可能有延迟（新上传的模型可能几小时后才同步）

### 方案B：固定可用IP（临时方案）

在`/etc/hosts`中固定huggingface.co到可用IP：

```bash
# 找到可用IP
for ip in $(nslookup huggingface.co 1.1.1.1 | grep "Address:" | tail -3 | awk '{print $2}'); do
    echo -n "  $ip: "
    timeout 5 curl -s -o /dev/null -w "HTTP %{http_code}" --resolve "huggingface.co:443:$ip" https://huggingface.co 2>&1 || echo "TIMEOUT"
    echo ""
done

# 写入hosts（选择HTTP 200的IP）
echo "18.65.14.125 huggingface.co" | sudo tee -a /etc/hosts
echo "18.65.14.125 cdn-lfs.huggingface.co" | sudo tee -a /etc/hosts
```

**优点**：不需要改代码或环境变量
**缺点**：CloudFront IP会轮换，可用IP可能明天就不可用；需要定期更新

### 方案C：配置Clash DNS（长期方案）

在Clash配置中启用DNS并使用远程DNS解析，避免系统DNS的污染：

```yaml
dns:
  enable: true
  listen: :7874
  enhanced-mode: fake-ip
  nameserver:
    - https://1.1.1.1/dns-query  # Cloudflare DoH
    - https://dns.google/dns-query  # Google DoH
  fallback:
    - https://1.1.1.1/dns-query
    - https://dns.google/dns-query
  fallback-filter:
    geoip: true
    geoip-code: CN
```

**优点**：从根本上解决DNS污染问题，所有被墙域名都能正确解析
**缺点**：需要修改Clash配置，可能影响其他网络行为

### 方案D：设置HTTP代理环境变量

让Python的`requests`/`huggingface_hub`走Clash代理：

```bash
export http_proxy=http://127.0.0.1:7897
export https_proxy=http://127.0.0.1:7897
export HTTP_PROXY=http://127.0.0.1:7897
export HTTPS_PROXY=http://127.0.0.1:7897
```

**注意**：这只在Clash的DIRECT节点能正确解析DNS时有效。如果Clash的DNS也用系统DNS，问题依然存在。需要配合方案C使用。

---

## §5 推荐方案

**推荐方案A（HF镜像）**——最简单、最稳定、零副作用：

```bash
# 写入shell配置
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.zshrc
source ~/.zshrc

# 验证
curl -s -o /dev/null -w "HTTP %{http_code}\n" https://hf-mirror.com
# 应该返回 HTTP 200
```

**如果方案A不满足**（如需要下载刚上传的新模型），用方案C（Clash DNS）+ 方案D（代理环境变量）组合。

---

## §6 Clash代理诊断SOP

未来遇到HuggingFace或其他网站访问问题时，按以下步骤诊断：

### 步骤1：确认Clash API

```bash
curl -s -H "Authorization: Bearer &tnrgN61AB@@Yy*U3HXg" http://127.0.0.1:9097/version
# 应返回 {"meta":true,"version":"v1.19.20"}
```

### 步骤2：确认代理端口

```bash
curl -s -H "Authorization: Bearer &tnrgN61AB@@Yy*U3HXg" http://127.0.0.1:9097/configs | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'mixed-port: {d.get(\"mixed-port\")}')"
# mixed-port: 7897
```

### 步骤3：确认当前节点

```bash
curl -s -H "Authorization: Bearer &tnrgN61AB@@Yy*U3HXg" http://127.0.0.1:9097/proxies/GLOBAL | python3 -c "import sys,json; d=json.load(sys.stdin); print(f'当前: {d.get(\"now\")}')"
```

### 步骤4：测试目标网站

```bash
# 直连
curl -s -o /dev/null -w "HTTP %{http_code} | %{time_total}s\n" --max-time 10 https://huggingface.co

# 走代理
curl -s -o /dev/null -w "HTTP %{http_code} | %{time_total}s\n" --max-time 10 -x http://127.0.0.1:7897 https://huggingface.co
```

### 步骤5：DNS诊断（如果间歇性超时）

```bash
# 系统DNS解析
nslookup huggingface.co

# Cloudflare DNS解析
nslookup huggingface.co 1.1.1.1

# 逐IP测试
for ip in $(nslookup huggingface.co 1.1.1.1 | grep "Address:" | tail -3 | awk '{print $2}'); do
    echo -n "  $ip: "
    timeout 5 curl -s -o /dev/null -w "HTTP %{http_code}" --resolve "huggingface.co:443:$ip" https://huggingface.co 2>&1 || echo "TIMEOUT"
    echo ""
done
```

### 步骤6：切换节点（如果当前节点有问题）

```bash
# 查看可选节点
curl -s -H "Authorization: Bearer &tnrgN61AB@@Yy*U3HXg" http://127.0.0.1:9097/proxies/GLOBAL | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('all'))"

# 切换节点
curl -s -X PUT -H "Authorization: Bearer &tnrgN61AB@@Yy*U3HXg" -H "Content-Type: application/json" -d '{"name":"节点名"}' http://127.0.0.1:9097/proxies/GLOBAL
```

---

## §7 已下载的模型/数据集状态

### 模型

| 模型 | 路径 | 大小 | 状态 |
|---|---|---|---|
| opendatalab/MinerU2.5-Pro-2605-1.2B | `~/.cache/huggingface/hub/models--opendatalab--MinerU2.5-Pro-2605-1.2B/` | 2.2G | ✅完整 |
| opendatalab/PDF-Extract-Kit-1.0 | `~/.cache/huggingface/hub/models--opendatalab--PDF-Extract-Kit-1.0/` | 238M | ✅完整 |
| orcarouter/Qwen3.8-27B-Uncensored-MLX | `~/.cache/huggingface/hub/models--orcarouter--Qwen3.8-27B-Uncensored-MLX/` | 4K | ❌只有refs，未下载 |

### 数据集（55个，截至2026-08-18）

主要数学题库数据集，包括NuminaMath-1.5、PolyMath、Omni-MATH-2、OpenMathReasoning、DeepMath-103K等。完整列表见`~/.cache/huggingface/hub/`目录。

---

## §8 关键认知

1. **Clash的DIRECT不是纯直连**——它通过Clash的DNS解析，所以走Clash 7897端口的DIRECT模式和绕过Clash的纯直连行为不同
2. **间歇性超时的根因是DNS轮询**——CloudFront返回多个IP，有些被墙有些没被墙，DNS轮询导致随机命中被墙IP
3. **HF镜像是最简单的解决方案**——`export HF_ENDPOINT=https://hf-mirror.com`一行搞定
4. **Clash API可以通过外部控制**——9097端口+secret可以查询状态、切换节点、修改配置
5. **诊断网络问题要逐层排查**——Clash API → 代理端口 → 节点 → DNS → 逐IP测试
