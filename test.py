import os

def delete_empty_folders_recursive(folder):
    if not os.path.isdir(folder):
        print(f"Error: {folder} does not exist!")
        return
    
    confirm = input(f"Are you sure you want to delete ALL empty folders in {folder} (recursive)? (y/n): ").lower()
    if confirm != "y":
        print("Deletion cancelled.")
        return
    
    # Traverse from deepest level up (topdown=False)
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            # Check if folder is empty
            if len(os.listdir(dir_path)) == 0:
                try:
                    os.rmdir(dir_path)
                    print(f"Deleted empty folder (recursive): {dir_path}")
                except Exception as e:
                    print(f"Error deleting {dir_path}: {e}")

# Test (create nested empty folders)
def create_nested_empty_folders():
    test_dir = "cleanup_test"
    # Create nested structure: cleanup_test/a/b/c (empty), cleanup_test/x/y (empty)
    os.makedirs(os.path.join(test_dir, "a", "b", "c"), exist_ok=True)
    os.makedirs(os.path.join(test_dir, "x", "y"), exist_ok=True)
    # Add a file to cleanup_test/a (so "a" is not empty, but "b/c" is)
    with open(os.path.join(test_dir, "a", "file.txt"), "w") as f:
        pass
    print(f"Created nested empty folders in {test_dir}")
    return test_dir

# Run
test_dir = create_nested_empty_folders()
delete_empty_folders_recursive(test_dir)