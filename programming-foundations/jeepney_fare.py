# jeepney_fare.py
# Author: Mica Rose D. Merjudio, BSCS 1-1
# Date: November 12, 2026
# Purpose: Computes jeepney fare based on distance and discount eligibility.

distance = int(input("Distance (km): "))
discount = input("Discount? (Y or N): ").strip().upper()

if distance <= 4:
    fare = 13.00
else:
    fare = 13.00 + (distance - 4) * 1.80

if discount == 'Y':
    fare = fare * 0.80

print(f"Fare: PHP {fare:.2f}")
