# Python Calculator 🧮

A simple calculator program written in Python that performs basic operations: addition, subtraction, multiplication, and division.

## Features
- CLI input for numbers and operations
- Handles division by zero gracefully
- Unit tested using `pytest`
- Added unit testing for addition function


### Run the Calculator and Pytest
```bash
# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

#Run the python calculator
python3 calculator.py

#Run the test
pytest test_calculator.py
