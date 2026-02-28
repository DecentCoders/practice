import os

def batch_rename_jpg(directory):
    # Validate directory exists
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory.")
        return

    # Get all .jpg files in the directory
    jpg_files = []
    for file_name in os.listdir(directory):
        # Full path to the file (cross-platform)
        file_path = os.path.join(directory, file_name)
        # Check if it's a file (not a directory) and ends with .jpg/.JPG (case-insensitive)
        if os.path.isfile(file_path) and file_name.lower().endswith(".jpg"):
            jpg_files.append(file_name)

    # Exit if no .jpg files found
    if not jpg_files:
        print("No .jpg files found in the directory.")
        return

    # Sort files (optional, for consistent numbering)
    jpg_files.sort()

    # Batch rename
    for count, old_name in enumerate(jpg_files, 1):
        # Split old name into name and extension (e.g., "vacation.jpg" → ("vacation", ".jpg"))
        old_path = os.path.join(directory, old_name)
        new_name = f"photo_{count}.jpg"
        new_path = os.path.join(directory, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed: {old_name} → {new_name}")
        except FileExistsError:
            print(f"Error: {new_name} already exists (skip renaming {old_name}).")
        except PermissionError:
            print(f"Error: No permission to rename {old_name}.")
        except Exception as e:
            print(f"Unexpected error renaming {old_name}: {e}")

# Test with current directory (replace with your target directory)
target_dir = os.getcwd()
batch_rename_jpg(target_dir)