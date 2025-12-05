def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to float (handles non-numeric input)
        num = float(numerator)
        denom = float(denominator)
        
        # Try to perform division (handles division by zero)
        result = num / denom
        return f"The result of the division is {result}"
        
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."