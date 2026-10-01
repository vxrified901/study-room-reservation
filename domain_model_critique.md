# AI Domain Model Critique

## Project
Campus Study Room Reservation System

## Overview

The AI-generated domain model used three entities: USER, ROOM, and RESERVATION. My revised model uses four entities: STUDENT, ADMINISTRATOR, ROOM, and RESERVATION. The AI draft was relatively simple and avoided many common over-modeling problems, but I changed several structural choices so that my model more directly represents the requirements from M2.

## Where the AI Over-Modelled

The AI did not significantly over-model the application. It avoided creating unnecessary entities such as ROLE, PERMISSION, SETTINGS, AUDIT_LOG, or a separate BUILDING entity. None of those entities were required by my M2 requirements.

One small example of unnecessary implementation detail is the `reminderSent` boolean inside RESERVATION. My requirement states that the system sends a reminder 30 minutes before a reservation, but it does not require the domain model to store whether a reminder was sent. I left this attribute out of my model because it describes implementation bookkeeping rather than a core concept of the reservation domain.

## Where the AI Under-Modelled

The AI represented both students and administrators with a single USER entity and a `role` attribute. This is workable, but it does not clearly represent the different responsibilities described in my requirements.

Students create, view, and cancel reservations, while administrators manage rooms and mark them unavailable for maintenance. My model therefore separates STUDENT and ADMINISTRATOR so that their relationships are explicit. STUDENT is related to RESERVATION through "makes," while ADMINISTRATOR is related to ROOM through "manages."

The AI model also did not represent the administrator-to-room management relationship at all. This leaves the requirement that administrators manage rooms visible only as an implied behavior instead of part of the domain structure.

## Relationships the AI Guessed

The AI states that a USER can make many RESERVATION records. However, the USER entity can have either the STUDENT or ADMIN role. This structure technically allows an administrator to participate in the "makes" relationship even though my requirements only state that students make reservations.

The AI also describes ROOM as having a `status` of either AVAILABLE or MAINTENANCE. This simplifies two different ideas into one attribute. A room can be unavailable because it is under maintenance, but whether a room is available for a requested time also depends on its existing reservations. Therefore, "AVAILABLE" is not necessarily a permanent state of a room.

My model instead uses `maintenanceUnavailable` to represent the administrator-controlled maintenance condition. Reservation availability can then be determined from the room's reservations and the requested time interval.

## Where the AI Was Right

The AI correctly identified ROOM and RESERVATION as core entities. Both are directly supported by the M2 requirements.

It also correctly modeled the relationship between rooms and reservations. A room can have multiple reservations over time, while each reservation is associated with one room.

The AI correctly recognized that a student can make multiple reservations and that each reservation needs to identify who made it.

It also correctly included the room's building, room number, and capacity. These attributes trace directly to the requirements for searching rooms and allowing administrators to update room information.

The AI also made a good decision by keeping the model relatively small. It did not automatically create separate Role, Permission, Settings, AuditLog, Notification, or Building entities without evidence that the application required them.

## Differences in Reservation Time Modeling

The AI uses three separate attributes: `reservationDate`, `startTime`, and `endTime`.

My model uses `startTime` and `endTime` as datetime values. I chose this structure because a reservation represents a time interval. Storing the date and time together makes the start and end of that interval explicit and supports the requirement that reservations for the same room cannot overlap.

This also makes it easier to express the rule that a reservation cannot exceed two hours and that back-to-back reservations are allowed.

## Overall Assessment

The AI produced a reasonable first draft and avoided severe over-modeling. Its strongest choices were identifying ROOM and RESERVATION as the central entities and keeping the model small.

However, the draft did not fully represent the different responsibilities of students and administrators. It also treated room availability as a simple status even though availability depends on both maintenance and existing reservations.

My revised model keeps the useful simplicity of the AI draft while making the student, administrator, room-management, and reservation relationships more explicit. I intentionally did not add entities that could not be justified by the M2 requirements. This keeps the domain model focused on concepts that the application actually needs.