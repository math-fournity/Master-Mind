"""
KnowledgeAbsorptionPipeline：知识吸收pipeline

把batch_extractor.py的逻辑从独立脚本改造成吸收pipeline的一个环节。

完整流程：
  1. AI阅读理解——调用AI完整阅读数学内容，形成结构化理解
  2. L1提取——从AI理解中提取2-3种解法路径
  3. L2提取——从L1中抽象弥漫性思维模式
  4. L3提取——从L1/L2中识别跨领域映射范式
  5. 质量审计——L2/L3审计（弥漫性/改变图结构）
  6. 存入ArangoDB——L1→requires/uses边, L2→awareness节点, L3→cross_domain边

对应204号方案 + 207号Check List的204-A Phase。

用法：
    pipeline = KnowledgeAbsorptionPipeline()
    result = pipeline.absorb(MathContent(
        title="费马大定理",
        statement="x^n + y^n = z^n在n>2时无非平凡整数解",
        proof="...",  # 可选
        domain=["数论", "代数几何"],
        methods=["模形式", "椭圆曲线"],
    ))
    # result.l1, result.l2, result.l3, result.audit, result.stored
"""
import os
import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional


@dataclass
class MathContent:
    """数学内容输入schema（204-A.0）"""
    title: str
    statement: str
    proof: str = ""  # 可选——有些内容只有陈述没有证明
    domain: List[str] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    source: str = ""  # 来源（论文/教材/讲义等）

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "statement": self.statement,
            "proof": self.proof,
            "domain": self.domain,
            "methods": self.methods,
            "source": self.source,
        }


@dataclass
class L1Extraction:
    """L1解法路径（204-A.2）"""
    problem_id: str
    title: str
    solutions: List[Dict[str, Any]] = field(default_factory=list)
    # 每个solution: {steps: [{concept, action}], method, difficulty}

    def to_dict(self) -> dict:
        return {
            "problem_id": self.problem_id,
            "title": self.title,
            "solutions": self.solutions,
        }


@dataclass
class L2Extraction:
    """L2思维模式（204-A.3）"""
    pattern_id: str
    pattern_name: str
    description: str
    evidence_step: str  # 来源步骤
    applicable_domains: List[str]  # 适用领域（≥2个）
    examples: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "pattern_id": self.pattern_id,
            "pattern_name": self.pattern_name,
            "description": self.description,
            "evidence_step": self.evidence_step,
            "applicable_domains": self.applicable_domains,
            "examples": self.examples,
        }


@dataclass
class L3Extraction:
    """L3跨领域映射范式（204-A.4）"""
    paradigm_id: str
    paradigm_name: str
    description: str
    source_domain: str
    target_domain: str
    mapping_type: str  # 结构同构/方法迁移/概念对应
    changes_graph_structure: bool  # 是否改变图结构（必须True）
    evidence: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "paradigm_id": self.paradigm_id,
            "paradigm_name": self.paradigm_name,
            "description": self.description,
            "source_domain": self.source_domain,
            "target_domain": self.target_domain,
            "mapping_type": self.mapping_type,
            "changes_graph_structure": self.changes_graph_structure,
            "evidence": self.evidence,
        }


@dataclass
class L4Extraction:
    """L4哲学/世界观洞察（204-B.0）"""
    node_id: str
    insight: str           # 哲学洞察文本
    applicable_principle: str  # 适用原理
    source_evidence: List[str] # 来源证据（哪些定理/证明中提取的）
    applicable_domains: List[str]  # 适用领域
    verification_method: str  # 验证方法（如何判断这个洞察是否有价值）

    def to_dict(self) -> dict:
        return {
            "node_id": self.node_id,
            "insight": self.insight,
            "applicable_principle": self.applicable_principle,
            "source_evidence": self.source_evidence,
            "applicable_domains": self.applicable_domains,
            "verification_method": self.verification_method,
        }


@dataclass
class ExtractionAudit:
    """质量审计结果（204-A.5 + 204-B.2）"""
    l2_passed: bool = False
    l2_reason: str = ""
    l3_passed: bool = False
    l3_reason: str = ""
    l4_passed: bool = False  # 204-B.2: L4质量审计
    l4_reason: str = ""
    needs_human_review: bool = False  # AI自审AI的循环验证风险

    def to_dict(self) -> dict:
        return {
            "l2_passed": self.l2_passed,
            "l2_reason": self.l2_reason,
            "l3_passed": self.l3_passed,
            "l3_reason": self.l3_reason,
            "l4_passed": self.l4_passed,
            "l4_reason": self.l4_reason,
            "needs_human_review": self.needs_human_review,
        }


@dataclass
class AbsorptionResult:
    """吸收结果（204-A.0）"""
    content: MathContent
    l1: Optional[L1Extraction] = None
    l2: List[L2Extraction] = field(default_factory=list)
    l3: List[L3Extraction] = field(default_factory=list)
    l4: List[L4Extraction] = field(default_factory=list)  # 204-B: L4哲学层
    audit: Optional[ExtractionAudit] = None
    stored: bool = False  # 是否已存入ArangoDB
    stored_to: Dict[str, str] = field(default_factory=dict)  # 各层级存入位置
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "content": self.content.to_dict(),
            "l1": self.l1.to_dict() if self.l1 else None,
            "l2": [l.to_dict() for l in self.l2],
            "l3": [l.to_dict() for l in self.l3],
            "l4": [l.to_dict() for l in self.l4],
            "audit": self.audit.to_dict() if self.audit else None,
            "stored": self.stored,
            "stored_to": self.stored_to,
            "timestamp": self.timestamp,
        }


class KnowledgeAbsorptionPipeline:
    """
    知识吸收pipeline（204-A）。

    从数学内容中提取L1/L2/L3三层知识，经质量审计后存入ArangoDB。

    调用方式：
        pipeline = KnowledgeAbsorptionPipeline()
        result = pipeline.absorb(content)

    注意：
    - AI阅读/L1/L2/L3提取需要外部AI执行（pipeline生成prompt，由调用方调度AI）
    - 质量审计由pipeline内部执行（规则检查）
    - ArangoDB存储由pipeline内部执行
    """

    def __init__(
        self,
        arango_host: str = None,
        arango_db: str = None,
        arango_user: str = None,
        arango_pass: str = None,
    ):
        self.arango_host = arango_host or os.environ.get("ARANGO_HOST", "http://localhost:8529")
        self.arango_db = arango_db or os.environ.get("ARANGO_DB", "xishujuzhen_math_glm52")
        self.arango_user = arango_user or os.environ.get("ARANGO_USER", "root")
        self.arango_pass = arango_pass or os.environ.get("ARANGO_PASS", "REDACTED-DB-PASSWORD")

    def absorb(self, content: MathContent) -> AbsorptionResult:
        """吸收数学内容的完整流程（204-A.0接口）"""
        result = AbsorptionResult(content=content)

        # 步骤1: AI阅读理解（生成prompt，由调用方调度AI）
        understanding_prompt = self._generate_understanding_prompt(content)
        # 注：实际AI调用由调用方执行，这里只生成prompt
        # 调用方拿到prompt后调度AI，把结果回填到result

        # 步骤2-4: L1/L2/L3提取（生成prompt）
        l1_prompt = self._generate_l1_prompt(content)
        l2_prompt = self._generate_l2_prompt(content)
        l3_prompt = self._generate_l3_prompt(content)

        # 把prompt附加到result，供调用方使用
        result._prompts = {
            "understanding": understanding_prompt,
            "l1": l1_prompt,
            "l2": l2_prompt,
            "l3": l3_prompt,
        }

        return result

    def absorb_with_extractions(
        self,
        content: MathContent,
        l1: L1Extraction,
        l2: List[L2Extraction],
        l3: List[L3Extraction],
        l4: List[L4Extraction] = None,  # 204-B: L4哲学层
    ) -> AbsorptionResult:
        """已有提取结果时直接走审计+存储（跳过AI提取步骤）"""
        l4 = l4 or []
        result = AbsorptionResult(content=content, l1=l1, l2=l2, l3=l3, l4=l4)

        # 步骤5: 质量审计
        result.audit = self._audit(l1, l2, l3, l4)

        # 步骤6: 存入ArangoDB（审计通过才存）
        if result.audit.l2_passed and result.audit.l3_passed and result.audit.l4_passed:
            result.stored, result.stored_to = self._store_to_arango(l1, l2, l3, l4)

        return result

    def _generate_understanding_prompt(self, content: MathContent) -> str:
        """204-A.1: AI阅读理解prompt"""
        lines = [
            "你是数学大师系统的知识吸收AI。请完整阅读以下数学内容，形成结构化理解。",
            "",
            f"标题：{content.title}",
            f"陈述：{content.statement}",
        ]
        if content.proof:
            lines.append(f"证明：{content.proof[:3000]}")  # 限制长度
        if content.domain:
            lines.append(f"领域：{', '.join(content.domain)}")
        if content.methods:
            lines.append(f"方法：{', '.join(content.methods)}")
        lines += [
            "",
            "请输出结构化理解（JSON格式）：",
            "{",
            '  "key_concepts": ["核心概念1", "核心概念2", ...],',
            '  "proof_structure": "证明结构概述（如果有的话）",',
            '  "domain_context": "领域背景",',
            '  "difficulty": "easy/medium/hard",',
            '  "prerequisites": ["前置知识1", "前置知识2", ...]',
            "}",
        ]
        return "\n".join(lines)

    def _generate_l1_prompt(self, content: MathContent) -> str:
        """204-A.2: L1提取prompt（从batch_extractor.py迁移）"""
        lines = [
            "你是数学大师系统的L1提取AI。请对以下定理做L1解法路径提取。",
            "",
            f"标题：{content.title}",
            f"陈述：{content.statement}",
        ]
        if content.methods:
            lines.append(f"方法提示：{', '.join(content.methods)}")
        if content.domain:
            lines.append(f"领域：{', '.join(content.domain)}")
        lines += [
            "",
            "提取2-3种解法路径，每种4-7步，每步标注concept和action。",
            "输出JSON格式：",
            "{",
            '  "solutions": [',
            '    {',
            '      "method": "解法名称",',
            '      "difficulty": "easy/medium/hard",',
            '      "steps": [',
            '        {"concept": "用到的概念", "action": "执行的操作"},',
            "        ...",
            "      ]",
            "    }",
            "  ]",
            "}",
            "",
            "注意：每道题至少2种解法。",
        ]
        return "\n".join(lines)

    def _generate_l2_prompt(self, content: MathContent) -> str:
        """204-A.3: L2提取prompt（从batch_extractor.py迁移）"""
        lines = [
            "你是数学大师系统的L2提取AI。请从以下数学内容中抽象弥漫性思维模式。",
            "",
            f"标题：{content.title}",
            f"陈述：{content.statement}",
        ]
        if content.domain:
            lines.append(f"领域：{', '.join(content.domain)}")
        lines += [
            "",
            "提取L2思维模式——必须是弥漫性思维模式（在多个领域可调用），不是某题专属技巧。",
            "每个L2必须覆盖≥2个领域。",
            "",
            "输出JSON数组：",
            "[",
            "  {",
            '    "pattern_name": "思维模式名称",',
            '    "description": "模式描述",',
            '    "evidence_step": "来源步骤",',
            '    "applicable_domains": ["领域1", "领域2", ...],  # 至少2个',
            '    "examples": ["例子1", "例子2"]',
            "  }",
            "]",
            "",
            "注意：L2必须是弥漫性思维模式（在多个领域可调用），不是某题专属技巧。",
        ]
        return "\n".join(lines)

    def _generate_l3_prompt(self, content: MathContent) -> str:
        """204-A.4: L3提取prompt（从batch_extractor.py迁移）"""
        lines = [
            "你是数学大师系统的L3提取AI。请从以下数学内容中识别跨领域映射范式。",
            "",
            f"标题：{content.title}",
            f"陈述：{content.statement}",
        ]
        if content.domain:
            lines.append(f"领域：{', '.join(content.domain)}")
        lines += [
            "",
            "提取L3范式——必须是具体范式（改变图结构，连接不同领域），不是元思维模式。",
            "每个L3必须有具体的跨领域映射。",
            "",
            "输出JSON数组：",
            "[",
            "  {",
            '    "paradigm_name": "范式名称",',
            '    "description": "范式描述",',
            '    "source_domain": "源领域",',
            '    "target_domain": "目标领域",',
            '    "mapping_type": "结构同构/方法迁移/概念对应",',
            '    "changes_graph_structure": true,  # 必须true',
            '    "evidence": ["证据1", "证据2"]',
            "  }",
            "]",
            "",
            "注意：L3必须是具体范式（改变图结构，连接不同领域），不是元思维模式。",
            '如果该内容没有L3级范式，返回空数组[]。',
        ]
        return "\n".join(lines)

    def _generate_l4_prompt(self, content: MathContent) -> str:
        """204-B.1: L4哲学洞察提取prompt"""
        lines = [
            "你是数学大师系统的L4哲学洞察提取AI。请从以下数学内容中提取1-3条哲学洞察。",
            "",
            f"标题：{content.title}",
            f"陈述：{content.statement}",
        ]
        if content.proof:
            lines.append(f"证明：{content.proof[:2000]}")
        if content.domain:
            lines.append(f"领域：{', '.join(content.domain)}")
        lines += [
            "",
            "哲学洞察的定义：",
            "- 不是具体解题技巧",
            "- 不是跨领域映射（那是L3）",
            "- 是关于'数学本质'的认识——什么让数学工作？什么让证明深刻？什么连接了看似无关的领域？",
            "",
            "例子：",
            '- "等价性比相等性更深刻"——来自费马大定理的证明',
            '- "深刻的数学真理往往隐藏在看似无关的领域之间"——来自朗兰兹纲领',
            '- "简化陈述不等于简单证明"——来自费马大定理',
            '- "对称性决定可解性"——来自伽罗瓦理论',
            '- "任何足够强的形式系统都有无法自证的真理"——来自哥德尔不完备性定理',
            "",
            "输出JSON数组：",
            "[",
            "  {",
            '    "insight": "哲学洞察文本",',
            '    "applicable_principle": "适用原理",',
            '    "source_evidence": ["来源证据1（具体定理/证明）"],',
            '    "applicable_domains": ["适用领域1", "适用领域2"],',
            '    "verification_method": "验证方法（如何判断这个洞察是否有价值）"',
            "  }",
            "]",
            "",
            "注意：",
            "- 必须有具体来源证据（不是空泛的格言）",
            "- 必须能指导具体决策（不是只说不做）",
            "- 最好在多个领域有体现（不是某个领域的特例）",
            '- 如果该内容没有L4级哲学洞察，返回空数组[]',
        ]
        return "\n".join(lines)

    def _audit(
        self,
        l1: L1Extraction,
        l2: List[L2Extraction],
        l3: List[L3Extraction],
        l4: List[L4Extraction] = None,
    ) -> ExtractionAudit:
        """204-A.5 + 204-B.2: 质量审计"""
        l4 = l4 or []
        audit = ExtractionAudit()

        # L2审计：是否真弥漫性（覆盖≥2领域，有具体例子）
        if not l2:
            audit.l2_passed = True  # 无L2不算失败——不是所有内容都有L2
            audit.l2_reason = "无L2提取（该内容可能无弥漫性思维模式）"
        else:
            l2_issues = []
            for pattern in l2:
                if len(pattern.applicable_domains) < 2:
                    l2_issues.append(f"{pattern.pattern_name}: 只覆盖{len(pattern.applicable_domains)}个领域——非弥漫性")
                if not pattern.examples:
                    l2_issues.append(f"{pattern.pattern_name}: 无具体例子")
            if l2_issues:
                audit.l2_passed = False
                audit.l2_reason = "; ".join(l2_issues)
            else:
                audit.l2_passed = True
                audit.l2_reason = f"{len(l2)}个L2全部通过弥漫性审计"

        # L3审计：是否真改变图结构（有具体的跨领域映射，不是元策略）
        if not l3:
            audit.l3_passed = True  # 无L3不算失败
            audit.l3_reason = "无L3提取（该内容可能无跨领域范式）"
        else:
            l3_issues = []
            for paradigm in l3:
                if not paradigm.changes_graph_structure:
                    l3_issues.append(f"{paradigm.paradigm_name}: 不改变图结构——非范式级")
                if paradigm.source_domain == paradigm.target_domain:
                    l3_issues.append(f"{paradigm.paradigm_name}: 源领域=目标领域——非跨领域")
                if not paradigm.evidence:
                    l3_issues.append(f"{paradigm.paradigm_name}: 无证据")
            if l3_issues:
                audit.l3_passed = False
                audit.l3_reason = "; ".join(l3_issues)
            else:
                audit.l3_passed = True
                audit.l3_reason = f"{len(l3)}个L3全部通过范式审计"

        # 204-B.2: L4审计——3个质量标准
        if not l4:
            audit.l4_passed = True  # 无L4不算失败
            audit.l4_reason = "无L4提取（该内容可能无哲学层洞察）"
        else:
            l4_issues = []
            for node in l4:
                # 标准1: 有具体来源证据（不是空泛格言）
                if not node.source_evidence:
                    l4_issues.append(f"{node.insight[:30]}: 无具体来源证据——空泛格言")
                # 标准2: 能指导具体决策（有applicable_principle和verification_method）
                if not node.applicable_principle:
                    l4_issues.append(f"{node.insight[:30]}: 无适用原理——只说不做")
                if not node.verification_method:
                    l4_issues.append(f"{node.insight[:30]}: 无验证方法——无法判断价值")
                # 标准3: 在多个领域有体现（≥2个applicable_domains）
                if len(node.applicable_domains) < 2:
                    l4_issues.append(f"{node.insight[:30]}: 只覆盖{len(node.applicable_domains)}个领域——特例")
            if l4_issues:
                audit.l4_passed = False
                audit.l4_reason = "; ".join(l4_issues)
            else:
                audit.l4_passed = True
                audit.l4_reason = f"{len(l4)}个L4全部通过哲学洞察审计"

        # AI自审AI的循环验证风险
        audit.needs_human_review = bool(l2 or l3 or l4)

        return audit

    def _store_to_arango(
        self,
        l1: L1Extraction,
        l2: List[L2Extraction],
        l3: List[L3Extraction],
        l4: List[L4Extraction] = None,
    ) -> tuple:
        """204-A.6 + 204-B.6: 存入ArangoDB K维度"""
        l4 = l4 or []
        stored_to = {}
        try:
            from arango import ArangoClient
            client = ArangoClient(hosts=self.arango_host)
            db = client.db(self.arango_db, username=self.arango_user, password=self.arango_pass)

            # L1→K维度·requires/uses边
            if l1.solutions:
                for sol in l1.solutions:
                    for step in sol.get("steps", []):
                        edge_doc = {
                            "_key": f"l1_{l1.problem_id}_{step.get('concept', 'unknown')}",
                            "type": "requires",
                            "source": l1.problem_id,
                            "target": step.get("concept", ""),
                            "action": step.get("action", ""),
                            "method": sol.get("method", ""),
                            "level": "L1",
                            "timestamp": datetime.now(timezone.utc).isoformat(),
                        }
                        try:
                            db.collection("kg_edges").insert(edge_doc)
                        except Exception:
                            pass
                stored_to["L1"] = "kg_edges"

            # L2→K维度·awareness节点
            for pattern in l2:
                node_doc = {
                    "_key": f"l2_{pattern.pattern_id}",
                    "type": "awareness",
                    "name": pattern.pattern_name,
                    "description": pattern.description,
                    "applicable_domains": pattern.applicable_domains,
                    "evidence_step": pattern.evidence_step,
                    "examples": pattern.examples,
                    "level": "L2",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
                try:
                    db.collection("kg_nodes").insert(node_doc)
                except Exception:
                    pass
            if l2:
                stored_to["L2"] = "kg_nodes"

            # L3→K维度·cross_domain边
            for paradigm in l3:
                edge_doc = {
                    "_key": f"l3_{paradigm.paradigm_id}",
                    "type": "cross_domain",
                    "source": paradigm.source_domain,
                    "target": paradigm.target_domain,
                    "mapping_type": paradigm.mapping_type,
                    "description": paradigm.description,
                    "evidence": paradigm.evidence,
                    "level": "L3",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
                try:
                    db.collection("kg_edges").insert(edge_doc)
                except Exception:
                    pass
            if l3:
                stored_to["L3"] = "kg_edges"

            # 204-B.6: L4→K维度·philosophy节点（新增collection）
            for node in l4:
                node_doc = {
                    "_key": f"l4_{node.node_id}",
                    "type": "philosophy",
                    "insight": node.insight,
                    "applicable_principle": node.applicable_principle,
                    "source_evidence": node.source_evidence,
                    "applicable_domains": node.applicable_domains,
                    "verification_method": node.verification_method,
                    "level": "L4",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
                try:
                    db.collection("kg_nodes").insert(node_doc)
                except Exception:
                    pass
            if l4:
                stored_to["L4"] = "kg_nodes"

            return True, stored_to

        except Exception as e:
            print(f"[KnowledgeAbsorptionPipeline] ArangoDB存储失败: {e}")
            print("[KnowledgeAbsorptionPipeline] fallback：未入库，标注stored=False")
            return False, stored_to
