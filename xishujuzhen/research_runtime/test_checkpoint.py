"""
checkpoint 原语测试（261号§3.5）。

用253号A1-A10的Gold Standard六元组作为测试数据，
验证checkpoint保存、哈希确定性、哈希无碰撞、恢复、完整性验证。

运行：
    .venv/bin/python3 -m xishujuzhen.research_runtime.test_checkpoint
"""

from .parser.models import SixTuple
from .parser.test_data.gold_standard import GOLD_STANDARDS
from .checkpoint.manager import CheckpointManager


def _six_tuple_dict_from_gold(gold: dict) -> dict:
    """从Gold Standard提取六元组的dict表示。"""
    return SixTuple.from_dict(gold["six_tuple"]).to_dict()


def test_10_round_save():
    """测试1：253号10轮checkpoint保存。"""
    print("--- 测试1：253号10轮checkpoint保存 ---")
    mgr = CheckpointManager()
    checkpoints = []
    for i, gold in enumerate(GOLD_STANDARDS, start=1):
        six_tuple_dict = _six_tuple_dict_from_gold(gold)
        cp = mgr.save(round_index=i, six_tuple_dict=six_tuple_dict)
        checkpoints.append(cp)
        print(f"A{i}: hash={cp.checkpoint_id[:12]}... ✅")
    assert mgr.count() == 10, f"应保存10个checkpoint, 实际{mgr.count()}"
    print("10个checkpoint全部保存成功\n")
    return mgr, checkpoints


def test_hash_determinism(mgr, checkpoints):
    """测试2：哈希确定性。"""
    print("--- 测试2：哈希确定性 ---")
    a3_dict = _six_tuple_dict_from_gold(GOLD_STANDARDS[2])
    cp_again = mgr.save(round_index=3, six_tuple_dict=a3_dict)
    a3_original = checkpoints[2]
    print(f"A3原哈希: {a3_original.checkpoint_id[:16]}...")
    print(f"A3重存哈希: {cp_again.checkpoint_id[:16]}...")
    assert cp_again.checkpoint_id == a3_original.checkpoint_id, "A3重新保存应产生相同哈希"
    print("A3的checkpoint重新保存 → 相同哈希 ✅\n")


def test_hash_no_collision(checkpoints):
    """测试3：哈希无碰撞。"""
    print("--- 测试3：哈希无碰撞 ---")
    ids = [cp.checkpoint_id for cp in checkpoints]
    unique_ids = set(ids)
    assert len(unique_ids) == 10, f"10个哈希应全部唯一, 实际唯一数{len(unique_ids)}"
    print(f"A1-A10的10个哈希全部唯一（{len(unique_ids)}个唯一） ✅\n")


def test_restore(mgr, checkpoints):
    """测试4：从checkpoint恢复。"""
    print("--- 测试4：从checkpoint恢复 ---")
    a7_cp = checkpoints[6]
    restored = mgr.restore(a7_cp.checkpoint_id)
    assert restored is not None, "A7 checkpoint应能恢复"
    assert restored.six_tuple_dict == a7_cp.six_tuple_dict, "恢复的六元组应与A7一致"
    # 也验证按轮次获取
    by_round = mgr.get_by_round(7)
    assert by_round is not None, "按轮次7应能获取checkpoint"
    assert by_round.checkpoint_id == a7_cp.checkpoint_id, "按轮次获取的id应一致"
    print("从A7的checkpoint恢复 → 六元组与A7一致 ✅\n")


def test_integrity(mgr, checkpoints):
    """测试5：完整性验证。"""
    print("--- 测试5：完整性验证 ---")
    a5_cp = checkpoints[4]
    ok = mgr.verify_integrity(a5_cp.checkpoint_id)
    assert ok, "A5 checkpoint完整性验证应通过"
    print(f"A5的checkpoint完整性验证 → {'✅' if ok else '❌'}\n")

    # 负向测试：不存在的id
    ok_fake = mgr.verify_integrity("nonexistent_id_12345")
    assert not ok_fake, "不存在的id完整性验证应返回False"


def main():
    print("=== checkpoint 测试 ===\n")
    mgr, checkpoints = test_10_round_save()
    test_hash_determinism(mgr, checkpoints)
    test_hash_no_collision(checkpoints)
    test_restore(mgr, checkpoints)
    test_integrity(mgr, checkpoints)
    print("✅ 所有测试通过")


if __name__ == "__main__":
    main()
