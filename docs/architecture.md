# Architecture overview

The JEV decision-making system follows a simple, explainable pipeline:

1. Collect decision options and their attributes.
2. Score each option using a weighted objective function.
3. Rank options by the final JEV score.
4. Present reasoning that highlights strengths, risks, and tradeoffs.

## Core components

- `DecisionOption`: the structured representation for each decision alternative.
- `JEVDecisionEngine`: calculates the score and produces ranked recommendations.
- `main.py`: example runner showing how to evaluate a scenario.

## Extensibility

This repository can easily be expanded into a richer AI product:

- Add historical data for learning
- Combine rule-based logic with LLM reasoning
- Add API endpoints with FastAPI
- Save rankings to a database or analytics platform
- Add scenario simulations and sensitivity analysis
