# Campus Study Room Reservation System
## Requirements Document

### Project Description
The Campus Study Room Reservation System allows university students to find and reserve available study rooms on campus. Students can search for rooms based on date, time, location, and capacity. The system prevents conflicting reservations and allows students to view or cancel their reservations. Administrators can manage rooms and temporarily make rooms unavailable.

## User Stories

### User Story 1 — Student Login
**As a student, I want to log in using my university account so that only authorized students can reserve study rooms.**

#### Acceptance Criteria
- Students must authenticate before making a reservation.
- Invalid login credentials must be rejected.
- A student must be logged in to view or modify their reservations.

### User Story 2 — Search for Available Rooms
**As a student, I want to search for available study rooms so that I can find a room that meets my needs.**

#### Acceptance Criteria
- Students can search by date and time.
- Students can filter rooms by building and capacity.
- Only rooms available during the entire requested period are displayed.
- Rooms marked unavailable by an administrator are excluded.

### User Story 3 — Reserve a Study Room
**As a student, I want to reserve an available study room so that I have a guaranteed place to study.**

#### Acceptance Criteria
- The student must select an available room, date, start time, and end time.
- A reservation cannot exceed 2 hours.
- The system rejects reservations that overlap an existing reservation for the same room.
- A successful reservation displays a confirmation.

### User Story 4 — View Reservations
**As a student, I want to view my upcoming reservations so that I can keep track of when and where I reserved a room.**

#### Acceptance Criteria
- The system displays the room, building, date, start time, and end time.
- Students can only view reservations associated with their own account.
- Past reservations are separated from upcoming reservations.

### User Story 5 — Cancel a Reservation
**As a student, I want to cancel a reservation I no longer need so that another student can use the room.**

#### Acceptance Criteria
- Students can cancel only their own reservations.
- A canceled reservation immediately makes the room available for that time period.
- The system asks the student to confirm before cancellation.
- The reservation is marked as canceled rather than permanently deleted.

### User Story 6 — Prevent Scheduling Conflicts
**As a student, I want the system to prevent conflicting reservations so that two students cannot reserve the same room at the same time.**

#### Acceptance Criteria
- The system checks availability before confirming a reservation.
- Overlapping reservations for the same room are rejected.
- Back-to-back reservations are permitted.
- If the room becomes unavailable before confirmation, the student receives an error and must choose another room or time.

### User Story 7 — Manage Study Rooms
**As an administrator, I want to manage study rooms so that the reservation system contains accurate room information.**

#### Acceptance Criteria
- Administrators can add new study rooms.
- Administrators can update a room's building, room number, and capacity.
- Administrators can mark a room unavailable for maintenance.
- Students cannot access administrator room-management functions.

### User Story 8 — Reservation Reminder
**As a student, I want to receive a reminder before my reservation so that I do not forget my scheduled study time.**

#### Acceptance Criteria
- The system sends a reminder 30 minutes before the reservation begins.
- The reminder identifies the building, room, and reservation time.
- Canceled reservations do not generate reminders.

## Non-Functional Requirements

### NFR 1 — Performance
At least 95% of room availability searches must return results within 2 seconds under a load of up to 100 concurrent users.

### NFR 2 — Availability
The reservation system must maintain at least 99.5% uptime per calendar month, excluding scheduled maintenance announced at least 24 hours in advance.

### NFR 3 — Security
After 5 consecutive failed login attempts within 10 minutes, the system must temporarily prevent additional login attempts for that account for 15 minutes.