# Social Economic Events on BUZZ

BUZZ transports signed lifecycle events for economic intent and settlement. It does not authorize or execute payments.

## Event families

- `social.economic.intent.created`
- `social.economic.intent.authorized`
- `social.economic.intent.refused`
- `settlement.submitted`
- `settlement.pending`
- `settlement.settled`
- `settlement.failed`
- `settlement.cancelled`
- `settlement.reconciled`
- `settlement.correction`

## Required fields

Every event MUST carry:

```text
event_id
schema_version
event_type
occurred_at
producer
principal_id
intent_id
execution_envelope_id?
receipt_id?
correlation_id
causation_id?
provenance[]
```

Value-bearing details SHOULD use normalized references rather than secrets or private wallet material.

## Ordering and replay

- Events are append-only facts, not mutable account state.
- Consumers MUST de-duplicate by `event_id` and domain idempotency key where applicable.
- A `settlement.submitted` event MUST NOT be interpreted as `settlement.settled`.
- Correction events reference prior events instead of deleting history.
- Replayed events MUST NOT duplicate transfers, rewards, ownership mutations, XP, or campaign attribution.

## Domain authority

BUZZ may announce that settlement occurred, but SOCIALS, GAME, CREATOR CORE, and other owning systems decide how a validated receipt changes their domain state.

## Failure isolation

If settlement infrastructure is unavailable, BUZZ still carries social/game/creator activity and may carry `pending` or `failed` economic lifecycle events. Payment failure cannot become workspace or social-network failure.
