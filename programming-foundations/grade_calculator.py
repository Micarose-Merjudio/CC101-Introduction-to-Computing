# grade_calculator.py
# Author: Mica Rose D. Merjudio, BSCS 1-1
# Date: November 12, 2026
# Purpose: Computes the midterm rating from laboratory and lecture grades.

lab = float(input("Laboratory grade: "))
lecture = float(input("Lecture grade: "))
rating = lab * 0.65 + lecture * 0.35
print(f"Midterm rating: {rating:.2f}")
