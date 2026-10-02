from jev_decision_ai.models import DecisionOption
from jev_decision_ai.decision_engine import JEVDecisionEngine


def main() -> None:
    options = [
        DecisionOption(
            name="Launch AI assistant pilot",
            cost=0.35,
            value=0.9,
            risk=0.25,
            urgency=0.8,
            confidence=0.85,
            strategic_fit=0.9,
        ),
        DecisionOption(
            name="Delay rollout",
            cost=0.2,
            value=0.55,
            risk=0.3,
            urgency=0.45,
            confidence=0.7,
            strategic_fit=0.65,
        ),
        DecisionOption(
            name="Full platform transformation",
            cost=0.82,
            value=0.95,
            risk=0.7,
            urgency=0.7,
            confidence=0.5,
            strategic_fit=0.95,
        ),
    ]

    engine = JEVDecisionEngine()
    ranked = engine.rank_options(options)

    print("JEV Decision Ranking")
    print("-" * 50)
    for result in ranked:
        print(
            f"{result.rank}. {result.option.name} | "
            f"score={result.score:.3f} | "
            f"reason={result.reasoning}"
        )


if __name__ == "__main__":
    main()
