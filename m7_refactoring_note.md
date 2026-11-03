
# M7 Refactoring Note
## Campus Study Room Reservation System

### Code Smell: Mixed Responsibilities

Before refactoring, the view_rooms() function handled
database access, room retrieval, and HTML generation.

This mixed database responsibilities with HTTP response
handling, making the function harder to maintain and test
independently.

### Refactoring Performed: Extract Function

I extracted the SQLite room-retrieval query into a new
get_rooms() function.

The view_rooms() function now calls get_rooms() and
uses the returned records to generate the same HTML.

No room data, routes, or displayed information were
intentionally changed.

### What Became Easier

Database retrieval is now separated from webpage rendering.

This makes it easier to modify the database query without
changing the HTML generation logic.

The get_rooms() function can also be tested independently
in future milestones.

### Behavior Preservation

Before refactoring:
4 tests passed in 0.45 seconds.

After refactoring:
4 tests passed in 0.39 seconds.

The same four tests were used without modifications.

The passing tests provide evidence that the existing
tested behavior was preserved.
