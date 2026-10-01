# AI Elicitation Audit Log

## Project
Campus Study Room Reservation System

## AI Tool Used
ChatGPT

## Purpose of the Audit

The purpose of this audit is to compare the requirements I developed for the Campus Study Room Reservation System with requirements independently suggested by an AI tool. I evaluated what the AI missed, what it added without being requested, and what useful ideas it identified that I had not originally considered.

## What the AI Missed

One important issue the AI did not focus on was the exact behavior of scheduling conflicts. My original requirements specifically state that overlapping reservations for the same room must be rejected while back-to-back reservations are allowed. This distinction is important because simply saying that the system should prevent double bookings does not completely define how reservation boundaries should behave.

The AI also did not clearly address what should happen if a room becomes unavailable while a student is in the process of making a reservation. My requirements specify that availability must be checked before the reservation is confirmed and that the student should receive an error if the room is no longer available.

Another detail that was not emphasized was preserving canceled reservations instead of permanently deleting them. My original requirements specify that canceled reservations should be marked as canceled. Keeping this information could be useful for maintaining reservation history and troubleshooting disputes.

## What the AI Invented

The AI introduced several requirements that were never part of my original project concept.

First, it introduced a check-in and check-out system using QR codes or geolocation. My original system only required students to reserve, view, and cancel study rooms. I never specified that students would have to physically verify that they arrived.

The AI also created an automatic no-show policy that releases a room if the student does not check in within 15 minutes. This could be useful, but the 15-minute rule was created by the AI rather than being based on one of my requirements.

Another invention was a daily and weekly booking quota. The AI suggested a default limit of two hours per day and eight hours per week. My original requirements only established a two-hour maximum for an individual reservation and did not establish a weekly reservation limit.

The AI also introduced group reservations and invitations using university email addresses. This was not part of my original project scope.

The AI added administrative usage reports for statistics such as peak hours, popular buildings, no-show rates, and room utilization. Although these reports could benefit administrators, analytics were not included in my original requirements.

Finally, the AI introduced technical implementation requirements such as university SSO, OAuth2/SAML/CAS, TLS 1.3, AES-256 encryption, database backup targets, and specific mobile viewport sizes. These may be reasonable engineering choices, but they were not requirements that I originally gave the AI. Some of them also move from describing what the system must accomplish into prescribing specific implementation technologies.

## What the AI Got Right

The AI identified some useful issues that I had not originally considered.

Accessibility was one of the strongest additions. Requiring the interface to meet WCAG 2.1 Level AA would make the application more usable for students with disabilities. This is something I did not include in my original requirements but would consider adding in a future revision.

The AI also identified the importance of simultaneous booking attempts. My requirements prevent overlapping reservations, but the AI went further by considering what happens when two students attempt to reserve the same room at nearly the same time. This is an important edge case because the system must ensure that only one reservation succeeds.

Another useful suggestion was allowing administrators to cancel reservations when a room unexpectedly becomes unavailable. My original requirements allowed administrators to mark rooms unavailable, but I did not completely define what should happen to an existing reservation if a room is closed for maintenance or another emergency.

## Overall Judgment

The AI produced several useful ideas and identified edge cases that I had not considered, especially accessibility, simultaneous booking attempts, and administrative overrides. However, its output should not be accepted directly as the final requirements specification.

The biggest issue was that the AI frequently turned assumptions into requirements. Features such as geolocation check-in, QR codes, weekly booking limits, group invitations, SSO protocols, analytics, and specific encryption technologies were introduced without first asking whether they belonged in the project scope.

This demonstrates why AI-generated requirements still require human review. The AI was useful for discovering possible missing cases, but the project owner still needs to determine which requirements reflect the actual needs and scope of the system.