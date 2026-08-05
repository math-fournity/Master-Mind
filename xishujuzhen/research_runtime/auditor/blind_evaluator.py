"""
BlindEvaluator：盲评流程

对应134号P4-4.3。

123号§49：执行盲评（评分者不知道哪些运行接受了哪些Hint）。
P4-4.COMP3：不让同一Master同时持有答案、设计Hint、运行Solver和评分。
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import random


@dataclass
class BlindEvalResult:
    """盲评结果"""
    run_id: str
    # 评分者不知道的处理组（盲评前）
    actual_treatment: str = ""
    # 评分者给出的评分
    progress_score: float = 0.0
    leakage_score: float = 0.0
    side_effect_score: float = 0.0
    # 评分者是否猜对了处理组（如果猜对，盲评可能失效）
    guessed_treatment: str = ""
    guessed_correctly: bool = False

    def to_dict(self) -> dict:
        return {
            "run_id": self.run_id,
            "actual_treatment": self.actual_treatment,
            "progress_score": self.progress_score,
            "leakage_score": self.leakage_score,
            "side_effect_score": self.side_effect_score,
            "guessed_treatment": self.guessed_treatment,
            "guessed_correctly": self.guessed_correctly,
        }


class BlindEvaluator:
    """
    P4-4.3：执行盲评。

    123号§49：评分者不知道哪些运行接受了哪些Hint。
    P4-4.COMP3：不让同一Master同时持有答案、设计Hint、运行Solver和评分。

    实现方法：
    1. 打乱运行顺序，隐藏处理组标签
    2. 评分者对每个运行评分
    3. 评分后揭晓处理组标签
    4. 检查评分者是否猜对了处理组（如果猜对率很高，盲评可能失效）
    """

    def __init__(self, seed: int = 42):
        self._rng = random.Random(seed)
        self._results: List[BlindEvalResult] = []

    def prepare_blind_set(
        self,
        runs: List[Dict[str, Any]],
    ) -> List[Dict[str, Any]]:
        """
        准备盲评集——打乱顺序，隐藏处理组标签。

        P4-4.3：评分者不知道哪些运行接受了哪些Hint。
        """
        blind_set = []
        for run in runs:
            blind_run = {
                "blind_id": f"blind_{self._rng.randint(10000, 99999)}",
                "response": run.get("response", ""),
                # 隐藏处理组标签
                "_actual_treatment": run.get("treatment_group", ""),
            }
            blind_set.append(blind_run)
        # 打乱顺序
        self._rng.shuffle(blind_set)
        return blind_set

    def evaluate(
        self,
        blind_run: Dict[str, Any],
        progress_score: float,
        leakage_score: float,
        side_effect_score: float,
        guessed_treatment: str = "",
    ) -> BlindEvalResult:
        """
        评分者对盲评运行评分。

        P4-4.COMP3：评分者不知道处理组，只看response评分。
        """
        actual = blind_run.get("_actual_treatment", "")
        result = BlindEvalResult(
            run_id=blind_run.get("blind_id", ""),
            actual_treatment=actual,
            progress_score=progress_score,
            leakage_score=leakage_score,
            side_effect_score=side_effect_score,
            guessed_treatment=guessed_treatment,
            guessed_correctly=(guessed_treatment == actual),
        )
        self._results.append(result)
        return result

    def verify_blind_integrity(self) -> Dict[str, Any]:
        """
        验证盲评完整性——检查评分者是否猜对了处理组。

        如果猜对率很高，说明Hint在response中留下了明显痕迹，盲评可能失效。
        """
        if not self._results:
            return {"integrity_ok": True, "n_results": 0}

        n_correct = sum(1 for r in self._results if r.guessed_correctly)
        guess_rate = n_correct / len(self._results)

        return {
            "integrity_ok": guess_rate < 0.5,  # 猜对率应低于50%
            "guess_rate": guess_rate,
            "n_results": len(self._results),
            "n_correct": n_correct,
            "warning": "盲评可能失效" if guess_rate >= 0.5 else "盲评有效",
        }

    def get_results(self) -> List[BlindEvalResult]:
        return self._results
