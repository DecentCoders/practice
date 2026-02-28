import os
from datetime import datetime  # To convert timestamp to readable time

def get_file_info(file_path):
    # Validate file exists first
    if not os.path.isfile(file_path):
        print(f"Error: '{file_path}' is not a valid file or does not exist.")
        return
    
    # Get file stats using os.stat()
    file_stats = os.stat(file_path)
    
    # 1. File size (in bytes)
    file_size = file_stats.st_size
    # Convert to KB (optional, for readability)
    file_size_kb = file_size / 1024
    
    # 2. Last modification time (timestamp → readable format)
    mod_timestamp = file_stats.st_mtime  # Unix timestamp (seconds since epoch)
    mod_time = datetime.fromtimestamp(mod_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    
    # Print results
    print(f"File: {file_path}")
    print(f"Size: {file_size} bytes ({file_size_kb:.2f} KB)")
    print(f"Last Modified: {mod_time}")

# Test with a sample file (replace with your file path)
# Use os.path.join for cross-platform compatibility
sample_file = os.path.join(os.getcwd(), "test.txt")
# Create a dummy test.txt if it doesn't exist (for testing)
with open(sample_file, "w") as f:
    f.write("Sample content for os module practice")

get_file_info(sample_file)