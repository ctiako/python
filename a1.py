# CS 305 Unit 1: Assignment.
# By Cyrille Tekam Tiako
# 16 Aug 2024

import math

# 1. Rectangle Area Functiondefrectangle_area(width, height=None):

def rect_area(width,height=None):
    if height is None:
        height = width
    return width * height


# 2. Lambda Function for Circle Area
circle_area = lambda radius: round(math.pi * radius ** 2, 5)

# 3. Collections / Comprehensions# Part 1: Perfect Squares
perfect_squares = tuple(x**2for x in range(1, 11))

# Part 2: Excluding Certain Values
exclusions = set(range(5, 50))
squares_set = set(perfect_squares) - exclusions

# 4. Generator Function for Perfect Squaresdefgen_squares(start, stop):

def generate_squares(start, stop):
    for i in range(start, stop):
        yield i ** 2

