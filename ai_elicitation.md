# AI-Generated Requirements

## Project
Campus Study Room Reservation System

## AI Tool
ChatGPT

## Prompt
I am designing a Campus Study Room Reservation System for university students. Please elicit the functional and non-functional requirements for this application. Include user stories and acceptance criteria.

## AI Response

The AI suggested expanding the original requirements to address edge cases, administrative controls, system integration, security, and compliance.

### User Story 9 — Check-In / Check-Out Enforcement

**As a student with an active reservation, I want to check into my reserved study room upon arrival so that unused rooms are freed up for other students if I no longer need them.**

#### Acceptance Criteria
- Students can check in through the app within 15 minutes before or after the reservation start time using methods such as a QR code or geolocation.
- If a student fails to check in within 15 minutes after the start time, the system marks the reservation as "No-Show" and releases the room.
- Students can manually check out early to free the remainder of their time slot.

### User Story 10 — Single Sign-On Integration

**As a student or administrator, I want to sign in using my university Single Sign-On credentials so that I do not need to manage a separate password.**

#### Acceptance Criteria
- Authentication requests are redirected to the university identity provider.
- Student and administrator permissions are mapped based on university directory information.
- Unauthenticated API requests return HTTP 401 Unauthorized.

### User Story 11 — Fair-Use Policy Controls

**As a university administrator, I want to set daily and weekly booking limits per student so that room access is distributed fairly.**

#### Acceptance Criteria
- A student cannot reserve more than 2 hours per day or 8 hours per week by default.
- Active and upcoming reservations count toward the limit.
- Canceled and expired reservations do not count toward the limit.
- Reservations exceeding the limit are rejected and the student is shown their remaining quota.

### User Story 12 — Group Reservations

**As a student leading a study group, I want to invite other group members to a reservation so that all members can see the room on their schedules.**

#### Acceptance Criteria
- The primary student can add group members using university email addresses.
- Invited students receive a notification.
- Invited students can view the reservation from their accounts.
- The reservation counts toward the primary student's quota.

### User Story 13 — Administrative Override and Reports

**As an administrator, I want to override existing reservations and view usage information so that I can resolve conflicts and evaluate room utilization.**

#### Acceptance Criteria
- Administrators can cancel student reservations for reasons such as maintenance or university events.
- Affected students are notified.
- Administrators can generate reports showing peak hours, popular buildings, no-show rates, and room utilization.

## Additional Non-Functional Requirements

### Database Concurrency
The booking system should use atomic transactions to prevent double-bookings when multiple students attempt to reserve the same room and time.

### Data Persistence and Backups
Database backups should run daily with a Recovery Point Objective of no more than 1 hour and a Recovery Time Objective of no more than 4 hours.

### Data Encryption
Data in transit should use TLS 1.3 encryption. Sensitive user information and tokens stored by the system should use AES-256 encryption.

### Role-Based Access Control
The system should enforce student and administrator privileges at the API level using the principle of least privilege.

### Web Accessibility
The user interface should comply with WCAG 2.1 Level AA and support keyboard navigation and screen readers.

### Mobile Responsiveness
The interface should support mobile, tablet, and desktop viewport sizes ranging from 320px to 1920px.