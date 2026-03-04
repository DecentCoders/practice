import os
from datetime import datetime

def rename_by_creation_date(folder):
    if not os.path.isdir(folder):
        print(f"Error: {folder} does not exist!")
        return
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        # Skip directories (only process files)
        if os.path.isfile(file_path):
            # Get creation time (st_ctime = creation time, st_mtime = modification time)
            create_time = os.stat(file_path).st_ctime
            # Convert timestamp to YYYY-MM-DD format
            date_str = datetime.fromtimestamp(create_time).strftime("%Y-%m-%d")
            # New filename: YYYY-MM-DD_filename.ext
            new_filename = f"{date_str}_{filename}"
            new_path = os.path.join(folder, new_filename)
            
            try:
                os.rename(file_path, new_path)
                print(f"Renamed: {filename} → {new_filename}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

# Test
rename_by_creation_date("batch_rename_test")