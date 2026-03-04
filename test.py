import os

def rename_with_prefix_suffix(folder, add_prefix=True, prefix="vacation_", suffix="_2025"):
    if not os.path.isdir(folder):
        print(f"Error: {folder} does not exist!")
        return
    
    for filename in os.listdir(folder):
        # Only process .jpg files from Problem 1
        if filename.endswith(".jpg") and filename.startswith("photo_"):
            # Split filename and extension (e.g., "photo_001.jpg" → ("photo_001", ".jpg"))
            name, ext = os.path.splitext(filename)
            
            # Apply prefix/suffix
            if add_prefix:
                new_name = f"{prefix}{name}{ext}"
            else:
                new_name = f"{name}{suffix}{ext}"
            
            # Full paths
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} → {new_name}")
            except Exception as e:
                print(f"Error renaming {filename}: {e}")

# Test: Add prefix first, then suffix (uncomment one at a time)
test_folder = "batch_rename_test"
rename_with_prefix_suffix(test_folder, add_prefix=True)  # vacation_photo_001.jpg
# rename_with_prefix_suffix(test_folder, add_prefix=False)  # photo_001_2025.jpg