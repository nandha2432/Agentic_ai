"""EXERCISE 4 - Evaluator-Optimizer on your own task."""

import _path  # noqa: F401
from agentcore import Agent, EvaluatorOptimizer


# ---------------------------------------------------------------- YOUR CODE

TASK = """
Write a short professional abstract for a college project called
"Blind Stick Safety System". The project uses an ultrasonic sensor to
detect obstacles and an ESP8266 to send safety alerts to a mobile app.
The abstract should explain the problem, solution, and main benefits.
Keep it between 80 and 120 words.
"""

CRITERIA = [
    "The abstract must contain between 80 and 120 words.",
    "The abstract must mention the ultrasonic sensor.",
    "The abstract must mention ESP8266 and the mobile app.",
    "The abstract must clearly explain the problem, solution, and benefit in clear professional English.",
]

# ------------------------------------------------------------ END YOUR CODE


if TASK.startswith("TODO"):
    raise SystemExit("Fill in TASK and CRITERIA first, then run this again.")

writer = Agent(
    name="Writer",
    instructions="You write clear, professional English.",
    temperature=0.7,
)

loop = EvaluatorOptimizer(
    generator=writer,
    criteria=CRITERIA,
    max_rounds=3
)

outcome = loop.run(TASK)

print(f"\n  passed: {outcome['passed']}   rounds: {outcome['rounds']}\n")
print(outcome["output"])

print("\n--- review history ---")
for entry in outcome["history"]:
    print(f"  {entry}")