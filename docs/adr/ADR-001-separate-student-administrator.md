# ADR-001: Separate Student and Administrator Domain Entities

**Status:** Accepted  
**Date:** October 6, 2026

## Context

The Campus Study Room Reservation System has two primary types of users: students and administrators.

The M2 requirements give these users different responsibilities. Students authenticate with their university accounts, search for available rooms, create reservations, view their reservations, and cancel their own reservations. Administrators add and update study rooms and mark rooms unavailable for maintenance.

During domain modeling, two approaches were considered. The original AI-generated domain model used a single `USER` entity with a `role` attribute. The revised domain model instead used separate `STUDENT` and `ADMINISTRATOR` entities.

The decision affects how responsibilities and relationships are represented. A single user entity simplifies account management, while separate entities make the different responsibilities more explicit.

## Decision

The system will use separate `STUDENT` and `ADMINISTRATOR` domain entities rather than a single `USER` entity with a role attribute.

Students will be associated with reservations, while administrators will be associated with managing study rooms.

This decision reflects the current requirements and the final domain model created for M3.

## Alternatives Considered

### Alternative 1: Single USER Entity With a Role Attribute

This approach would represent students and administrators using one `USER` entity with a `role` attribute containing values such as `STUDENT` or `ADMINISTRATOR`.

This was a genuine alternative because the original AI-generated domain model used it. It would simplify authentication, shared account information, and future role changes.

It was not selected because the current requirements give students and administrators different responsibilities. Separate entities make their relationships to reservations and rooms more explicit.

### Alternative 2: USER, ROLE, and PERMISSION Entities

Another approach would use a generic `USER` entity connected to separate `ROLE` and `PERMISSION` entities.

This would support flexible authorization and allow users to have multiple roles.

It was not selected because the current system only defines two user types with fixed responsibilities. Introducing additional entities would make the domain model more complex without addressing a current requirement.

## Consequences

### Benefits

- Student reservation responsibilities and administrator room-management responsibilities are represented separately.
- The domain model makes it easier to understand which actors are associated with reservations and room management.
- The model avoids introducing a larger role and permission system that is not currently required.

### What Becomes Harder

- **Authentication:** The application may need additional logic to determine whether an authenticated university account belongs to a student or an administrator.
- **Multiple roles:** A person who is both a student and an administrator may require two linked records or additional account-management logic.
- **Role changes:** Changing someone from a student to an administrator becomes more complicated than updating a single role attribute.
- **Duplicated information:** Both entities contain shared attributes such as university ID and email, potentially requiring duplicated validation or a shared identity mechanism later.
- **Future flexibility:** If the system introduces additional roles, the separate-entity design may require more structural changes than a role-based approach.

Overall, this decision prioritizes clarity in the current domain model over flexibility in future account and role management.
