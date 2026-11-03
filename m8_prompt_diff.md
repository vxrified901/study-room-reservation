
# M8 Prompt-and-Diff Log
## Campus Study Room Reservation System

### AI Assistance
I used ChatGPT to help implement structured JSON logging,
request correlation, and an incident response runbook.

### Prompt Summary
I provided the M8 assignment requirements and asked
for help making my existing Flask application observable.

### Changes to app.py
- Added JSON-formatted structured logging.
- Added consistent timestamp, level, event, and
  request_id fields.
- Added a unique request ID for each HTTP request.
- Added request_started and request_completed events.
- Added rooms_loaded with the number of rooms retrieved.
- Added database_error logging for SQLite failures.

### Log Evidence
File: m8_sample_logs.jsonl

A single request produces three structured events:
1. request_started
2. rooms_loaded
3. request_completed

The request_id correlates the three events.

### Runbook
File: m8_runbook.md

Documented how to recognize, diagnose, and recover
from an HTTP 500 error caused by database access failure.

### Testing
Command:
python -m pytest -v

Result:
4 tests passed in 0.48 seconds.

The existing room-listing functionality remains working.

### Limitations
The logging demonstrates observability for the current
room-listing feature. The application is a development
prototype and does not include centralized log collection
or production monitoring.
