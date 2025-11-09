"""
Process the daily sales CSVs into a single processed CSV containing only Pink Morsel sales.
Produces: data/processed_sales.csv with columns: Sales,Date,Region
Assumptions:
 - product matching is case-insensitive and matches exactly 'pink morsel'
 - price values have a leading '$' (e.g. '$3.00')
"""
import csv
import glob
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PATTERN = os.path.join(DATA_DIR, 'daily_sales_data_*.csv')
OUT_PATH = os.path.join(DATA_DIR, 'processed_sales.csv')

rows_written = 0

with open(OUT_PATH, 'w', newline='', encoding='utf-8') as fout:
    writer = csv.writer(fout)
    writer.writerow(['Sales', 'Date', 'Region'])

    for path in sorted(glob.glob(PATTERN)):
        with open(path, newline='', encoding='utf-8') as fin:
            reader = csv.DictReader(fin)
            for row in reader:
                product = row.get('product', '').strip().lower()
                # Match 'pink morsel' case-insensitively
                if product != 'pink morsel':
                    continue

                price_raw = row.get('price', '').strip().replace('$', '').replace(',', '')
                qty_raw = row.get('quantity', '').strip()
                date = row.get('date', '').strip()
                region = row.get('region', '').strip()

                try:
                    price = float(price_raw)
                    qty = float(qty_raw)
                except Exception:
                    # Skip rows with invalid numeric data
                    continue

                sales = price * qty
                # Write sales with two decimal places
                writer.writerow([f"{sales:.2f}", date, region])
                rows_written += 1

print(f"Wrote {rows_written} rows to {OUT_PATH}")
