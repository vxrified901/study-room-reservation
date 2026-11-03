
# M6 — Testing, Coverage, and Bug Injection
## Campus Study Room Reservation System

### AI Assistance
ChatGPT was used to help design additional automated tests,
select a meaningful bug to inject, and document the results.

### Original Application
The M5 walking skeleton uses Flask and SQLite to display
study rooms and their capacities through the homepage.

### Tests Added
1. Database initialization creates three expected rooms.
2. Reinitialization preserves existing room changes.
3. An empty database displays no room entries.

The existing acceptance test verifies that changing a room's
capacity in SQLite changes the HTTP response.

### Coverage
Command:
python -m pytest -v --cov=app --cov-report=term-missing --cov-report=html

Result:
4 tests passed.
91% code coverage.

### Bug Injection
File: app.py

Original:
html += f"<p>{name} - Capacity: {capacity}</p>"

Injected:
html += f"<p>{name} - Capacity: {capacity + 1}</p>"

The injected bug incorrectly increases the displayed capacity
of every room by one seat.

### Failure Evidence
Command:
python -m pytest -v

Result:
1 failed, 3 passed.

The acceptance test detected that the application displayed
an incorrect capacity.

### Fix
The original capacity expression was restored.

Result:
4 passed.
91% coverage.

### Files Changed
- test_app.py: Added three tests.
- app.py: Temporarily injected and reverted the capacity bug.
- m6_bug_injection.diff: Recorded the deliberate fault.
- m6_prompt_diff.md: Documented the testing process.

### Limitations
The tests cover the current M5 room-listing feature.
Reservation creation, authentication, and conflict detection
are not implemented or tested in this milestone.
