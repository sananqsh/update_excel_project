import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

def read_excel_data(file_path, key_column):
        # Use the pandas library to read the Excel file
        data_frame = pd.read_excel(file_path)
        # Convert the data frame into a list of dictionaries (each dict = a row)
        rows_list = data_frame.to_dict('records')

        # Return a dictionary of dictionaries, with key_column as main key
        return {
                row[key_column]: {
                        key: value for key, value in row.items() if key != key_column
                } for row in rows_list
        }

def compare_and_add_changes(old_data, new_data, key, compare_key):
        pass

# Define the file path of the Excel file
OLD_FILE_PATH = os.environ.get("OLD_FILE")
NEW_FILE_PATH = os.environ.get("NEW_FILE")

KEY_COLUMN = os.environ.get("KEY_COLUMN")
COMP_COLUMN = os.environ.get("COMPARE_COLUMN")

old_data = read_excel_data(OLD_FILE_PATH, KEY_COLUMN)
new_data = read_excel_data(NEW_FILE_PATH, KEY_COLUMN)

