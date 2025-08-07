def isstringalphanumeric(s):
    """
    Check if the input string is alphanumeric (containing only letters and numbers).
    
    :param s: Input string to check
    :return: True if the string is alphanumeric, False otherwise
    """
    return s.isalnum()

# Example usage
string1 = "Hello$"
if isstringalphanumeric(string1):
    print(f"The string '{string1}' is alphanumeric.")
else:
    print(f"The string '{string1}' is not alphanumeric.")