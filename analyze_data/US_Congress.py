def check_memory_usage(df, col_type='object'):
    """
    Calculates the memory usage of each column in the specified DataFrame `df`,
    after converting the column to the specified data type `col_type`.

    Args:
        df (pandas.DataFrame): The DataFrame for which to calculate memory usage.
        col_type (str, optional): The data type to which each column should be
            converted before calculating memory usage. Defaults to 'object'.

    Returns:
        dict: A dictionary containing the memory usage of each column in bytes,
        after conversion to the specified data type. The dictionary also includes
        the total memory usage of the DataFrame in bytes.

    """
    memory_dict = {}
    for col in df.columns:
        memory_dict[col] = df[col].astype(col_type).memory_usage(deep=True, index=False)
    memory_dict['total_memory_usage'] = sum(memory_dict.values())
    return memory_dict


def memory_usage_difference(df, col_type1='object', col_type2='category'):
    """
    Calculates the difference in memory usage between two different column data types for a given DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame for which to calculate the memory usage difference.
        col_type1 (str, optional): The first column data type. Defaults to 'object'.
        col_type2 (str, optional): The second column data type. Defaults to 'category'.

    Returns:
        dict: A dictionary containing the memory usage difference (in bytes) for each column and the total difference.
    """
    # Get memory usage for both column data types
    memory_usage1 = check_memory_usage(df, col_type=col_type1)
    memory_usage2 = check_memory_usage(df, col_type=col_type2)

    # Calculate the difference in memory usage
    diff_dict = {}
    for col in df.columns:
        diff_dict[col] = memory_usage1[col] - memory_usage2[col]

    # Calculate total difference
    total_diff = sum(diff_dict.values())

    # Create output dictionary
    output_dict = {
        'column_diff': diff_dict,
        'total_diff': total_diff
    }

    return output_dict

