import os
import shutil

def sort_files_by_size(source_folder):
    # Define size thresholds (1MB = 1024*1024 bytes)
    size_folders = {
        "small_files": (0, 1024*1024),          # <1MB
        "medium_files": (1024*1024, 10*1024*1024), # 1MB-10MB
        "large_files": (10*1024*1024, float("inf")) # >10MB
    }
    
    # Create size folders
    for folder in size_folders.keys():
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            # Get file size in bytes
            file_size = os.stat(file_path).st_size
            
            # Determine target folder
            target_folder = None
            for folder, (min_size, max_size) in size_folders.items():
                if min_size <= file_size < max_size:
                    target_folder = folder
                    break
            
            if target_folder:
                target_path = os.path.join(source_folder, target_folder, filename)
                try:
                    shutil.move(file_path, target_path)
                    print(f"Moved {filename} ({file_size/1024:.2f} KB) → {target_folder}/")
                except Exception as e:
                    print(f"Error moving {filename}: {e}")

# Test (create files with different sizes - dummy content)
def create_files_with_sizes():
    source_folder = "downloads_test"
    os.makedirs(source_folder, exist_ok=True)
    
    # Small file (<1MB: 500KB)
    small_file = os.path.join(source_folder, "small.txt")
    with open(small_file, "w") as f:
        f.write("a" * 500 * 1024)  # 500KB of text
    
    # Medium file (5MB)
    medium_file = os.path.join(source_folder, "medium.txt")
    with open(medium_file, "w") as f:
        f.write("b" * 5 * 1024 * 1024)  # 5MB of text
    
    # Large file (15MB)
    large_file = os.path.join(source_folder, "large.txt")
    with open(large_file, "w") as f:
        f.write("c" * 15 * 1024 * 1024)  # 15MB of text
    
    print(f"Created size-test files in {source_folder}")
    return source_folder

# Run
source = create_files_with_sizes()
sort_files_by_size(source)