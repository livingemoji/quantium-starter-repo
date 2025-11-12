# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## Processed data output

A processed CSV containing only Pink Morsel sales has been generated at `data/processed_sales.csv`.

This file contains three columns: `Sales`, `Date`, and `Region`.

To regenerate it, run the processing script from the repository root:

```
python scripts/process_sales.py
```

The script filters for product == "pink morsel" (case-insensitive), computes sales as price * quantity, and writes the combined output.

## Data Visualization

A Dash web application (`app.py`) is available to visualize the Pink Morsel sales data and answer the key business question: **Were sales higher before or after the price increase on January 15, 2021?**

### Running the visualization:

From the repository root, install dependencies (if not already installed):

```
pip install -r requirements.txt
```

Then start the Dash app:

```
python app.py
```

The app will start on `http://127.0.0.1:8050/` and display an interactive line chart showing:
- Daily total sales of Pink Morsels across all regions over time
- A marked indicator for the price increase date (January 15, 2021)
- Hover tooltips to inspect individual daily sales values

### Key Insight

The visualization clearly shows the impact of the price increase—there is a visible jump in total daily sales starting on January 15, 2021, indicating that despite higher prices, revenue increased.
