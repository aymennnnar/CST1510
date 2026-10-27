"""
RECORD CHECK  -  Cyber Lane 
===========================

Name  :Aymen Abdul Rahiman
Lane  :Cyber 
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


source_ip = input("Source IP      : ")
failed_logins = float(input("Failed logins  : "))
total_attempts = float(input("Total attempts : "))

passed_logins = total_attempts - failed_logins
percent_failed = (failed_logins / total_attempts) * 100

print("=" * 38)
print(f"  SECURITY CHECK  -  {source_ip}")
print("=" * 38)
print(f"  Failed logins   : {failed_logins:>10.2f}")
print(f"  Total attempts  : {total_attempts:>10.2f}")
print(f"  Passed logins   : {passed_logins:>10.2f}")
print(f"  Percent failed  : {percent_failed:>10.1f} %")
print("=" * 38)