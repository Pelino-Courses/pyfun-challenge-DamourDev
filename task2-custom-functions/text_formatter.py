def format_text(text: str, prefix: str = "", suffix: str = "", capitalize: bool = False, max_length: int = None) -> str: 
    """
    The function which format the input text with optional prefix, suffix, capitalization, and maximum length.

    Args:
        text (str): The input text to format.
        prefix (str): The prefix to add to the text. Default is an empty string.
        suffix (str): The suffix to add to the text. Default is an empty string.
        capitalize (bool): Whether to capitalize the first letter of the text. Default is False.
        max_length (int): The maximum length of the formatted text. If None, no limit is applied.

    Returns:
        str: The function returns formatted text.
    

    Raises:
        TypeError: If the input text , prefix, or suffix is not a string and max_length is not an integer.
        ValueError: If max_length is not none and  the max_length is less than 0.
        
    """

    try:

        if not isinstance(text, str): # check if text is a string
            raise TypeError("text must be a string") 
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")
        if not isinstance(suffix, str):
            raise TypeError("suffix must be a string")
        if not isinstance(capitalize, bool):
            raise TypeError("capitalize must be a boolean")
        
        if max_length is not None:
            if not isinstance(max_length, int) or max_length < 0: # check if max_length is a positive integer or None
                raise TypeError("max_length must be a positive integer or None")

            
        if capitalize:
          
          text = text.capitalize() # capitalize the first letter of the text
        
        formatted_text = prefix + text + suffix

        if max_length is not None and max_length > 0 and len(formatted_text) > max_length:
             
             formatted_text = formatted_text[:max_length] # cut the text to max_length

        return formatted_text
    
    except(TypeError, TypeError) as e:
        return f"Error: {e}"

text1 = format_text("CST NYARUGENGE", prefix="Welcome in ", capitalize=False, max_length=None)
print(text1) 
text2 = format_text("information technology department", prefix=" ", suffix="", capitalize=True, max_length=27) 
print(text2)
text3 = format_text("how are you", prefix="Hey", suffix="?", capitalize=True, max_length=15)
print(text3)

        



    