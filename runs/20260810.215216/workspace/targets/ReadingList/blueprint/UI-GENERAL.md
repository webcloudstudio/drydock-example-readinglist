# UI-GENERAL: Reading List Interface

| Field       | Value |
|-------------|-------|
| Version     | 20260810 V1 |
| Description | Defines shared interaction patterns for the reading-list interface. |
| Depends On  | ARCHITECTURE.md |
| Provides    | shared reading-list UI patterns |
| Consumes    | — |

## Page Structure

The reading-list interface uses a clear page heading, an add-book form, a list region, and action controls.

The add form contains labeled title and author fields and a submit control. Each displayed book includes its title, author, and a remove control.

## Empty State

When no books exist, the list region communicates that the reading list is empty while keeping the add form available.

## Validation Presentation

Validation failures appear near the add form as clear user-facing feedback. The entered values remain available for correction when practical.

## List Presentation

Books appear in insertion order. Each book has an independently usable remove control.

## Programmatic Acceptance

- None. Shared presentation guidance has no independent programmatic interface; screen and feature specifications cover its executable behavior.

## User Acceptance

- A reader can add, view, and remove books without instructions.
- The empty state makes the next available action clear.

## Guardrails

- The add form labels both title and author inputs.
- Remove controls identify the book they affect.
- Validation feedback is visible without requiring external instructions.
