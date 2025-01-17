import sys

def extract_logs_by_date(log_file_path, date):
    output_file_path = f"output/output_{date}.txt"
    
    try:
        with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
            for line in log_file:
                # Check if the line starts with the correct date (first 10 characters)
                if line[:10] == date:
                    output_file.write(line)
        
        print(f"Logs for {date} have been written to {output_file_path}")
    
    except FileNotFoundError:
        print(f"Error: Log file {log_file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    date = sys.argv[1]
    
    # Validate date format
    try:
        # Try to parse the date to ensure it is in the correct format
        from datetime import datetime
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        sys.exit(1)

    log_file_path = "test_logs.log"  # Specify the path to your large log file
    extract_logs_by_date(log_file_path, date)
