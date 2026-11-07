Python Bulk File Renamer

A simple Python-based file renaming tool that allows users to rename multiple files in a directory interactively.

## Features

- Specify a directory path.
- Check whether the directory exists.
- Automatically detect files inside the directory.
- Enter new names for individual files.
- Rename files using Python's built-in `os` module.
- Display confirmation after each successful rename.

## Technologies Used

- Python 3
- `os` module
- `pathlib` module

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/V-920/Bulk-File-Renamer
   ```

2. Navigate to the project directory:

   ```bash
   cd Bulk-File-Renamer
   ```

3. Run the Python script:

   ```bash
   python "File Renamer.py"
   ```

4. Enter the directory path when prompted.
5. Enter a new name for each file.

## Example

```text
Enter the directory path: C:\Users\Example\Documents

Enter new name for 'old.txt': new.txt
Renamed 'old.txt' to 'new.txt'
```

## What I Learned

- Working with Python's `os` module.
- Checking directory existence.
- Listing files in a directory.
- Working with file paths.
- Using `os.rename()` to rename files.
- Taking user input and handling basic conditions.

## Future Improvements

- Add automatic bulk renaming.
- Support custom file naming patterns.
- Add duplicate filename handling.
- Add error handling for invalid filenames.
