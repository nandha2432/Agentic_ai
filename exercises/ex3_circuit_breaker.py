import _path  # noqa: F401
from agentcore import Agent, ToolRegistry, tool
from agentcore.demo_tools import CAMPUS_INSTRUCTIONS


# ---------------------------------------------------------------- YOUR CODE
@tool
def check_exam_results(roll_number: str) -> dict:
    """Fetch a student's latest examination results.

    Call this whenever the user asks about marks, grades or results.

    Args:
        roll_number: The roll number, for example 21CS045.
    """

    # Simulate a broken results server
    raise ConnectionError(
        "results server unreachable (timeout after 5s)"
    )
# ------------------------------------------------------------ END YOUR CODE


agent = Agent(
    name="Campus Assistant",
    instructions=CAMPUS_INSTRUCTIONS,
    registry=ToolRegistry([check_exam_results]),
    max_iterations=10,
)

result = agent.run("What are the exam results for 21CS045?")

print(f"\n{result.output}\n")
print(result.trace.render())

failures = [
    s for s in result.trace.steps
    if s.kind == "tool" and not s.ok
]

disabled = [
    s for s in failures
    if "ToolDisabled" in s.detail
]

print(f"""
  tool attempts : {len(failures)}
  outcome       : {result.trace.outcome}
  breaker fired : {bool(disabled)}

  Expected: attempts stop shortly after 3, outcome is "completed",
  and the agent tells the user the results service is unavailable.
""")