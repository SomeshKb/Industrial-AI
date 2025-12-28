# Industrial-AI — Backend

This repository contains the Flask backend for the Industrial-AI Anomaly Detection service.

IMPORTANT: the project was refactored to a clean `app/` package layout. Legacy top-level
folders (`models/`, `routes/`, `services/`, `constants/`) have been turned into lightweight
shims that forward to the new implementation under `app/`. After you verify everything
works in your environment you can remove those legacy folders.

Quick start
-----------

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run the app (development):

```bash
python app.py
```

API
---
- Base URL: `/api/v1`
- Example endpoints:
	- `GET /api/v1/models` — list models (supports `limit`, `offset`, `status`, `name` query params)
	- `POST /api/v1/models` — create a model (JSON: `{ "name": "..." }`)
	- `GET /api/v1/models/{id}` — get by id

Project layout (important files)
-------------------------------

- `app/__init__.py` — application factory `create_app()`
- `app/core/config.py` — configuration
- `app/db/__init__.py` — SQLAlchemy instance
- `app/models/anomaly_model.py` — SQLAlchemy model (UUID primary key)
- `app/schemas/anomaly_model_schema.py` — marshmallow schemas
- `app/services/anomaly_model_service.py` — business logic layer (no Flask imports)
- `app/api/v1/routes/anomaly_model.py` — HTTP routes (uses services & schemas)

Notes
-----
- The refactor follows separation of concerns: routes (HTTP) → schemas (validation) → services
	(business logic) → models (persistence).
- Database: SQLite by default (`sqlite:///app.db`).
- API versioning: `/api/v1/*`.

If you want me to remove the legacy folders entirely, I can do that next — but I left
shims in place to avoid breaking any external scripts during the transition.

