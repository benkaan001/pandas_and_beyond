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


def extract_count(dict_list: dict) -> int:
    """
    Extracts the count values from a list of dictionaries and returns their sum.

    Parameters:
    -----------
    dict_list: list of dict
        A list of dictionaries containing 'count' values.

    Returns:
    --------
    int
        The sum of the 'count' values in the input list of dictionaries.

    Example:
    --------
    >>> dict_list = [{'count': 3}, {'count': 5}, {'count': 2}]
    >>> extract_count(dict_list)
    10
    """
    return sum(int(d['count']) for d in dict_list)


def extract_negative_remark_count(dict_list: dict) -> int:
    """
Extracts the total count of negative remarks from a list of dictionaries.

Parameters:
dict_list (list[dict]): A list of dictionaries, each containing a 'name' key representing the type of remark and a 'count' key representing the number of occurrences of that type of remark.

Returns:
int: The total count of negative remarks in the dict_list, where a negative remark is defined as one of 'Longwinded', 'Unconvincing', or 'Obnoxious'.

Example:
dict_list = [{'name': 'Longwinded', 'count': '5'}, {'name': 'Inappropriate', 'count': '2'}, {'name': 'Obnoxious', 'count': '3'}]
extract_negative_remark_count(dict_list) -> 8
In this example, there are 5 occurrences of 'Longwinded' and 3 occurrences of 'Obnoxious', so the total count of negative remarks is 8.
"""
    remarks = ['Longwinded', 'Unconvincing', 'Obnoxious']
    total_count = 0
    for d in dict_list:
        if d['name'] in remarks:
            count = int(d['count'])
            total_count += count
    return total_count



def extract_funny_count(dict_list: list) -> int:
    """
    Extracts the count of the 'Funny' category from a list of dictionaries.

    Parameters:
    -----------
    dict_list : list
        A list of dictionaries, where each dictionary contains a 'name' key and a 'count' key.

    Returns:
    --------
    int
        The total count of the 'Funny' category in the list of dictionaries.

    Example:
    --------
    >>> dict_list = [{'name': 'Funny', 'count': '10'},
                     {'name': 'Cool', 'count': '5'},
                     {'name': 'Useful', 'count': '7'},
                     {'name': 'Funny', 'count': '3'}]
    >>> extract_funny_count(dict_list)
    13
    """
    funny_count = 0
    for d in dict_list:
        if d['name'] == 'Funny':
            funny_count += int(d['count'])
    return funny_count
