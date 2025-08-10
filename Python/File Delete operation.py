import os

filepath = r'D:\SQL and Python Practice\Python\abc.py'

if os.path.exists(filepath):
    try:
        os.remove(filepath)
        print(f"File '{filepath}' has been deleted successfully.")
    except Exception as e:
        print(f"An error occurred while trying to delete the file: {e}")
else:
    print(f"File '{filepath}' does not exist.")
