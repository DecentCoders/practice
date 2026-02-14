def process_logs(input_file, output_file):
    # This dictionary acts as our database
    error_counts = {}

    try:
        # 1. READ: Open the file for reading ('r')
        with open(input_file, "r") as f:
            for line in f:
                if "ERROR" in line:
                   
                    parts = line.strip().split(" - ")
                    error_msg = parts[-1] 
                    if error_msg in error_counts:
                        error_counts[error_msg] += 1
                    else:
                        error_counts[error_msg] = 1
        
        # 4. WRITE: Save the results to the output file ('w')
        with open(output_file, "w") as out:
            out.write("ERROR FREQUENCY REPORT\n")
            out.write("="*22 + "\n")
            for error, count in error_counts.items():
                out.write(f"{error}: {count}\n")
        
        print(f"Processed successfully. Check {output_file}")

    except FileNotFoundError:
        print("Error: Input file missing!")

# Running the script
process_logs("raw_logs.txt", "summary.txt")