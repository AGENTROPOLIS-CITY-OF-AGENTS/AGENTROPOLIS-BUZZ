# BUZZ Connector Event Boundary

BUZZ may carry connector lifecycle, account-state, capability, review, and workflow events.

## Non-authority rule
A BUZZ event may inform state, but does not itself authorize a connector action.

Canonical path:
event -> reconcile/resolve current state -> AEGIS/Dispatch decision -> execution -> receipt

## Useful events
- connector connected/disconnected
- policy revision changed
- host capability changed
- app liveness changed
- route ownership changed
- skill/plugin admission changed

All consequential actions still require current mandate and policy evaluation.
