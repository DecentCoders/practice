def extract_error_name(line):
    """Function to pull the error message out of a log string."""
    if "ERROR" in line:
        # Splitting by " - " and taking the last part
        parts = line.split(" - ")
        return parts[-1].strip()
    return None

def process_logs(input_file, output_file):
    error_counts = {}

    # Read logic
    try:
        with open(input_file, "r") as f:
            for line in f:
                error = extract_error_name(line)
                if error:
                    # Update dictionary: if error exists, +1; if not, set to 1
                    error_counts[error] = error_counts.get(error, 0) + 1
        
        # Write logic
        with open(output_file, "w") as out:
            out.write("--- ERROR SUMMARY REPORT ---\n")
            for error, count in error_counts.items():
                out.write(f"{error}: {count} occurrences\n")
        
        print(f"Success! Report saved to {output_file}")

    except FileNotFoundError:
        print("Error: The raw log file was not found.")

# Run the program
process_logs("raw_logs.txt", "cleaned_report.txt")