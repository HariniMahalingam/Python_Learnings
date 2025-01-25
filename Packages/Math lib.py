import math

print("sin using math library", math.sin(45))
print("gcd using math library", math.gcd(20, 30))

#use of from and importing only specific libraries
from statistics import mean, median, mode

print("Mean from statistics library", mean([10, 20, 30, 40]))
print("Median from statistics library", median([10, 20, 30, 40]))
print("Mode from statistics library", mode([1, 2, 3, 4, 5, 5, 5, 1, 3]))
