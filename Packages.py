1.
# Definition of radius
r = 0.43

# Import the math package
import math 

# Calculate C
C = math.pi * 2 * r
# Calculate A
A = math.pi * (r ** 2)

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

2.
# Definition of radius
r = 192500

# Import radians function of math package
from math import radians 

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)


# Print out dist
print(dist)

