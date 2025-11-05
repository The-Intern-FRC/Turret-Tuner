import sys
from analysis import analyzer

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/main.py /path/to/logs_or_flashdrive")
        sys.exit(1)
    path = sys.argv[1]
    analyzer.run_analysis(path)
