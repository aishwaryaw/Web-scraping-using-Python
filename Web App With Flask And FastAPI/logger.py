import os
import datetime

abs_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(abs_path)
logs_dir = os.path.join(BASE_DIR, "logs")
os.makedirs(logs_dir, exist_ok=True)


def trigger_log_save():
    
    filename = f"{datetime.datetime.now()}.txt"
    filename = filename.replace(" ", "-")
    filename = filename.replace(".", "-")
    filename = filename.replace(":", "-")
    filepath = os.path.join(logs_dir, filename)
    with open(filepath, 'w+') as f:
        f.write("triggered")
