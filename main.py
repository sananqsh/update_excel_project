import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

OLD_FILE_PATH = os.environ.get("OLD_FILE")
NEW_FILE_PATH = os.environ.get("NEW_FILE")
OUTPUT_FILE_PATH = os.environ.get("OUTPUT_FILE")

KEY_COLUMN = os.environ.get("KEY_COLUMN")
COMP_COLUMN = os.environ.get("COMPARE_COLUMN")


def read_excel_data(file_path, key_column):
    """
        Reads excel files with pandas library
        Converts the data frame into a list of dictionaries, each dict === a row
        And returns a dictionary of dictionaries, with key_column as main key
    """

    # TODO: Handle FileNotFound and KeyError exceptions

    data_frame = pd.read_excel(file_path)
    rows_list = data_frame.to_dict('records')

    return {
        row[key_column]: {
            key: value for key, value in row.items() if key != key_column
        } for row in rows_list
    }

def compare_and_add_changes(old_data, new_data, compare_key):
    """
        Compares employee data
        The current version only checks the `level` column for changes
        But generalization is possible, if requested 
    """

    for id, new_employee in new_data.items():
        # Compare employee data
        if id in old_data:
            old_employee = old_data[id]
            if old_employee[compare_key] != new_employee[compare_key]:
                new_employee["changes"] = f"{old_employee.get(compare_key)}->{old_employee.get(compare_key)}"
            else:
                new_employee["changes"] = ""

        else:
            new_employee["changes"] = "new joiner"


    # Employees that are not in the new data:
    for id, old_employee in old_data.items():
       if id not in new_data:
           new_employee = old_employee
           new_employee["changes"] = "left company"
           new_data[id] = new_employee


def write_excel_data(updated_data, output_file_path, key_column):
    rows_list = [{key_column: id, **employee_data} for id, employee_data in updated_data.items()]
    data_frame = pd.DataFrame(rows_list)
    data_frame.to_excel(output_file_path, index=False)


if __name__ == "__main__":
    old_data = read_excel_data(OLD_FILE_PATH, KEY_COLUMN)
    new_data = read_excel_data(NEW_FILE_PATH, KEY_COLUMN)

    compare_and_add_changes(old_data, new_data, COMP_COLUMN)
    write_excel_data(new_data, OUTPUT_FILE_PATH, KEY_COLUMN)
