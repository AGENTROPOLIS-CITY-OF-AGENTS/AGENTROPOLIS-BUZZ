# BUZZ as the AGENTROPOLIS Life Plane Event Fabric

BUZZ is the preferred signed collaboration/event substrate for AGENTROPOLIS Life Plane events involving humans, agents, workflows, rooms, approvals, git activity, project coordination, and persistent presence.

## Boundary

BUZZ is a nervous system, not an authority root.

It may transport and index events, but it does not independently grant mandates, permissions, identity authority, policy overrides, receipt authority, or canonical world-state authority.

## Event flow

```text
source system
  -> Life Plane adapter
  -> normalized CityEvent
  -> policy/visibility filter
  -> BUZZ event mapping where appropriate
  -> room/channel/workflow/search/audit surfaces
```

Not every infrastructure metric belongs in BUZZ. High-volume telemetry should remain in its proper observability system unless a summarized or actionable event is needed by humans/agents/workflows.

## Initial mapped classes

Recommended Life Plane classes for BUZZ integration:

- `agent.presence.changed`
- `agent.message`
- `mandate.created`
- `mandate.updated`
- `mandate.revoked`
- `task.created`
- `task.transitioned`
- `receipt.emitted`
- `audit.finding`
- `security.signal`
- `human.approval`
- `human.pause`
- `human.revoke`
- selected `district.state.changed`
- selected `world.projection.changed`

## Required metadata

Mapped events should retain, directly or by reference:

- Life Plane event id
- source identity/system
- timestamp
- district/institution context
- correlation id
- provenance
- mandate reference when applicable
- execution-envelope reference when applicable
- receipt or denial reference when terminal
- visibility classification

## Presence law

BUZZ presence can indicate that an agent is reachable, active, degraded, paused, or unavailable. Presence must never be interpreted as execution permission.

## Safety

- Fail closed on unknown visibility classes.
- Never publish secrets or private payloads to public communities.
- Preserve tenant/community boundaries.
- Keep agent identities distinct from human identities.
- Preserve signed-event provenance wherever the underlying event supports it.
