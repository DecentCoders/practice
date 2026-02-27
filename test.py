import os

def count_total_files(directory):
    """
    Count the total number of files (excluding directories) in a given directory and all its subdirectories.
    """
    total_file_count = 0

    for root, dirs, files in os.walk(directory):
        total_file_count += len(files) 
    return total_file_count

if __name__ == "__main__":
    target_directory = "./your_target_dir" 
    try:
        count = count_total_files(target_directory)
        print(f"Total number of files in {target_directory} (including subdirectories): {count}")
    except FileNotFoundError:
        print(f"Error: The directory {target_directory} does not exist.")
    except NotADirectoryError:
        print(f"Error: {target_directory} is not a valid directory (it is a file).")