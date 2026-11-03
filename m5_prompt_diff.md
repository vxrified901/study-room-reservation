# M5 — Walking Skeleton Prompt-and-Diff Log

## Project

Campus Study Room Reservation System

## AI Tool Used

ChatGPT

## Objective

Implement a working end-to-end application feature using Python, connect it to persistent storage, configure continuous integration, and verify that automated checks pass on GitHub.

## AI Assistance and Prompts

### Prompt 1: Walking Skeleton Implementation

**Task given to AI:** Help implement one genuine end-to-end feature for the Campus Study Room Reservation System using Python.

**AI-generated solution:** ChatGPT suggested using Flask and SQLite to implement a page that displays available study rooms.

The application includes a Flask route that receives an HTTP request, queries room records from SQLite, and returns the results to the browser.

### Prompt 2: Database Verification

**Task given to AI:** Help verify that the webpage retrieves real database records rather than displaying hardcoded information.

**AI-generated solution:** ChatGPT provided a command to update the capacity of an existing study room in SQLite.

**Verification performed:** I changed Library Room 101's capacity from 4 to 10. After refreshing the webpage, the updated capacity appeared, confirming that the application retrieved data from the database.

### Prompt 3: Automated Testing

**Task given to AI:** Help create an automated test to verify that the application retrieves room information from SQLite.

**AI-generated solution:** ChatGPT provided a pytest test using a temporary SQLite database and Flask's test client.

**Verification performed:** I ran the test locally using `python -m pytest -v`. The test passed.

### Prompt 4: Continuous Integration

**Task given to AI:** Help configure GitHub Actions to automatically check the Python application and run automated tests.

**AI-generated solution:** ChatGPT provided a GitHub Actions workflow that installs dependencies, checks Python compilation, and executes pytest.

**Verification performed:** I committed and pushed the workflow to GitHub. GitHub Actions successfully completed the `build-and-test` job.

## Changes and Adjustments During Implementation

1. Created `app.py` to implement the Flask application and SQLite integration.
2. Created `test_app.py` to verify that database changes appear in the HTTP response.
3. Created `.github/workflows/ci.yml` to automate compilation checks and testing.
4. Created `.gitignore` to exclude local database files and temporary Python files from version control.
5. Corrected the location of `.gitignore` so it applied to the project root.
6. Installed and configured Git, connected the local project to the existing GitHub repository, and preserved earlier project documentation.
7. Configured Git identity and completed GitHub authentication to push the M5 changes.

## Accepted AI Suggestions

- Use Flask for the initial Python web application.
- Use SQLite for persistent storage.
- Implement a small room-listing feature as the first end-to-end slice.
- Use pytest for automated testing.
- Use GitHub Actions for continuous integration.
- Verify the database connection through an observable change in the webpage.

## Revisions and Limitations

The initial implementation was intentionally limited to viewing study rooms. Authentication, reservation creation, cancellation, and administrator management were deferred to later development.

The initial database contains sample room records, but the webpage retrieves them through SQL queries rather than returning a fixed list.

The local database file was excluded from Git. Automated tests create a separate temporary database to ensure that the CI workflow does not depend on local machine state.

## Final Outcome

The walking skeleton successfully demonstrated a real request traveling from the browser through Flask to SQLite and back.

The application displayed study room records and reflected a database update after the page was refreshed.

The automated test passed locally, and the GitHub Actions workflow completed successfully with a green `build-and-test` job.

This milestone established a working foundation for implementing additional reservation system features in future sprints.