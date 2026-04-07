import os
from pathlib import Path
from google.adk.agents import Agent
from studybot.tools import explain_topic, quiz_student, study_planner

def _load_local_env() -> None:
    env_candidates = [
        Path(__file__).with_name(".env"),
        Path(__file__).resolve().parents[1] / ".env",
    ]
    for env_path in env_candidates:
        if not env_path.exists():
            continue
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

os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "FALSE")

if not os.getenv("GOOGLE_API_KEY"):
    raise RuntimeError(
        "Missing GOOGLE_API_KEY. Create studybot/.env from studybot/.env.example "
        "or set GOOGLE_API_KEY in your environment."
    )

MODEL_NAME = os.getenv("STUDYBOT_MODEL", "gemini-2.5-flash-lite")

root_agent = Agent(
    model=MODEL_NAME,
    name="StudyBot",
    description="A helpful assistant for students to answer questions and provide explanations.",
    instruction="""You are StudyBot, an AI assistant designed to help students. 
    When a student asks you to explain something, use the explain_topic tool.
    Always be encouraging and clear.""",
    tools=[explain_topic, quiz_student, study_planner],
)

