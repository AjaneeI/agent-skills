# Frozen-run preflight

- Explicit authorization, authorized attempts, and remaining allowance verified
- Immutable commit/model/data/scorer/tool context recorded
- Local service credentials and permission scope checked without leaking values
- No held-out data in development workspace
- Retry / timeout / fallback behavior matches protocol
- Data capture, timestamp and fingerprint directories exist
- Stop conditions and failure handling confirmed
- On completion: preserve exact result, report whether unscored, never auto-retry
