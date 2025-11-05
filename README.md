Turret Analysis & Predictive Firing System

This repository contains a full Python-based analysis pipeline for FRC turret data. It is designed to take AdvantageKit logs (or any exported logs from a flash drive), perform predictive firing analysis, calculate tuning suggestions, and generate comprehensive reports in PDF, TXT, and Jupyter notebook formats.

Features

- Log ingestion: Reads AdvantageKit logs or flash drive CSVs.
- Shot analysis: Computes yaw, pitch, exit velocity, and margins of error.
- Hit/miss tracking: Automatically records whether each shot hit or missed.
- Chronological shot numbering: Assigns unique numbers and timestamps to each shot.
- Duplicate detection: Avoids double-counting identical shots.
- Predictive analysis: Suggests optimal tuning parameters for drag, mass, area, and exit velocity.
- Visualization: Generates plots of shot performance, accuracy, and trends.
- Reports: Creates full TXT and PDF reports with all computed metrics.
- Jupyter integration: Comes with ready-to-run notebook templates for interactive exploration.
- Fully reproducible environment: Includes virtual environment setup with all dependencies.

Setup

1. Clone the repository (or open your Codespace).

2. Activate the virtual environment:

   source .venv/bin/activate

3. Install dependencies (if not already installed):

   pip install -r requirements.txt

Usage

1. Run analysis on logs:

   python src/main.py <path_to_logs>

   Example:

   python src/main.py data/raw

   This will:
   - Read all logs in data/raw
   - Deduplicate and assign chronological shot numbers
   - Run predictive firing analysis
   - Generate plots in reports/figures/
   - Output PDF and TXT reports in reports/

2. Run interactive Jupyter notebook:

   jupyter notebook

   Open notebooks/TurretAnalysis.ipynb for:
   - Interactive data exploration
   - Custom plotting
   - Step-by-step calculation review

3. Log shot results manually

   In Python, you can record whether a shot was a hit or miss:

   from analysis import turret_solver
   turret_solver.log_shot_result(True)  # True = hit, False = miss

Directory Structure

.
├── src/
│   ├── main.py             # Entry point
│   ├── analysis/           # Analysis modules
│   │   └── turret_solver.py
│   └── utils/              # Logging & helper utilities
├── data/
│   ├── raw/                # Raw AdvantageKit/flash drive logs
│   └── processed/          # Processed, deduplicated logs
├── reports/
│   ├── figures/            # Generated plots
│   ├── logs/               # System logs
│   └── analysis_report.pdf # Auto-generated reports
├── notebooks/
│   └── TurretAnalysis.ipynb
├── .venv/                  # Python virtual environment
├── requirements.txt
└── README.txt

Notes

- Only unique shots are analyzed; duplicates are ignored.
- All shots are assigned a chronological number and a timestamp.
- Analysis automatically accounts for all tunable variables: drag, mass, area, velocity, and launcher/target heights.
- Designed for manual triggering — plug in a flash drive or copy logs, then run the Python script.

Dependencies

- Python 3.10+
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter / Notebook
- ReportLab
- Tabulate

Created for FRC turret data analysis and predictive tuning.
