# buggy_average.py
# Author: Mica Rose D. Merjudio, BSCS 1-1
# Date: November 12, 2026
# Purpose: Debugged quiz-average program that computes average and displays pass/fail status.

count = 1
total = 0

while count <= 3:
    score = float(input("Enter score: "))
    total = total + score
    count = count + 1

average = total / 3

if average >= 75:
    print("PASSED")
else:
    print("FAILED")

print(f"Average: {average:.2f}")
