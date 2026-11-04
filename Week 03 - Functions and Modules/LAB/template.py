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

def status_of(percent):
    """Return status based on failed login percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

def check(value, limit):
    """Calculate difference and percentage for log attempts."""
    diff = limit - value
    percent = (value / limit) * 100
    return diff, percent

def print_report(source_ip, failed_logins, total_attempts):
    """Print a bordered report for a given IP record."""
    diff, pct = check(failed_logins, total_attempts)
    free = diff  # remaining attempts/allowance
    status = status_of(pct)
    
    print("=" * 40)
    print(f"RECORD CHECK - {source_ip}")
    print("-" * 40)
    print(f"Failed         : {failed_logins:8.2f}")
    print(f"Total          : {total_attempts:8.2f}")
    print(f"Remaining      : {free:8.2f}")
    print(f"Percent        : {pct:7.2f} %")
    print(f"Status         : {status:>8}")
    print("=" * 40)

def main():
    print("Running Security Audit Mini-Project...")
    count = 0
    
    while True:
        source_ip = input("Enter source IP (or type 'quit' to exit): ")
        if source_ip.lower() == 'quit':
            break
            
        try:
            failed_logins = float(input("Enter failed logins: "))
            total_attempts = float(input("Enter total attempts: "))
        except ValueError:
            print("Please enter valid numbers for logins and attempts.")
            continue
            
        print_report(source_ip, failed_logins, total_attempts)
        count += 1
        
    print(f"\nTotal records checked: {count}")

if __name__ == "__main__":
    main()