# Domain Model Prompt-and-Diff Log

## Project
Campus Study Room Reservation System

## AI Tool
ChatGPT

## Prompt Given to AI

I am developing a Campus Study Room Reservation System.

My M2 requirements are:

- Students authenticate using their university account.
- Students can search for available study rooms by date, time, building, and capacity.
- Students can reserve an available room for a maximum of 2 hours.
- The system must prevent overlapping reservations for the same room but allow back-to-back reservations.
- Students can view their upcoming and past reservations.
- Students can cancel their own reservations. Canceled reservations remain in the system rather than being deleted.
- Administrators can add study rooms and update their building, room number, and capacity.
- Administrators can mark rooms unavailable for maintenance.
- The system sends students a reminder 30 minutes before a reservation.
- Students cannot access administrator room-management functions.

Please draft a domain model for this application as an ER diagram using Mermaid. Include the entities, important attributes, relationships, and cardinalities that you believe are necessary. Do not ask me questions first; make a reasonable first draft based only on these requirements.

## AI First Draft

The AI produced three entities:

- USER
- ROOM
- RESERVATION

The AI modeled USER as having a role of either STUDENT or ADMIN and connected USER to RESERVATION. ROOM was also connected to RESERVATION.

## Changes Made in My Model

### 1. USER Split Into STUDENT and ADMINISTRATOR

**AI:** Used one USER entity with a role attribute.

**Mine:** Uses separate STUDENT and ADMINISTRATOR entities.

**Reason:** The M2 requirements give students and administrators different responsibilities. Students make reservations, while administrators manage rooms. Separating them makes those relationships explicit.

### 2. Administrator-to-Room Relationship Added

**AI:** Did not show a relationship between administrators and rooms.

**Mine:** ADMINISTRATOR manages ROOM.

**Reason:** M2 specifically states that administrators can add, update, and mark rooms unavailable.

### 3. Room Status Changed

**AI:** Used a ROOM status of AVAILABLE or MAINTENANCE.

**Mine:** Uses a maintenanceUnavailable boolean.

**Reason:** Whether a room is available also depends on existing reservations for the requested time. Availability should not be treated as only a permanent room status.

### 4. Reservation Date and Time Changed

**AI:** Used reservationDate, startTime, and endTime.

**Mine:** Uses datetime startTime and datetime endTime.

**Reason:** A reservation represents a time interval. Datetime values directly identify the beginning and end of that interval and simplify checking duration and overlap rules.

### 5. reminderSent Removed

**AI:** Added a reminderSent boolean to RESERVATION.

**Mine:** Does not include reminderSent.

**Reason:** M2 requires the system to send a reminder, but it does not require reminder-delivery state to be part of the core domain model.

## Elements Kept From the AI Draft

I kept ROOM and RESERVATION as core entities because they directly trace to the M2 requirements.

I also kept the concept that one student can have multiple reservations and one room can have multiple reservations over time.

The room attributes building, room number, and capacity were retained because students use these properties when searching for rooms and administrators can modify them.

## Entities Intentionally Not Added

I did not add separate ROLE, PERMISSION, SETTINGS, AUDIT_LOG, NOTIFICATION, or BUILDING entities. The M2 requirements do not require these concepts to exist independently in the domain model.

Adding them would increase the complexity of the model without providing a clear requirement-based reason for doing so.

## Final Result

The AI draft contained a useful basic structure and did not severely over-model the application. My final model keeps that simplicity while making the different responsibilities of students and administrators more explicit and representing room availability and reservation time more accurately.