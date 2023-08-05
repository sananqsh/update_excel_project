import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv(".env")

# Define the file path of the Excel file
INPUT_FILE_PATH = os.environ.get("INPUT_FILE")
COMPARE_FILE_PATH = os.environ.get("COMPARE_FILE")

# KEY_COLUMN = os.environ.get("KEY_COLUMN")

# TEST:
KEY_COLUMN = 'استاد'

# Use the pandas library to read the Excel file
input_data_frame = pd.read_excel(INPUT_FILE_PATH)
# compare_data_frame = pd.read_excel(COMPARE_FILE_PATH)

# Convert the data frame into a list of dictionaries where each dictionary represents a row
input_rows_list = input_data_frame.to_dict('records')
# compare_rows_list = compare_data_frame.to_dict('records')

idf_dict = {
        row[KEY_COLUMN]: {
                key: value for key, value in row.items() if key != KEY_COLUMN
        } for row in input_rows_list
}

# Print the list of rows
for row in idf_dict:
        print(row)
        print(":{\n")
        print(idf_dict[row])
        print("\n}\n")

