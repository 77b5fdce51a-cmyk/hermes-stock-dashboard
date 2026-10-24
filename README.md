# Hermes Stock Dashboard

10 subsystems, each backed by a Google Sheet + Google AI Studio (Gemini).
One Streamlit dashboard combines them all.

## Structure
- `app.py` — main dashboard
- `core/` — Google Sheets + AI clients
- `subsystems/` — 10 subsystem modules
- `scripts/` — helper scripts (setup, deploy, etc.)

## Setup
1. Create a Google Cloud project, enable Sheets API, create a service account, download JSON key.
2. Create 10 Google Sheets (or 1 Sheet with 10 tabs). Share each with the service account email.
3. Copy `.env.example` to `.env` and fill in values.
4. `pip install -r requirements.txt`
5. `streamlit run app.py`
