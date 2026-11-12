# sum_to_n.py
# Author: Mica Rose D. Merjudio, BSCS 1-1
# Date: November 12, 2026
# Purpose: Computes the sum of numbers from 1 to n using a for loop.

n = int(input("Enter a positive whole number n: "))

total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"Sum of 1 to {n} = {total_sum}")
