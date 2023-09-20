import random

# For the range:
RANGE_LOWER_BOUND = 0
RANGE_UPPER_BOUND = 25

# For generating random numbers:
RAND_LOWER_BOUND = 0
RAND_UPPER_BOUND = 100

# For rounding:
ROUND_DIGITS = 2

# Initialize random number generator:
random.seed()

# Create an empty list for storing random numbers:
randNumArray = []

for i in range(RANGE_LOWER_BOUND, RANGE_UPPER_BOUND):
    # Generate random float between RAND_LOWER_BOUND and RAND_UPPER_BOUND, and round it to ROUND_NUM_DIGITS after the decimal:
    randomFloat = round(random.uniform(RAND_LOWER_BOUND, RAND_UPPER_BOUND), ROUND_DIGITS)
    # Stick it in an array:
    randNumArray.append(randomFloat)

# Find the largest number in the array:
largestNumber = max(randNumArray)

print(f'\nThe largest number in the array is {largestNumber}.\n{randNumArray}\n')