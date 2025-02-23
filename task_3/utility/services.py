from pathlib import Path

def parse_log_line(line:str)->dict:
    return {
        "date": line.split()[0],
        "time": line.split()[1],
        "message_type": line.split()[2].upper(),
        "message": " ".join(line.split()[3:])
    }

def load_logs(file_path:str)->list:
    with open(Path(file_path),"r") as file:
        return [parse_log_line(line) for line in file]
    
def filter_logs_by_level(logs:list, level:str)->list:
    return [log for log in logs if log["message_type"].casefold() == level.casefold()]

def count_logs_by_level(logs:list,logs_levels:list)->dict:
    return {level: len(filter_logs_by_level(logs, level)) for level in logs_levels}


def display_log_counts(counts:dict):
    table_header_one = "Log level"
    table_header_two = "Count"
    table_column_width = 10

    print(f"{table_header_one:<{table_column_width}} | {table_header_two:<{table_column_width}} |")
    print(f"{'-'*table_column_width} | {'-'*table_column_width} |")
    for level, count in counts.items():
        print(f"{level:<{table_column_width}} | {count:<{table_column_width}} |")


def display_logs_by_level(logs:list,level:str):
    print(f"\nDisplaying details of logs with level: {level}")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")