import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from utils import logger

def read_logs(path):
    path = Path(path)
    all_logs = []
    for file in path.glob("*.csv"):
        try:
            df = pd.read_csv(file)
            all_logs.append(df)
        except Exception as e:
            print(f"Warning: failed to read {file}: {e}")
    if not all_logs:
        return pd.DataFrame()
    combined = pd.concat(all_logs, ignore_index=True)
    combined['timestamp'] = pd.to_datetime(combined['timestamp'])
    combined = combined.drop_duplicates(subset=['yaw','pitch','velocity','timestamp'])
    combined = combined.sort_values('timestamp').reset_index(drop=True)
    combined['shot_num'] = np.arange(1,len(combined)+1)
    return combined

def generate_txt_report(df, filename="reports/analysis_log.txt"):
    with open(filename,'w') as f:
        f.write("Turret Shot Analysis Report\n")
        f.write(f"Generated: {pd.Timestamp.now()}\n\n")
        for _, row in df.iterrows():
            f.write(f"Shot {row['shot_num']}: Timestamp={row['timestamp']}, Yaw={row['yaw']:.3f}, Pitch={row['pitch']:.3f}, Velocity={row['velocity']:.2f}, Hit={row['hit']}\n")

def generate_pdf_report(df, filename="reports/analysis_log.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica",10)
    c.drawString(50,height-50,"Turret Shot Analysis Report")
    c.drawString(50,height-65,f"Generated: {pd.Timestamp.now()}")
    y = height - 90
    for _, row in df.iterrows():
        line = f"Shot {row['shot_num']}: Timestamp={row['timestamp']}, Yaw={row['yaw']:.3f}, Pitch={row['pitch']:.3f}, Velocity={row['velocity']:.2f}, Hit={row['hit']}"
        c.drawString(50,y,line)
        y -= 15
        if y < 50:
            c.showPage()
            c.setFont("Helvetica",10)
            y = height - 50
    c.save()

def generate_plots(df):
    fig_dir = Path("reports/figures")
    fig_dir.mkdir(parents=True, exist_ok=True)
    
    # Velocity distribution
    plt.figure()
    sns.histplot(df['velocity'], kde=True)
    plt.title("Velocity Distribution")
    plt.savefig(fig_dir/"velocity_distribution.png")
    
    # Pitch distribution
    plt.figure()
    sns.histplot(df['pitch'], kde=True)
    plt.title("Pitch Distribution")
    plt.savefig(fig_dir/"pitch_distribution.png")
    
    # Yaw distribution
    plt.figure()
    sns.histplot(df['yaw'], kde=True)
    plt.title("Yaw Distribution")
    plt.savefig(fig_dir/"yaw_distribution.png")
    
    # Hit/miss pie
    plt.figure()
    df['hit'].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Hit/Miss Ratio")
    plt.savefig(fig_dir/"hit_miss_ratio.png")
    
    plt.close('all')

def run_analysis(path):
    df = read_logs(path)
    if df.empty:
        print("No logs found.")
        return
    generate_txt_report(df)
    generate_pdf_report(df)
    generate_plots(df)
    print(f"✅ Analysis complete. {len(df)} shots processed. Reports and plots saved.")
