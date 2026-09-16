import _path  # noqa: F401
from agentcore import Agent, tool
from agentcore.demo_tools import campus_registry, CAMPUS_INSTRUCTIONS

NOTICES: list[dict] = []


# ---------------------------------------------------------------- YOUR CODE
@tool
def send_notice(roll_number: str, subject: str, body: str) -> dict:
    """
    Send a notice to a student and return a confirmation.

    Call this tool when the user asks to inform, notify, or tell a
    student something. Do not call this tool when the user only asks
    for information or wants to look up something about a student.

    Args:
        roll_number: The roll number of the student who should receive the notice.
        subject: The subject or title of the notice.
        body: The message that should be sent to the student.
    """
    NOTICES.append({
        "roll_number": roll_number,
        "subject": subject,
        "body": body
    })

    return {
        "sent": True,
        "to": roll_number,
        "subject": subject
    }
# ------------------------------------------------------------ END YOUR CODE


registry = campus_registry()
registry.register(send_notice)

agent = Agent(
    name="Campus Assistant",
    instructions=CAMPUS_INSTRUCTIONS,
    registry=registry
)

for question in [
    "What is Priya's fee balance?",
    "Inform Priya about her outstanding fee balance.",
]:
    print("\n" + "=" * 74)
    print(f"Q: {question}")

    result = agent.run(question)

    print(f"\n{result.output}\n")
    print(result.trace.render())

print(f"\n  notices recorded: {len(NOTICES)}   (expected: 1)")

if len(NOTICES) != 1:
    print("  -> Your docstring is not doing its job. Rewrite it and run again.")