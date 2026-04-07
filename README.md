# pyforge-labs

A structured collection of hands-on codelabs for learning Python, including a StudyBot example built with Google ADK.

## StudyBot (Google ADK) - Ready-To-Run Setup

The StudyBot agent is implemented in `studybot/agent.py`, with tools in `studybot/tools.py`.

### 1) Create and activate a virtual environment

```bash
cd /workspaces/pyforge-labs
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Configure environment variables

```bash
cp studybot/.env.example studybot/.env
```

Then edit `studybot/.env` and set:

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

Optional model override:

```env
STUDYBOT_MODEL=gemini-2.5-flash-lite
```

### 4) Run a smoke test (recommended)

```bash
python scripts/smoke_test.py
```

Expected result: `Smoke test passed.` followed by a short StudyBot response.

### 5) Run the ADK web UI

```bash
adk web . --host 127.0.0.1 --port 8000 --allow_origins "regex:.*"
```

Open `http://127.0.0.1:8000/dev-ui`.

## Troubleshooting: "No response"

- Missing or invalid API key: run `python scripts/smoke_test.py` first; if it fails, fix `studybot/.env`.
- CORS/session issues in remote containers: keep `--allow_origins "regex:.*"` in the `adk web` command.
- Streaming stalls in UI: turn off token streaming in the top-right of ADK Dev UI and resend.
- Port conflicts: run `ss -ltnp | grep :8000` and stop the conflicting process, then restart ADK.
