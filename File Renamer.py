import os
import pathlib
dir_path = input("Enter the directory path: ")
if not os.path.exists(dir_path):
    print("The specified directory does not exist.")
else:
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            new_filename = input(f"Enter new name for '{filename}': ")
            new_file_path = os.path.join(dir_path, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed '{filename}' to '{new_filename}'")