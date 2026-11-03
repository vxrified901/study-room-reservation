
# M7 Prompt-and-Diff Log
## Campus Study Room Reservation System

### AI Assistance

I used ChatGPT to identify a structural problem in
my existing Flask application and plan a refactoring
that would preserve the application's behavior.

### Prompt Summary

I provided the M7 assignment requirements and worked
through identifying a code smell, refactoring the
application, and verifying the results with my M6 tests.

### Original Structure

The view_rooms() function contained the SQLite query
and generated the HTML response.

### Changes Made

File: app.py

- Added get_rooms() to retrieve room records from SQLite.
- Removed direct database access from view_rooms().
- Updated view_rooms() to call get_rooms().
- Preserved the existing route and HTML output.

### Test Verification

Command used before and after:

python -m pytest -v

Before:
4 passed in 0.45 seconds.

After:
4 passed in 0.39 seconds.

The test suite was not modified during the refactor.

### Diff Evidence

The before-and-after structural changes are recorded
in the Git diff for app.py.

### Limitations

The tests demonstrate preservation of the behavior
covered by the existing M6 suite. They do not prove
that every possible application behavior is unchanged.
