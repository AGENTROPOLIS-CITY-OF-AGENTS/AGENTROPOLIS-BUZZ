# BUZZ Agentropolis Integration

## Canonical role

Within Agentropolis, BUZZ is the internal collaboration bus and signed workspace substrate connecting humans, agents, workflows, projects, and governed communication events.

BUZZ is not the owner control plane and is not the multi-platform edge gateway.

> NEURO = command authority.
> BOTBAE = communications edge.
> BUZZ = internal collaboration bus.
> HERMES = orchestration.

## Integration boundary

```text
Discord / Telegram / WhatsApp / Slack
                  |
                BOTBAE
                  |
                  v
                BUZZ
                  |
                  v
               HERMES
          /       |       \
       DEVIN    VERITY   GROK BOT
```

BOTBAE converts platform-specific messages into normalized events.
BUZZ carries collaboration state, channels, threads, DMs, workflow events, search context, and audit-visible communication.
HERMES coordinates agent work.
NEURO remains the human authority plane.

## What BUZZ owns

- collaborative channels and threads
- DMs and workspace membership
- signed event transport
- workflow and project events
- agent-visible conversation state
- search and retrieval across workspace history
- collaboration receipts and audit context
- agent participation inside governed rooms

## What BUZZ does not own

- Discord, Telegram, WhatsApp, or Slack credentials
- platform-specific webhook logic
- owner approval policy
- worker-agent code
- high-risk execution authority

## Message rule

BUZZ events can carry intent, evidence, requests, approvals, denials, and receipts.

They do not silently convert conversational intent into production authority.

Where an action has consequences outside the collaboration substrate, the request must resolve through the Agentropolis execution corridor:

```text
Identity
  -> Mandate
  -> Policy
  -> Tool Permission
  -> Execution Envelope
  -> Execute
  -> Receipt
  -> Audit
```

## Agent roles

- **HERMES** coordinates and delegates.
- **DEVIN** performs governed engineering work.
- **VERITY** independently validates evidence and results.
- **GROK BOT** contributes divergent, creative, or exploratory reasoning without inheriting authority.
- **AEGIS** evaluates policy and risk.
- **54T** provides assurance and validation controls.

## Canonical statement

**BUZZ is where the Agentropolis society collaborates. BOTBAE gets messages into and out of that society. NEURO decides the human authority boundaries under which it operates.**
