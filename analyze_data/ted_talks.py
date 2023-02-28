import ast

def str_to_list(ratings_str: str) -> list:
    """
    Converts a string representation of a list to a Python list object.

    Arguments:
    ratings_str -- a string representation of a Python list object.

    Returns:
    A Python list object containing the elements from the input string.

    Raises:
    ValueError -- if the input string is not a valid string representation of a Python list object.

    Dependencies:
    This function depends on the ast module to convert the string to a list object.
    """

    try:
        return ast.literal_eval(ratings_str)
    except (ValueError, SyntaxError):
        raise ValueError("Invalid string representation of a Python list object.")