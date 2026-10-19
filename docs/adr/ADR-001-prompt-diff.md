# ADR-001 Prompt-and-Diff Log

## Project

Campus Study Room Reservation System

## Architectural Decision

Use separate `STUDENT` and `ADMINISTRATOR` domain entities instead of one `USER` entity with a role attribute.

## AI Tool Used

ChatGPT

## Prompt Submitted

I am developing a Campus Study Room Reservation System. During domain modeling, I considered whether students and administrators should be represented by one USER entity with a role attribute or by separate STUDENT and ADMINISTRATOR entities.

I chose separate STUDENT and ADMINISTRATOR entities because students and administrators currently have different responsibilities and relationships in the system. Students make and cancel reservations, while administrators manage study rooms and can mark rooms unavailable.

Please draft ADR-001 for this architectural decision. Include these sections: Context, Decision, Alternatives Considered, and Consequences. The consequences must include both benefits and what becomes harder because of this decision. Include at least two genuine alternatives that could reasonably have been selected.

## AI-Generated Output Summary

ChatGPT generated an initial ADR recommending separate STUDENT and ADMINISTRATOR entities.

The draft included the required sections and discussed two alternatives: a single USER entity with a role attribute, and a more complex role-based access control model.

It also identified trade-offs involving authentication, shared account management, and future role changes.

## Changes Made After Reviewing the AI Draft

### 1. Removed Unsupported Administrator Features

**AI draft:** Included administrators setting operating hours, overriding bookings, maintaining audit logs, and managing study room clusters.

**Final ADR:** Limited administrator responsibilities to adding and updating rooms and marking rooms unavailable for maintenance.

**Reason:** The additional features were not established by the M2 requirements.

### 2. Removed Unnecessary Implementation Assumptions

**AI draft:** Suggested shared traits, composition, or base authentication profiles.

**Final ADR:** Described authentication complexity as a consequence without selecting a specific implementation.

**Reason:** The project has not yet made those implementation decisions.

### 3. Removed Unsupported Type-Safety Claims

**AI draft:** Claimed that compile-time type checking would prevent students from accessing administrator functionality.

**Final ADR:** Focused on clearer domain relationships instead.

**Reason:** Separate domain entities do not automatically enforce authorization or guarantee compile-time protection.

### 4. Simplified the Alternatives

**AI draft:** Discussed a single USER table with nullable role-specific columns and a dynamic RBAC permission graph.

**Final ADR:** Kept both alternatives but explained their trade-offs in terms of the current project requirements.

**Reason:** A single USER entity does not necessarily require many nullable fields, and the system does not currently require dynamic permissions.

### 5. Strengthened the Negative Consequences

**AI draft:** Identified authentication and role changes as difficulties.

**Final ADR:** Made the consequences more explicit by discussing multiple roles, duplicated user information, role transitions, and future extensibility.

**Reason:** The assignment specifically requires explaining what becomes harder because of the decision.

## Accepted AI Suggestions

- Use the four required ADR sections.
- Explain why the architectural decision was necessary.
- Compare the separate-entity design against a unified USER model.
- Consider a flexible role-and-permission model as an alternative.
- Document both benefits and drawbacks.

## Rejected or Revised AI Suggestions

- Administrator features not present in the requirements.
- Assumptions about authentication implementation.
- Claims that separate entities automatically provide compile-time authorization safety.
- Speculative future attributes unrelated to the current application.

## Final Assessment

The AI draft provided a useful structure and identified genuine alternatives. However, several claims extended beyond the project's documented requirements.

The final ADR was revised to reflect the actual M3 domain-model decision and to explain the costs of maintaining separate STUDENT and ADMINISTRATOR entities.

The architectural decision remained the same, but the reasoning and consequences were made more specific to the Campus Study Room Reservation System.
