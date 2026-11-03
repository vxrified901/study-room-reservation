
# M8 Runbook — Study Room Listing Failure

## Application
Campus Study Room Reservation System

## Incident: Study Room Page Returns HTTP 500

### Observable Symptoms
- A user visits the application homepage.
- Instead of seeing the available study rooms, the user
  receives an HTTP 500 Internal Server Error.
- The application may record a database_error event.

### Confirm the Problem
1. Open the application homepage at:
   http://127.0.0.1:5000/

2. Confirm whether the webpage displays an HTTP 500 error.

3. Check the application terminal for JSON log records.

4. Look for an event named database_error.

5. Find the request_id associated with the error.

6. Use that request_id to locate the corresponding
   request_started and request_completed events.

7. Inspect the error_type field to identify the SQLite
   error category.

### Troubleshooting
1. Verify that rooms.db exists in the application directory.

2. Confirm the application has permission to access
   the database file and its containing directory.

3. Verify the database contains the rooms table.

4. Check whether another process is locking the database.

5. Confirm that the DATABASE setting in app.py points
   to the intended SQLite database.

### Recovery Procedure
1. Stop the Flask development server using Ctrl+C.

2. Back up the existing rooms.db file before modifying it.

3. Correct any identified file permission or path problems.

4. If the database is missing, determine whether a backup
   is available before creating a replacement.

5. Restore the database from a known-good backup when
   necessary.

6. Restart the application:
   python app.py

7. Reload the homepage and verify that room records appear.

8. Confirm that the request_completed event reports
   status 200 and that rooms_loaded is recorded.

### Escalation
If the database cannot be recovered or the error continues,
contact the project maintainer or repository owner.

Do not delete or overwrite the database without preserving
a backup first.

### Verification
The incident is resolved when:
- The homepage returns HTTP 200.
- Room records are displayed correctly.
- The application logs show a successful request.
- No database_error event occurs for the verification request.
