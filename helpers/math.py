def sum_value(a, b):
    # Check if variables are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Only numbers are allowed')
    return a + b
