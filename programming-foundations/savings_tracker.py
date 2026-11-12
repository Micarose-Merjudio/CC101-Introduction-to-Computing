# savings_tracker.py
# Author: Mica Rose D. Merjudio, BSCS 1-1
# Date: November 12, 2026
# Purpose: Totals daily savings until 0 is entered using a while loop.

total_saved = 0.0
count = 0

amount = float(input("Savings today (0 to stop): "))
while amount != 0:
    total_saved += amount
    count += 1
    amount = float(input("Savings today (0 to stop): "))

if count > 0:
    print(f"Total saved in {count} days: PHP {total_saved:,.2f}")
else:
    print("No savings recorded.")
