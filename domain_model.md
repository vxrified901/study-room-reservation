# Campus Study Room Reservation System
## Domain Model

```mermaid
erDiagram
    STUDENT ||--o{ RESERVATION : makes
    ROOM ||--o{ RESERVATION : receives
    ADMINISTRATOR ||--o{ ROOM : manages

    STUDENT {
        uuid studentId PK
        string universityId UK
        string email
    }

    ADMINISTRATOR {
        uuid adminId PK
        string universityId UK
        string email
    }

    ROOM {
        uuid roomId PK
        string building
        string roomNumber
        int capacity
        boolean maintenanceUnavailable
    }

    RESERVATION {
        uuid reservationId PK
        uuid studentId FK
        uuid roomId FK
        datetime startTime
        datetime endTime
        string status
    }
```

## Model Rules

- A student can make zero or many reservations.
- Each reservation belongs to exactly one student.
- A room can have zero or many reservations over time.
- Each reservation is for exactly one room.
- An administrator can manage multiple rooms.
- Reservations for the same room cannot overlap.
- Back-to-back reservations are allowed.
- A reservation cannot exceed two hours.
- Canceled reservations remain stored with a canceled status.
- Rooms marked unavailable for maintenance cannot be reserved.