"""Backward-compatible db export for older imports.

Prefer importing the DB instance from `app.db` in new code:
	from app.db import db
"""

from app.db import db

__all__ = ["db"]
