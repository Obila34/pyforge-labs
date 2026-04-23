# pyforge-labs

This is where I keep my Python experiments and learning projects. Right now the main thing here is **StudyBot** — an AI study assistant I built using Google's Agent Development Kit (ADK). It can explain topics, quiz you, and put together a study plan when you have an exam coming up.

I put the full walkthrough in `StudyBot_Complete_Codelab.ipynb` if you want to follow along with how I built it. Or you can just clone and run it directly using the instructions below.

---

## What StudyBot does

- **Explain any topic** at beginner, intermediate, or advanced level
- **Quiz you** with multiple choice questions and mark your answers
- **Build a study plan** day-by-day when you tell it how much time you have

The agent lives in `studybot/agent.py` and its tools are in `studybot/tools.py`. Pretty straightforward once you see the structure.

---

## Running it locally

You'll need Python 3.10+ and a [Google AI Studio](https://aistudio.google.com/apikey) API key (free tier works fine).

**Clone the repo**

```bash
git clone https://github.com/Obila34/pyforge-labs.git
cd pyforge-labs
```

**Create a virtual environment and install dependencies**

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Set up your API key**

```bash
cp studybot/.env.example studybot/.env
```

Open `studybot/.env` and drop in your key:

```env
GOOGLE_API_KEY=your_google_ai_studio_api_key
GOOGLE_GENAI_USE_VERTEXAI=FALSE
```

There's also an optional `STUDYBOT_MODEL` variable if you want to swap models (defaults to `gemini-2.5-flash-lite`).

**Do a quick sanity check**

```bash
python scripts/smoke_test.py
```

If it prints `Smoke test passed.` and some text about Python functions, you're good to go. If it errors, the most likely culprit is the API key — double-check `studybot/.env`.

**Launch the web UI**

```bash
adk web . --host 127.0.0.1 --port 8000 --allow_origins "regex:.*"
```

Then open [http://127.0.0.1:8000/dev-ui](http://127.0.0.1:8000/dev-ui) in your browser and start chatting.

---

## Troubleshooting

**"No response" in the UI** — Run the smoke test first. If that fails, the issue is almost definitely the API key.

**CORS errors in a remote dev container** — Make sure you're including `--allow_origins "regex:.*"` in the `adk web` command.

**Responses seem to stall** — Try turning off token streaming using the toggle in the top-right corner of the ADK Dev UI, then resend your message.

**Port already in use** — Find what's on 8000 with `ss -ltnp | grep :8000` (Linux/Mac) or `netstat -ano | findstr :8000` (Windows), kill it, and try again.
