
# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."

    try:
        # Perform the division
        result = numerator / denominator
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
