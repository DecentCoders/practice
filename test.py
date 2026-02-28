import os

def change_working_dir(target_dir):
    # Print initial CWD
    print(f"Initial CWD: {os.getcwd()}")
    
    try:
        # Change to target directory
        os.chdir(target_dir)
        print(f"Success! New CWD: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Error: Directory '{target_dir}' does not exist.")
    except PermissionError:
        print(f"Error: No permission to access '{target_dir}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Get user's Documents directory (cross-platform)
# For Windows: C:/Users/[Name]/Documents
# For macOS/Linux: /home/[Name]/Documents
if os.name == "nt":  # Windows
    documents_dir = os.path.join(os.environ["USERPROFILE"], "Documents")
else:  # macOS/Linux
    documents_dir = os.path.join(os.environ["HOME"], "Documents")

# Test the function
change_working_dir(documents_dir)

# Optional: Reset to original CWD (uncomment if needed)
# os.chdir(original_cwd)