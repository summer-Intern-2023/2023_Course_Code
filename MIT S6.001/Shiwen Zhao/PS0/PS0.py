def calculate_power_and_square_root(x, y): 
    """ 
    Calculates the power of x to the y and the square root of x. 
    Args: 
        x (int): The base number. 
        y (int): The exponent. 
        
    Returns: 
        tuple: A tuple containing the calculated power and square root. 
    """ 
    power = x ** y 
    square_root = int(x ** 0.5) 
    return power, square_root