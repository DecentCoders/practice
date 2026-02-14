def extract_error_name(line):
    """
    Function to pull the error message out of a log string.
    Expected format: "Date Time - LEVEL - Message"
    """
    if "ERROR" in line:
        # Splitting by " - " creates: ["2026-02-14 10:05", "ERROR", "Connection Timeout"]
        parts = line.split(" - ")
        # We take the last part (index -1) and clean up any whitespace
        return parts[-1].strip()
    return None
def extract_details(line):
    if "ERROR" in line:
        parts = line.split(" - ")
        time = parts[0]
        message = parts[-1].strip()
        return (time, message)
    return None

def process_logs(input_file, output_file):
    error_counts = {}

    try:
        # 1. READ the raw log file
        with open(input_file, "r") as f:
            for line in f:
                error = extract_error_name(line)
                if error:
                    # 2. MANIPULATE data: Count occurrences in a dictionary
                    # .get(error, 0) avoids KeyErrors if it's the first time seeing the error
                    error_counts[error] = error_counts.get(error, 0) + 1
        
        # 3. WRITE the final report
        with open(output_file, "w") as out:
            out.write("--- ERROR SUMMARY REPORT ---\n")
            # Loop through the dictionary items to format the output
            for error, count in error_counts.items():
                out.write(f"[{error}] found {count} times.\n")
        
        print(f"Success! Report saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found. Please run the dummy file generator first.")

# Execute the process
process_logs("raw_logs.txt", "cleaned_report.txt")