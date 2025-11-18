import math

def paint_calc(height, width, coverage):
    area = height * width
    num_cans = math.ceil(area / coverage)
    print(f"You'll need {num_cans} cans of paint.")

# User input
height = int(input("Height of wall (m): "))
width = int(input("Width of wall (m): "))

# 1 can covers 5 square meters
coverage = 5

paint_calc(height, width, coverage)