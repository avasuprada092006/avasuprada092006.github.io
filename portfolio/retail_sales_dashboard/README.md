# Retail Revenue & Margin Explorer

An original portfolio project that uses Python, SQL and a dependency-free interactive HTML dashboard to explore retail order performance.

## Open the demo

Open `index.html` in a modern browser. The dashboard works offline and supports region and category filters.

## Rebuild the sample

Run `python generate_project.py` from this folder to recreate the CSV and summary using a fixed random seed. The included dashboard is a prebuilt, offline view of this sample.

## Data and limits

The 720 order lines are generated synthetic data. They are not real company transactions, and the sales patterns are not market estimates. The data is intended to demonstrate joins/aggregation concepts, margin calculations, filtering, and basic validation.

## Files

- `orders.csv`: generated order-line data, INR amounts
- `queries.sql`: schema, monthly/category analysis, and a consistency check
- `metrics.json`: calculated sample summary
- `generate_project.py`: reproducible generator and analysis logic
- `index.html`: interactive offline dashboard
