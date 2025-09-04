# create the 2 numbers divid program 
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b