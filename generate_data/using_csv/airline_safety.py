import csv

def add_column(col_name: str,
               col_values: list,
               position: int = None,
               file_path: str = '../data/cleaned/airline_safety_clean.csv') -> None:
    """
    Add a new column with the given column name and col_values to an existing CSV file.

    Args:
        col_name (str): The name of the new column to be added.
        col_values (list): A list of col_values for the new column. The length of the list
            should be the same as the number of rows in the CSV file.
        position (int): The position at which to insert the new column.
            Default is None, which appends the column to the end of the CSV file.
        file_path (str): The path to the CSV file. Default is
            '../data/cleaned/airline_safety_clean.csv'.

    Returns:
        None

    Raises:
        ValueError: If the length of the col_values list does not match the number
            of rows in the CSV file.

    Example:
        # Add a new column named 'new_col' with col_values [1, 2, 3] to the CSV file
        # located at '../data/cleaned/airline_safety_clean.csv'.
        add_column('new_col', [1, 2, 3], '../data/cleaned/airline_safety_clean.csv')
    """

    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        reader_data = list(reader)
        header, data = reader_data[0], reader_data[1:]

    # Check if column length matches the number of rows
    if len(col_values) != len(data):
        raise ValueError("Length of col_values list does not match number of rows in CSV file.")

    # Determine the column position:
    if position is None:
        position = len(header)

    # Add the column name to the position
    header.insert(position, col_name)

    # Add col_values to the data rows
    for i, row in enumerate(data):
        row.insert(position, col_values[i])

    # Update the CSV file
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(header)
        writer.writerows(data)

    # Print confirmation
    print(f"Added new column '{col_name}' at position {position} to {file_path.split('/')[-1]} file.")
