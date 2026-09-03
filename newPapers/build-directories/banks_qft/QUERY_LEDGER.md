# Query ledger

No unresolved readings.

`query-ledger.json` is the machine-readable ledger. It is empty while every
reading is closed; any entry must carry `status: closed` before release.

Each query must name its owner, physical PDF page, printed page, source marker,
candidate readings, and the image check needed for closure.
