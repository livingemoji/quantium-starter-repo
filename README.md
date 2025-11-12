# Quantium starter repo
This repo contains everything you need to get started on the program! Good luck!

## Processed data output

A processed CSV containing only Pink Morsel sales has been generated at `data/processed_sales.csv`.

This file contains three columns: `Sales`, `Date`, and `Region`.

To regenerate it, run the processing script from the repository root:

```
python scripts\\process_sales.py
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

### Features

The dashboard includes:
- **Interactive line chart** showing daily sales trends with fill area visualization
- **Region filter** with radio buttons to view sales by region (North, South, East, West) or all regions combined
- **Price increase marker** - a red dashed line highlighting the price change date (January 15, 2021)
- **Dynamic coloring** - each region has its own color for easy visual distinction
- **Hover tooltips** - view exact sales values for any date by hovering over the chart
- **Professional styling** with gradient backgrounds, shadows, and responsive design

### Region Filtering

Use the radio button filter at the top of the dashboard to switch between:
- **All** - Combined sales from all regions
- **North** - Northern region sales only
- **South** - Southern region sales only
- **East** - Eastern region sales only
- **West** - Western region sales only

The chart updates instantly when you change the selection, maintaining the price increase marker for reference.

### Key Insight

The visualization clearly shows the impact of the price increase—there is a visible and sustained jump in daily sales starting on January 15, 2021. This indicates that despite the higher prices, total revenue increased significantly.

````
