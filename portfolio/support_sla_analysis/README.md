# Support Ticket SLA Quality Monitor

An original portfolio project that uses Python, SQL and a dependency-free interactive HTML dashboard to examine service operations.

## Open the demo

Open `index.html` in a modern browser. The dashboard works offline and supports priority and category filters.

## Rebuild the sample

Run `python generate_project.py` from this folder to recreate the CSV and summary using a fixed random seed. The included dashboard is a prebuilt, offline view of this sample.

## Data and limits

The 480 tickets are synthetic. The example SLA targets (High: 8h, Medium: 24h, Low: 48h) are illustrative and do not represent a real organization's policy. Ratings and resolution times are generated for practice, not business conclusions.

## Files

- `tickets.csv`: generated ticket data
- `queries.sql`: schema, SLA summaries, and a consistency check
- `metrics.json`: calculated sample summary
- `generate_project.py`: reproducible generator and analysis logic
- `index.html`: interactive offline dashboard
