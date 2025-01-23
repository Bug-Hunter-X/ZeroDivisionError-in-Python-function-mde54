def function_with_uncommon_error(x, y):
    try:
        if x == 0:
            return float('inf')  # Or raise a more descriptive exception
        return x + y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None # Or handle the error in a more appropriate manner