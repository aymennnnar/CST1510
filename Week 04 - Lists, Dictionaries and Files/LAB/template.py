"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =========================================================================
# FUNCTIONS
# =========================================================================

def check_record(value, limit):
    """Calculate the difference (remaining allowance) and percentage."""
    free = limit - value
    percent = (value / limit) * 100
    return free, percent

def status_of(percent):
    """Return status based on failed login percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def print_report(label, value, limit):
    """Print a bordered report for a given IP record."""
    free, percent = check_record(value, limit)
    status = status_of(percent)
    
    print("=" * 40)
    print(f"RECORD CHECK - {label}")
    print("-" * 40)
    print(f"Failed         : {value:8.2f}")
    print(f"Total          : {limit:8.2f}")
    print(f"Free           : {free:8.2f}")
    print(f"Percent        : {percent:7.2f} %")
    print(f"Status         : {status:>8}")
    print("=" * 40)

def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts safely."""
    try:
        records = []
        with open(path, "r") as f:
            for line in f:
                label, value, limit = line.strip().split(",")
                records.append({
                    "label": label,
                    "value": float(value),
                    "limit": float(limit)
                })
        return records
    except FileNotFoundError:
        print(f"Notice: File '{path}' not found. Starting with an empty records list.")
        return []


# =========================================================================
# STORE
# =========================================================================

# Attempt to load from records.txt (Expected format: source_ip,failed_logins,total_attempts)
records = load_records("records.txt")

# Fallback default records if records.txt hasn't been created yet
if not records:
    records = [
        {"label": "10.0.0.5", "value": 12.0, "limit": 400.0},
        {"label": "10.0.0.9", "value": 95.0, "limit": 100.0},
        {"label": "10.0.0.12", "value": 45.0, "limit": 100.0}
    ]


# =========================================================================
# PROCESS + OUTPUT
# =========================================================================

over_limit_count = 0
results_lines = []

for record in records:
    print_report(record["label"], record["value"], record["limit"])
    _, percent = check_record(record["value"], record["limit"])
    status = status_of(percent)
    
    if status == "OVER LIMIT":
        over_limit_count += 1
        
    results_lines.append(f"{record['label']},{status}")

# Write results out to results.txt
with open("results.txt", "w") as f:
    for line in results_lines:
        f.write(line + "\n")

print(f"\nTotal OVER LIMIT records: {over_limit_count}")