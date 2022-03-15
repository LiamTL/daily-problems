# Your task is to create a function that does four basic mathematical operations.

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    
    elif operator == "-":
        return value1 - value2
    
    elif operator == "*":
        return value1 * value2
    
    elif operator == "/":
        return value1 / value2
    
    elif operator == "//":
        return value1 // value2
    
    elif operator == "**":
        return value1 ** value2