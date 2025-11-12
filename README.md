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

## Testing

A comprehensive test suite (`test_app.py`) ensures the Dash app functions correctly and contains all expected components. The tests use pytest and the Dash testing framework.

### Test Coverage

The test suite includes 4 tests organized into two test classes:

#### `TestDashAppComponents` - Component Presence Tests
1. **test_header_is_present** - Verifies the header with title "Pink Morsel Sales Dashboard" is present
2. **test_visualization_is_present** - Confirms the dcc.Graph component (chart visualization) exists
3. **test_region_picker_is_present** - Validates the dcc.RadioItems component for region filtering is present with all 5 options (All, North, South, East, West)

#### `TestDashAppCallbacks` - Functionality Tests
4. **test_sales_chart_callback_exists** - Ensures the callback function for chart updates is properly defined

### Running the Tests

From the repository root, execute the test suite:

```
python -m pytest test_app.py -v
```

The `-v` flag provides verbose output showing each test name and result.

### Expected Output

```
test_app.py::TestDashAppComponents::test_header_is_present PASSED
test_app.py::TestDashAppComponents::test_visualization_is_present PASSED
test_app.py::TestDashAppComponents::test_region_picker_is_present PASSED
test_app.py::TestDashAppCallbacks::test_sales_chart_callback_exists PASSED

====== 4 passed in X.XXs ======
```

All tests should pass, confirming the dashboard is working as expected.

## Continuous Integration

To support continuous integration (CI/CD) pipelines, automated test scripts are provided that activate the virtual environment and run the test suite with proper exit code handling.

### CI Test Scripts

Two scripts are provided to support different environments:

- **`run_tests.bat`** — Windows batch script for CI/CD systems (GitHub Actions, Azure Pipelines, etc.)
- **`run_tests.sh`** — Bash script for Unix/Linux/macOS CI/CD systems

Both scripts perform the same steps:
1. Verify the virtual environment exists at `.venv`
2. Activate the virtual environment
3. Verify all dependencies are installed
4. Run the test suite with pytest
5. Return exit code 0 on success or 1 on failure

### Using the CI Scripts Locally

To run tests locally using the CI script:

**Windows:**
```
.\run_tests.bat
```

**Unix/Linux/macOS:**
```
bash run_tests.sh
```

### Integrating with CI/CD Systems

The scripts are designed to integrate seamlessly with popular CI/CD platforms:

#### GitHub Actions Example
```yaml
name: Run Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Create venv
        run: python -m venv .venv
      - name: Run tests
        run: .\run_tests.bat
```

#### Expected Output
```
================================
Pink Morsel Sales Dashboard - CI
================================

Step 1: Checking virtual environment...
[OK] Virtual environment found

Step 2: Activating virtual environment...
[OK] Virtual environment activated

Step 3: Verifying dependencies...
[OK] All dependencies are installed

Step 4: Running test suite...
[all 4 tests PASS]

[SUCCESS] CI BUILD SUCCESSFUL
```

### Exit Codes

- **Exit code 0** — All tests passed, build successful
- **Exit code 1** — One or more tests failed, build failed

This allows CI/CD systems to automatically detect build status and take appropriate actions (e.g., block merges, notify developers, trigger deployments).

````
