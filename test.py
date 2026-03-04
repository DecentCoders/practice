import os
import shutil

def sort_files_by_type(source_folder):
    # Create target folders (ignore if exists)
    folder_mapping = {
        ".jpg": "images",
        ".png": "images",
        ".pdf": "docs",
        ".docx": "docs",
        ".mp4": "videos",
        ".mov": "videos",
        ".txt": "others"
    }
    
    # Create all target folders first
    for folder in set(folder_mapping.values()):
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
    
    # Iterate over files in source folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        # Skip directories (only process files)
        if os.path.isfile(file_path):
            # Get file extension (lowercase for case-insensitive matching)
            ext = os.path.splitext(filename)[1].lower()
            # Find target folder (default to "others")
            target_folder = folder_mapping.get(ext, "others")
            target_path = os.path.join(source_folder, target_folder, filename)
            
            # Move file
            try:
                shutil.move(file_path, target_path)
                print(f"Moved: {filename} → {target_folder}/")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

# Step 1: Create test folder and mixed files
def create_mixed_files():
    source_folder = "downloads_test"
    os.makedirs(source_folder, exist_ok=True)
    
    # Create 5 files of each type
    file_types = [".jpg", ".pdf", ".mp4", ".txt"]
    for ext in file_types:
        for i in range(1, 6):
            filename = f"test_{i}{ext}"
            file_path = os.path.join(source_folder, filename)
            with open(file_path, "w") as f:
                pass
    print(f"Created mixed files in {source_folder}")
    return source_folder

# Run
source = create_mixed_files()
sort_files_by_type(source)