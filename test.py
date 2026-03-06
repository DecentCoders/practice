import os
import shutil
from datetime import datetime, timedelta

def sort_files_by_access_time(source_folder):
    # Define time thresholds (7 days ago)
    seven_days_ago = datetime.now() - timedelta(days=7)
    time_folders = {
        "recent": seven_days_ago,
        "old": datetime.min
    }
    
    # Create time folders
    for folder in time_folders.keys():
        os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
    
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            # Get last access time (st_atime)
            access_time = datetime.fromtimestamp(os.stat(file_path).st_atime)
            
            # Determine target folder
            if access_time >= seven_days_ago:
                target_folder = "recent"
            else:
                target_folder = "old"
            
            target_path = os.path.join(source_folder, target_folder, filename)
            try:
                shutil.move(file_path, target_path)
                print(f"Moved {filename} (accessed: {access_time.strftime('%Y-%m-%d')}) → {target_folder}/")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

# Test (create files with different access times - simulate old files)
def create_files_with_access_times():
    source_folder = "downloads_test"
    os.makedirs(source_folder, exist_ok=True)
    
    # Recent file (access time = now)
    recent_file = os.path.join(source_folder, "recent.txt")
    with open(recent_file, "w") as f:
        f.write("Recent file")
    
    # Old file (access time = 10 days ago - simulate by modifying st_atime)
    old_file = os.path.join(source_folder, "old.txt")
    with open(old_file, "w") as f:
        f.write("Old file")
    
    # Note: On most OS, you can't manually set st_atime easily (this is a simulation)
    print(f"Created time-test files in {source_folder}")
    return source_folder

# Run
source = create_files_with_access_times()
sort_files_by_access_time(source)