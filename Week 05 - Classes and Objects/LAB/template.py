"""
RECORD CHECK  -  my version
===========================

Name  :Aymen Abdul Rahiman
Lane  :Cyber 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =========================================================================
# 1. CLASS
# =========================================================================

class Record:
    """Represents a security log record with source IP, failed logins, and total attempts."""
    over_limit_count = 0  

    def __init__(self, label, value, limit):
        """Initialize label (source IP), value (failed logins), and limit (total attempts)."""
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        """Return failed logins as a percentage of total attempts."""
        return (self.value / self.limit) * 100

    def status(self):
        """Return OVER LIMIT, WARNING, or OK based on failure percentage."""
        p = self.percent()
        if p >= 100:
            return "OVER LIMIT"
        elif p >= 90:
            return "WARNING"
        else:
            return "OK"


# =========================================================================
# 2. RECORDS
# =========================================================================

def load_records(path):
    """Read label,value,limit lines from a file and return a list of Record objects."""
    records = []
    with open(path, "r") as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

try:
    records = load_records("records_sample.txt")
except FileNotFoundError:
    records = [
        Record("10.0.0.5", 12.0, 400.0),
        Record("10.0.0.9", 95.0, 100.0),
        Record("10.0.0.12", 45.0, 100.0)
    ]


# =========================================================================
# 3. OUTPUT
# =========================================================================

for record in records:
    print()
    print("=" * 34)
    print(f"RECORD CHECK - {record.label}")
    print("=" * 34)

    free = record.limit - record.value
    p = record.percent()
    stat = record.status()

    if stat == "OVER LIMIT":
        Record.over_limit_count += 1

    print(f"Failed         : {record.value:8.2f}")
    print(f"Total          : {record.limit:8.2f}")
    print(f"Free           : {free:8.2f}")
    print(f"Percent        : {p:7.2f} %")
    print(f"Status         : {stat:>8}")

    print("=" * 34)

print(f"\nTotal OVER LIMIT records: {Record.over_limit_count}")


