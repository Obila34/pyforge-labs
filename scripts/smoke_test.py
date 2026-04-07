import asyncio
import os
import sys
from pathlib import Path

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from studybot.agent import root_agent


async def main() -> int:
    app_name = "studybot-smoke"
    user_id = "smoke-user"

    if not os.getenv("GOOGLE_API_KEY"):
        print("ERROR: GOOGLE_API_KEY is not set.")
        print("Create studybot/.env from studybot/.env.example, then retry.")
        return 1

    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=app_name, user_id=user_id)
    runner = Runner(app_name=app_name, agent=root_agent, session_service=session_service)

    message = types.Content(
        role="user",
        parts=[types.Part(text="Explain Python functions in two sentences.")],
    )

    chunks = []
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session.id,
        new_message=message,
    ):
        if not event.content or not event.content.parts:
            continue
        for part in event.content.parts:
            text = getattr(part, "text", None)
            if text:
                chunks.append(text)

    final_text = "".join(chunks).strip()
    if not final_text:
        print("ERROR: Agent returned no text response.")
        return 1

    print("Smoke test passed.")
    print(final_text[:500])
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
