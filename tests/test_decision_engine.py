from jev_decision_ai.models import DecisionOption
from jev_decision_ai.decision_engine import JEVDecisionEngine


def test_rank_options_prioritizes_best_choice() -> None:
    options = [
        DecisionOption(
            name="A",
            value=0.9,
            cost=0.25,
            risk=0.15,
            urgency=0.8,
            confidence=0.9,
            strategic_fit=0.9,
        ),
        DecisionOption(
            name="B",
            value=0.6,
            cost=0.4,
            risk=0.5,
            urgency=0.6,
            confidence=0.5,
            strategic_fit=0.6,
        ),
    ]

    ranked = JEVDecisionEngine().rank_options(options)
    assert ranked[0].option.name == "A"
    assert ranked[0].rank == 1
    assert ranked[0].score >= ranked[1].score
