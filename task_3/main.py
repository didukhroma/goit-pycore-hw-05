import sys
from pathlib import Path
from utility.services import load_logs, count_logs_by_level, filter_logs_by_level,display_log_counts, display_logs_by_level

def main():
    try:
        logs_levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
        
        path = sys.argv[1]

        attr = ''
        if len(sys.argv) > 2:
            attr = sys.argv[2].upper()
        
        

        if not Path(path).is_file():
            raise Exception(f"{path} is not a valid file path")
        
        
        logs = load_logs(path)
        logs_count = count_logs_by_level(logs,logs_levels)
       

        display_log_counts(logs_count)

        if attr :
            if  not attr in logs_levels:
                raise Exception(f"\n{attr} is not a valid log level. Please provide one of the following log levels: INFO, DEBUG, ERROR, WARNING")
        
            logs_filtered_by_level = filter_logs_by_level(logs, attr)
            display_logs_by_level(logs_filtered_by_level, attr)
        


    except Exception as e:
        print(f"Error: {e}")
       



if __name__ == '__main__':
    main()