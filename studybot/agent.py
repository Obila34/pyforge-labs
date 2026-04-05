import os
from pathlib import Path
from google.adk.agents import Agent
from studybot.tools import explain_topic, quiz_student, study_planner

def _load_local_env() -> None:
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)

_load_local_env()

root_agent = Agent(
    model="gemini-2.5-flash-lite",
    name="StudyBot",
    description="A helpful assistant for students to answer questions and provide explanations.",
    instruction="""You are StudyBot, an AI assistant designed to help students. 
    When a student asks you to explain something, use the explain_topic tool.
    Always be encouraging and clear.""",
    tools=[explain_topic, quiz_student, study_planner],
)