# Excel Comparison Project

## Intro

This is a python project that shows differences between two similar-ish excel files.

The app takes an old excel file and a new excel file and outputs an excel file (Shocking! Right?) with a new column: `changes`

The files should have Key Column and Compare Columns (which are set in a `.env` file:
  - Key column acts like primary keys in databases, and the rows are identified by it.
  - Compare columns are what we detect changes on.

So the other columns' values can vary between two excel files, but we only compare the specified columns.

After running the app on files, the output is an excel file, with data based on the new excel rows, but:
  - To show the changes, we add a new column: `changes` to our output file.
  - And lastly, the data in old rows, but not in new rows are appended to the output file rows; with column `changes` value: `left`

For better understanding, here's an example below (if you are smart, you can skip it :) and read the installation guide).

### Example scenario:

We have two excels of our employees, two version of them--one with updated data.

We want to detect changes in their levels in the organization.

Each employee (each row), has a `personnel id` (key column) and a `level` column (compare column).

We iterate over the rows of the newer file and check that row by `personnel id` in the older excel rows.

#### Cases:
  - The row exists but the Compare columns are not identical -> include all changes in a new column: `changes` (e.g. `myCompareCol: 2.3->4.4`)
  - The row with this Key column does not exist in older data -> It's a new row and `changes`' value: `new joiner`
  - The old row is not present in new data -> Deleted row and `changes`'s value: `left the company`

## Installation
Search installing `python` and `pip` if you don't have it.
Also, if you're on Windows, Windows Command Line is stupid, get [this](https://gitforwindows.org/) which gives you bash terminal.

- Clone the project
  ```
  git clone https://github.com/sananqsh/update_excel_project.git
  ```

- Install requirements (it's preferred to use [virtual environments](https://docs.python.org/3/library/venv.html) for installed packages)
  ```
  pip install -r requirements.txt
  ```
- Fill the `.env` file with valid data
  - Previous file, current file, the name of the output file, key column and the compare column.
- Run the app
  ```
  python3 main.py
  ```

If all things go OK, an output file would be created!

> You can also specify the name of the files while running the script.
> ```
> python3 main.py --prev my_prev_file.xlsx --cur my_current_file.xlsx --out my_output_file.xlsx
> ```
> All of these arguments are optional and they're default values are read from the `.env` file.
