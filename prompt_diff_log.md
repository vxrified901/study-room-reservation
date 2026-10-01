# Prompt-and-Diff Log

## Project
Campus Study Room Reservation System

## AI Tool
ChatGPT

## Prompt Given to AI

I am designing a Campus Study Room Reservation System for university students. Please elicit the functional and non-functional requirements for this application. Include user stories and acceptance criteria.

## Purpose

The AI was given a general description of the project so that I could compare its suggested requirements with the requirements I developed for the system.

## Differences Between My Requirements and the AI Output

### 1. Scheduling Conflicts
**My Requirement:** Overlapping reservations are rejected, while back-to-back reservations are allowed.

**AI Output:** The AI discussed preventing double bookings and handling simultaneous reservation attempts.

**Decision:** Keep my original requirement and add the AI's concurrency idea as a possible improvement. My requirement defines expected scheduling behavior more clearly.

### 2. Maximum Reservation Length
**My Requirement:** A single reservation cannot exceed 2 hours.

**AI Output:** The AI added a limit of 2 hours per day and 8 hours per week.

**Decision:** Keep my requirement. The weekly quota was not part of the original project scope.

### 3. Check-In System
**My Requirement:** No physical check-in is required.

**AI Output:** The AI added QR code or geolocation-based check-in and check-out.

**Decision:** Reject. This adds unnecessary complexity to the current version of the system.

### 4. No-Show Handling
**My Requirement:** No automatic no-show policy was included.

**AI Output:** Reservations are automatically released if the student does not check in within 15 minutes.

**Decision:** Defer. This could be useful in the future, but it depends on implementing a check-in system.

### 5. University SSO
**My Requirement:** Students must authenticate, but no specific authentication technology was selected.

**AI Output:** The AI specified university SSO using technologies such as OAuth2, SAML, or CAS.

**Decision:** Defer. Authentication is necessary, but the specific implementation should be decided during system design.

### 6. Group Reservations
**My Requirement:** Reservations belong to an individual student.

**AI Output:** Students can invite group members using university email addresses.

**Decision:** Reject. Group reservation management was not part of the original project scope.

### 7. Administrative Override
**My Requirement:** Administrators can mark study rooms unavailable.

**AI Output:** Administrators can also cancel existing reservations when necessary.

**Decision:** Accept. This handles cases such as emergency maintenance that I had not fully considered.

### 8. Usage Analytics
**My Requirement:** No analytics or reporting feature was included.

**AI Output:** Administrators can generate reports about peak hours, room popularity, no-shows, and utilization.

**Decision:** Defer. This could be useful in a future version but is unnecessary for the initial system.

### 9. Simultaneous Reservations
**My Requirement:** Availability is checked before a reservation is confirmed.

**AI Output:** The AI explicitly considered two students attempting to reserve the same room at nearly the same time.

**Decision:** Accept. This identifies an important edge case that should be considered.

### 10. Accessibility
**My Requirement:** Accessibility standards were not explicitly specified.

**AI Output:** The system should comply with WCAG 2.1 Level AA.

**Decision:** Accept. This is a useful requirement that I had overlooked.

### 11. Encryption
**My Requirement:** Access controls and authentication are required, but specific encryption technologies were not selected.

**AI Output:** The AI specified TLS 1.3 and AES-256.

**Decision:** Defer. Security is important, but these specific technologies should not be assumed without further system-design decisions.

### 12. Database Backups
**My Requirement:** No backup requirements were specified.

**AI Output:** The AI specified daily backups, an RPO of no more than 1 hour, and an RTO of no more than 4 hours.

**Decision:** Defer. This may be useful for a production system but was not part of the original project scope.

## Changes After Reviewing the AI Output

After reviewing the AI-generated requirements, I identified three ideas that could improve a future revision of my requirements:

1. Handle simultaneous reservation attempts so that only one student can successfully reserve the same room and time.
2. Allow administrators to cancel existing reservations when a room unexpectedly becomes unavailable.
3. Require the user interface to meet an established accessibility standard such as WCAG 2.1 Level AA.

I would not immediately add the AI-generated check-in system, geolocation, QR codes, weekly quotas, group reservations, analytics, or specific authentication and encryption technologies because these were not established as part of the original project scope.

## Final Assessment

The comparison showed that AI was useful for identifying edge cases and possible improvements, but it also generated requirements based on assumptions that I never provided. The AI output works better as a source of possible requirements and questions than as a final requirements specification. Each AI-generated requirement still needs human review before being accepted into the project.
