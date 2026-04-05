# pyforge-labs
A structured collection of hands-on codelabs for learning Python — from first steps to production-grade AI/ML systems.

## StudyBot (Google ADK) quick run

The StudyBot agent is in `studybot/agent.py`.

### CLI check

```bash
cd /workspaces/pyforge-labs
adk run studybot
```

### Web UI

```bash
cd /workspaces/pyforge-labs
adk web . --host 127.0.0.1 --port 8000 --allow_origins "regex:.*"
```

Open:

```text
http://127.0.0.1:8000/dev-ui
```

Notes:
- In remote/devcontainer sessions, forwarded browser origins can be blocked by default.
- `--allow_origins "regex:.*"` prevents `403 Forbidden` on session creation and `/run_sse`.
- If port 8000 is busy, find the process with `ss -ltnp | grep :8000` and stop it, then relaunch.
