import os
import pandas as pd
import argparse
from dotenv import load_dotenv

load_dotenv(".env")

PREV_FILE_PATH = os.environ.get("PREV_FILE")
CURRENT_FILE_PATH = os.environ.get("CURRENT_FILE")
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

def compare_and_add_changes(prev_data, cur_data, compare_key):
    """
        Compares row data
        The current version only checks the `compare_key` column for changes
        But generalization is possible, if requested 
    """

    for id, cur_row in cur_data.items():
        # Compare row data
        if id in prev_data:
            prev_row = prev_data[id]
            if prev_row[compare_key] != cur_row[compare_key]:
                cur_row["changes"] = f"{prev_row.get(compare_key)}->{cur_row.get(compare_key)}"
            else:
                cur_row["changes"] = ""

        else:
            cur_row["changes"] = "new joiner"


    # rows that are not in the cur data:
    left_company_keys = set(prev_data.keys()) - set(cur_data.keys())
    for id in left_company_keys:
        prev_row = prev_data[id]
        cur_row = prev_row.copy()
        cur_row["changes"] = "left company"
        cur_data[id] = cur_row

    return cur_data


def write_excel_data(updated_data, output_file_path, key_column):
    rows_list = [{key_column: id, **row_data} for id, row_data in updated_data.items()]
    data_frame = pd.DataFrame(rows_list)
    data_frame.to_excel(output_file_path, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compare and update row data.")
    parser.add_argument("--prev", default=PREV_FILE_PATH, help="Name of the prev Excel file")
    parser.add_argument("--cur", default=CURRENT_FILE_PATH, help="Name of the current Excel file")
    parser.add_argument("--out", default=OUTPUT_FILE_PATH, help="Name of the output Excel file")
    args = parser.parse_args()

    prev_file_path = args.prev
    cur_file_path = args.cur    
    output_file_path = args.out
    
    prev_data = read_excel_data(prev_file_path, KEY_COLUMN)
    cur_data = read_excel_data(cur_file_path, KEY_COLUMN)

    updated_data = compare_and_add_changes(prev_data, cur_data.copy(), COMP_COLUMN)

    write_excel_data(updated_data, output_file_path, KEY_COLUMN)
