# BUZZ Representation + Continuity Events

Status: proposed event contract
Date: 2026-09-15

BUZZ carries signed lifecycle facts; conversation is not authoritative state.

## Event family

- `representation.selected`
- `representation.transform.started`
- `representation.transform.completed`
- `representation.transform.failed`
- `representation.checkpoint.created`
- `continuity.asserted`
- `continuity.rejected`
- `lineage.forked`
- `context.rehydrated`
- `context.entropy.high`
- `fleet.topology.selected`
- `fleet.topology.changed`

## Minimum envelope

```json
{
  "event_id": "...",
  "event_type": "representation.changed",
  "subject_id": "...",
  "fleet_run_id": null,
  "execution_cell_id": null,
  "source_representation": "...",
  "target_representation": "...",
  "preserved_invariants": [],
  "declared_distortion": null,
  "continuity_claim": null,
  "authority_ref": "...",
  "receipt_ref": "...",
  "provenance_ref": "...",
  "occurred_at": "..."
}
```

## Rules

1. Events report state transitions; they do not grant authority.
2. `continuity.asserted` requires a continuity evidence/receipt reference for material migrations.
3. `representation.changed` must not conceal a lineage fork.
4. BUZZ clients may render events conversationally, spatially, or as dashboards without changing event semantics.
