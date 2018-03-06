#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?

import math

# Solved with combination where you can choose down steps, and a number of 40 choices must be made
g = 20
t = g * 2

result = math.factorial(t)/((math.factorial(g))*(math.factorial(t-g)))


print(int(result))

