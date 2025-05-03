def process_numbers(*args, **kwargs):
    """
    Helper function to process inputs and validate them.

    Returns:
    a tuple of numbers and a dictionary of operations.
    
    Raises:
    TypeError or valueError for invalid inputs.
    """
    try:
        numbers = [] # list to store numbers
        for arg in args:
            if isinstance(arg, (int, float)):
                numbers.append(arg)
            else:
                raise TypeError(f"Invalid argument: {arg}. All arguments must be numbers.")
            
        for key, value in kwargs.items(): # iterate through keyword arguments
            if key not in ['add', 'subtract', 'multiply', 'divide'] or not isinstance(value, bool): # check if the key is valid and value is boolean
                raise ValueError(f"Invalid operation: {key}. Must be one of ['add', 'subtract', 'multiply', 'divide'].")
        
        return numbers
    
    except TypeError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: {e}"
    


def calculate(*args, **kwargs): # perform arithmetic operations
    """
    This function performs basic arithmetic operations on given numbers.
    
    positional arguments:
    *args: numbers to be used in the calculation(int or float)

    Keyword arguments (coose among the following):
    add: bool, if True,  adds all numbers 
    subtract: bool, if True, subtracts in order of the numbers given
    multiply: bool, if True, multiplies all numbers
    divide: bool, if True, divides in order of the numbers given

    Returns:
    Dictionary with the results of the operations performed or error message.

    Raises:
    TypeError: If any of the arguments is not a number.
    ValueError: If no valid operation is specified.

"""
    try:
        numbers= process_numbers(*args, **kwargs) # call the helper function to process inputs
        if isinstance(numbers, str): # check if the helper function returned an error message
            return numbers # return the error message

    
        results = {}
        if kwargs.get('add'):
            results['add'] = sum(numbers)

        if kwargs.get('subtract'):
            
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            results['subtract'] = result

        if kwargs.get('multiply'):
            result = 1
            for num in numbers:
                result *= num
            results['multiply'] = result

        if kwargs.get('divide'):
            try:
                result = numbers[0]
                for num in numbers[1:]:
                    result /= num
                results['divide'] = result

            except ZeroDivisionError:
                return "Error: Division by zero is not allowed."
            
        if not results:
            raise ValueError("No valid operation specified. Please choose at least one operation.")
        return results
    
    except TypeError as e:
        return f"Error: {e}" # return eror message if any of the arguments is not a number
    

variable1 = calculate(10, 5, 2, add=True)
print(variable1) 
variable2 = calculate(10, 5, 2, add=True, subtract=True, multiply=True, divide=True)
print(variable2)
variable3 = calculate(10, "x", 2, add=True)
print(variable3) 

    