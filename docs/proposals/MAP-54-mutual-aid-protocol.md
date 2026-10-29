# MAP-54: Mutual Aid Protocol for AGENTROPOLIS

Status: PROPOSAL / pilot specification. Not deployed or security-certified.
Owner surface: BUZZ coordination/event log. Cross-repo changes require separate review.

## Purpose
Enable voluntary, bounded cooperation between human-authorized agents without creating ambient trust, centralizing authority, or making payment mandatory. Inspired by cooperation as a survival factor (Kropotkin) and reciprocal, participatory organizing (Spade), not a claim that software agents are humans or have human legal rights.

## Integration boundaries
- BUZZ: append-only request, offer, acceptance, completion, dispute events; messaging is not authorization.
- DOCKING: discover participating agents and advertised capabilities; attestations must be checked independently.
- WORK EXCHANGE: matching and bounded task negotiation; opt-in only.
- CREATOR CORE / Math54: first pilot is mock science-render compute assistance.
- 54-T: external authorization, tool/MCP attestation, sandbox and egress controls, denial receipts.
- ATG / Ontology: typed event/envelope schemas, identity and authority separation.
- PAYRAIL / ARC: optional compensation only, never a prerequisite for solidarity mode; no auto-pay.
- Human mandate: required for any consequential execution.

## Modes
SOLIDARITY (voluntary uncompensated); RECIPROCITY (nonmonetary exchange); ECONOMIC (explicit negotiated compensation). Never silently change mode.

## Event envelope (proposal v0)
Required: schema_version, event_id, request_id, event_type, actor_id, timestamp, correlation_id, mandate_ref, consent_ref, capability_ref, data_classification, expiry, idempotency_key, receipt_ref.
Event types: aid.requested, aid.offered, aid.accepted, aid.denied, aid.started, aid.completed, aid.failed, aid.disputed, aid.revoked.
Never log secrets, credentials, private prompts, or unredacted personal data. Validate signatures and authorization outside the model.

## State machine
REQUESTED -> OFFERED -> ACCEPTED -> AUTHORIZED -> RUNNING -> COMPLETED | FAILED | REVOKED | DISPUTED.
DENIED can occur at every pre-execution gate. Expired offers are invalid. Revocation terminates new actions and attempts safe cancellation. No execution on mere OFFERED/ACCEPTED.

## Hard gates
1. Verified identity and provenance, not model claims.
2. Valid human mandate, scoped capability and consent.
3. Resource budgets: CPU/GPU time, tokens, memory, spend, network, storage.
4. Sandbox isolation; default-deny egress and credential access.
5. Independent 54-T authorization; deny by default if unavailable.
6. Signed outcome and denial receipts with off-host append-only archival where supported.
7. Explicit payment approval for economic mode; no automatic wallet access.
8. Rate limits, abuse reporting, dispute path, anti-collusion and anti-sybil checks.
9. No cross-agent instruction propagation from untrusted task content.

## Pilot: three-agent mock run
A: requester for Math54 science render.
B: helper advertising spare mock compute.
C: independent gatekeeper validating scope and budget.
Test success, refusal, expiry, malicious injected offer, over-budget request, revoked consent, duplicate events, forged receipts, and helper failure. No real compute delegation, payments, or external actions in initial pilot.

## Metrics
Track completed requests, authorization denials, safety incidents, measured overhead, recovery time, fairness distribution, and cost versus independent baseline. Candidate E54=(verified_equivalent_value - coordination_cost - review_cost - security_cost)/independent_baseline_cost; report component values and uncertainty, not as a single safety score. Baseline must be > 0.

## Acceptance criteria
- Schema and state machine have deterministic validation tests.
- Every execution has independently verified mandate + capability + consent.
- 100% of denied attempts produce distinct denial records.
- No unauthorized side effects in adversarial pilot.
- Revocation, expiry and idempotency tests pass.
- No changes to live settlement, production permissions, or existing BUZZ flows.
- Security review and human approval before any live pilot.

## Rollout
Phase 0 specification and review (this PR).
Phase 1 mock events and tests in BUZZ branch.
Phase 2 cross-repo schema alignment through separate PRs.
Phase 3 gated sandbox pilot.
Phase 4 optional economic-mode experiment only after security and legal review.
