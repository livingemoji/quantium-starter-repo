#!/bin/bash

# Pink Morsel Sales Dashboard - CI Test Script
# This script is designed to be run by CI/CD systems to validate the application
# 
# Functionality:
# - Activates the project virtual environment
# - Runs the test suite with pytest
# - Returns exit code 0 on success, 1 on failure
#
# Usage: bash run_tests.sh

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script directory (where this script is located)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo -e "${YELLOW}================================${NC}"
echo -e "${YELLOW}Pink Morsel Sales Dashboard - CI${NC}"
echo -e "${YELLOW}================================${NC}"
echo ""

# Step 1: Check if virtual environment exists
echo -e "${YELLOW}Step 1: Checking virtual environment...${NC}"
if [ ! -d "$SCRIPT_DIR/.venv" ]; then
    echo -e "${RED}X Virtual environment not found at $SCRIPT_DIR/.venv${NC}"
    echo "Please create a virtual environment first:"
    echo "  python -m venv .venv"
    exit 1
fi
echo -e "${GREEN}✓ Virtual environment found${NC}"
echo ""

# Step 2: Activate virtual environment
echo -e "${YELLOW}Step 2: Activating virtual environment...${NC}"
# For bash/shell, source the activation script
source "$SCRIPT_DIR/.venv/bin/activate" || {
    echo -e "${RED}X Failed to activate virtual environment${NC}"
    exit 1
}
echo -e "${GREEN}✓ Virtual environment activated${NC}"
echo "  Python: $(python --version)"
echo "  Pip: $(pip --version)"
echo ""

# Step 3: Verify dependencies are installed
echo -e "${YELLOW}Step 3: Verifying dependencies...${NC}"
if ! python -c "import pandas; import dash; import plotly; import pytest" 2>/dev/null; then
    echo -e "${YELLOW}⚠ Some dependencies are missing, attempting to install...${NC}"
    pip install -q -r "$SCRIPT_DIR/requirements.txt"
    echo -e "${GREEN}✓ Dependencies installed${NC}"
else
    echo -e "${GREEN}✓ All dependencies are installed${NC}"
fi
echo ""

# Step 4: Run the test suite
echo -e "${YELLOW}Step 4: Running test suite...${NC}"
echo ""

cd "$SCRIPT_DIR"

# Run pytest with verbose output and capture the exit code
if python -m pytest test_app.py -v --tb=short; then
    TEST_RESULT=0
    echo ""
    echo -e "${GREEN}✓ All tests passed!${NC}"
else
    TEST_RESULT=1
    echo ""
    echo -e "${RED}X Some tests failed!${NC}"
fi

echo ""
echo -e "${YELLOW}================================${NC}"

# Step 5: Print summary
if [ $TEST_RESULT -eq 0 ]; then
    echo -e "${GREEN}✓ CI BUILD SUCCESSFUL${NC}"
    echo -e "${YELLOW}================================${NC}"
    exit 0
else
    echo -e "${RED}✗ CI BUILD FAILED${NC}"
    echo -e "${YELLOW}================================${NC}"
    exit 1
fi
