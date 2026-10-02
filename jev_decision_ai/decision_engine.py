from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class DecisionOption:
    name: str
    value: float
    cost: float
    risk: float
    urgency: float
    confidence: float
    strategic_fit: float


@dataclass(frozen=True)
class DecisionResult:
    option: DecisionOption
    score: float
    reasoning: str
    rank: int


class JEVDecisionEngine:
    """A simple decision scoring engine based on a JEV-style evaluation."""

    def rank_options(self, options: List[DecisionOption]) -> List[DecisionResult]:
        scored: List[DecisionResult] = []
        for index, option in enumerate(options, start=1):
            score = self._compute_score(option)
            reasoning = self._build_reasoning(option, score)
            scored.append(
                DecisionResult(
                    option=option,
                    score=score,
                    reasoning=reasoning,
                    rank=index,
                )
            )

        ranked = sorted(scored, key=lambda item: item.score, reverse=True)
        return [
            DecisionResult(
                option=result.option,
                score=result.score,
                reasoning=result.reasoning,
                rank=rank,
            )
            for rank, result in enumerate(ranked, start=1)
        ]

    def _compute_score(self, option: DecisionOption) -> float:
        """Normalize score to a 0-1 range with explicit tradeoff weights."""
        score = (
            0.35 * option.value
            + 0.20 * option.strategic_fit
            + 0.20 * option.confidence
            + 0.15 * option.urgency
            - 0.20 * option.cost
            - 0.20 * option.risk
        )
        return max(0.0, min(1.0, score))

    def _build_reasoning(self, option: DecisionOption, score: float) -> str:
        if score >= 0.75:
            return "High strategic value, strong confidence, and manageable risk."
        if score >= 0.45:
            return "Solid option with moderate tradeoffs and acceptable risk exposure."
        return "Lower expected return relative to cost and uncertainty."
