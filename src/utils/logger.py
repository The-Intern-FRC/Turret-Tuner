import os
import csv
from datetime import datetime

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

LOG_DIR = "reports/logs"
ensure_dir(LOG_DIR)
LOG_FILE = os.path.join(LOG_DIR, "analysis_log.csv")

def log_shot(shot_data):
    # shot_data: dict with keys ['shot_num','timestamp','yaw','pitch','velocity','hit','extras']
    fieldnames = ['shot_num','timestamp','yaw','pitch','velocity','hit','extras']
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE,'a',newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(shot_data)
