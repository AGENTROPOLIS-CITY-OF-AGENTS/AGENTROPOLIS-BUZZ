# Hermes <-> BUZZ Interoperability

BUZZ is the AGENTROPOLIS collaboration substrate. Hermes Bot Mode, group chat, mentions, peer/A2A, cron delivery, and Collective Wisdom are runtime-facing transports/surfaces beneath BUZZ governance.

## Inbound normalization
Every Hermes-originated event entering BUZZ preserves an immutable origin envelope: citizen/profile, canonical runtime address, source message/session, parent/alternate identity where present, correlation/delegation/occurrence IDs, and transport provenance.

A separately redacted AEGIS projection may be supplied to model context. Never mutate canonical provenance to perform privacy redaction.

## Authority
A peer message, mention, group membership, room leadership, delivery destination, or replicated runtime fact is not an authorization grant. BUZZ routes the request to Dispatch; Mandate + AEGIS resolve authority independently.

## Continuity
Delivery destination and continuity ownership are separate. Preserve delivery_provenance (origin|home|broadcast) and continuation_session_ref. Broadcast delivery never silently creates continuation authority.

## Authority transfer
Hosted-room/runtime leadership changes require AGENTROPOLIS fencing above transport: authority_lease_id, monotonic fence_token, previous/new authority, and revocation evidence. Replicated runtime state is recovery evidence, not automatic failover authority.

## Collective Wisdom
Wisdom candidate-skill events may travel over BUZZ for review and coordination, but canonical skill state lives in the Skill Registry and promotion requires assurance.

## Do not duplicate
BUZZ does not reimplement Hermes peer/A2A transport, group-chat routing, cron delivery, or runtime notification UX.