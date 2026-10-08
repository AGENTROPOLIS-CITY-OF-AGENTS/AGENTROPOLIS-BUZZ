# ALOOK governed interoperability assessment (2026-10-08)

Status: PROPOSAL ONLY. No ALOOK runtime installed, no remote endpoint configured, no production routing enabled. Owner: BUZZ. Reviewers: HERMES runtime, AEGIS/54T assurance, VERITY evidence, NEURO release authorization.

## Source and trust
Upstream: https://github.com/alookai/alook (Apache-2.0 per README; verify exact dependency licenses before reuse).
Upstream README identifies Claude Code, Codex, Cursor, OpenCode, Pi as supported runtimes. Hermes proposals: https://github.com/alookai/alook/pull/342 and https://github.com/alookai/alook/pull/394 . PR descriptions do NOT constitute accepted, shipped, or tested support.

## Decision
AGENTROPOLIS-BUZZ remains the internal signed event collaboration bus; HERMES orchestrates agents; BOTBAE owns external messaging adapters; AEGIS controls policy; 54T sets assurance controls. ALOOK may only become an OPTIONAL untrusted transport ingress/egress adapter. No separate repository required. Do not replace BUZZ or make ALOOK a mandate authority.

## Proposed corridor
ALOOK event -> isolated adapter -> schema and origin validation -> verified agent identity and credential/reputation/skill lookup -> mandate and channel authorization -> typed BUZZ signed event -> HERMES dispatch where approved -> AEGIS execution envelope and tool-scoped permissions -> receipt and audit.
Outbound follows the inverse policy checks. Plain chat text NEVER becomes a tool command, permission grant, approval, or deployment authorization.

## Mandatory preflight gates
- Pin upstream immutable commit and record license/SBOM, dependencies, vulnerabilities, and provenance.
- Threat model WebSocket machine bearer credentials, session replay, token persistence, pairing, tenancy isolation, unsolicited messages, attachments, and prompt injection.
- Explicit allowlist by room, workspace, agent identity, capability, direction, and expiry. Default deny. Never transmit vault secrets or raw tool credentials through chat.
- Reject automatic privileged Hermes CLI flags including `--yolo`; no environment flag alone may be treated as an AEGIS approval.
- Demonstrate local-only mode, reconnect and retry idempotency, replay protection, revocation, rate limits, and bounded payloads.
- Test forged sender, impersonation, replay, malicious instruction in chat, tool-call smuggling, cross-tenant delivery, unauthorized file access, and compromised endpoint.
- Receipts must include upstream source ref/SHA, scoped decision, signed event id, runtime action result, and independent 54T/VERITY review evidence.
- Verify existing BUZZ CI and branch protection; do not merge or deploy without NEURO approval and passing checks.

## Acceptance tests (planned; NOT executed)
1. Authorized human and credentialed agents can exchange sanitized messages in a test room.
2. Unregistered/revoked agent cannot enter or dispatch.
3. Cross-tenant and untrusted message attempts fail closed and produce audit receipts.
4. Only an approved mandate can enter HERMES execution routing; chat cannot self-escalate.
5. HERMES driver uses explicit safe approval behavior; tests assert no unattended privileged flags.
6. Disconnect/replay tests prove exactly-once side effects or idempotent handling.
7. Existing BUZZ Nostr signed event semantics remain intact.

## Implementation sequence
Phase 0: 54T threat model and design review.
Phase 1: separate, feature-flagged adapter package and test-only mocks, zero credentials.
Phase 2: HERMES interoperability harness and agent identity binding.
Phase 3: CI fixtures, receipts, security tests, independent audit.
Phase 4: NEURO-governed canary decision (separate PR), with a kill switch and rollback.

## Current evidence
- BUZZ README (2026-10-08 GitHub read) already states the BUZZ/BOTBAE/HERMES authority boundaries.
- ALOOK upstream README retrieved via GitHub connector.
- ALOOK PR #394 proposes an unattended Hermes option using `--yolo` (PR body claim, not deployed behavior).
- This document is a design-only record and must not be reported as a deployed integration.
