"""
RECORD CHECK  -  my version
===========================

Name  :Aymen Abdul Rahiman
Lane  :Cyber 
Date  :03-10-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


over_limit_count = 0

while True:
    label = input("Enter label/name (or 'quit' to exit): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter used value: "))
    limit = float(input("Enter total limit: "))


    difference = limit - value
    percent = (value / limit) * 100 if limit != 0 else 0.0


    if percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 34)
    print(f"RECORD CHECK — {label}")
    print("=" * 34)
    print(f"Used    : {value:10.2f}")
    print(f"Total   : {limit:10.2f}")
    print(f"Free    : {difference:10.2f}")
    print(f"Percent : {percent:9.2f} %")
    print(f"Status  : {status:>10}")
    print("=" * 34)
    print()

print(f"\nSession ended. Total records marked OVER LIMIT: {over_limit_count}")