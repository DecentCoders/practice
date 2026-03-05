import os
import shutil

# Reuse functions from previous problems (simplified)
def batch_rename_workflow(folder):
    """Step 1: Batch rename files with prefix 'my_files_'"""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            new_filename = f"my_files_{filename}"
            new_path = os.path.join(folder, new_filename)
            try:
                os.rename(file_path, new_path)
                print(f"Renamed: {filename} → {new_filename}")
            except Exception as e:
                print(f"Rename error: {e}")

def organize_workflow(folder):
    """Step 2: Organize by file type"""
    folder_mapping = {".jpg": "images", ".pdf": "docs", ".mp4": "videos", ".txt": "others"}
    for folder_name in set(folder_mapping.values()):
        os.makedirs(os.path.join(folder, folder_name), exist_ok=True)
    
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            target_folder = folder_mapping.get(ext, "others")
            target_path = os.path.join(folder, target_folder, filename)
            try:
                shutil.move(file_path, target_path)
                print(f"Organized: {filename} → {target_folder}/")
            except Exception as e:
                print(f"Organize error: {e}")

def cleanup_workflow(folder):
    """Step 3: Delete empty folders"""
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if len(os.listdir(dir_path)) == 0:
                try:
                    os.rmdir(dir_path)
                    print(f"Cleaned up empty folder: {dir_path}")
                except Exception as e:
                    print(f"Cleanup error: {e}")

# Main workflow
def full_workflow():
    # Create test folder with mixed files
    workflow_dir = "full_workflow_test"
    os.makedirs(workflow_dir, exist_ok=True)
    
    # Create 10 mixed files
    for ext in [".jpg", ".pdf", ".mp4", ".txt"]:
        for i in range(1, 4):
            filename = f"workflow_{i}{ext}"
            file_path = os.path.join(workflow_dir, filename)
            with open(file_path, "w") as f:
                pass
    
    # Create empty test folder (to cleanup later)
    os.makedirs(os.path.join(workflow_dir, "empty_test"), exist_ok=True)
    
    # Run full workflow
    print("=== Step 1: Batch Rename ===")
    batch_rename_workflow(workflow_dir)
    
    print("\n=== Step 2: Organize Files ===")
    organize_workflow(workflow_dir)
    
    print("\n=== Step 3: Cleanup Empty Folders ===")
    cleanup_workflow(workflow_dir)
    
    print("\n✅ Full workflow completed!")

# Run
full_workflow()