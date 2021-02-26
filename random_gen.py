#!/usr/bin/env python3

# Generate random number

# Imports
import random

# Constants
MAX = 1000

def get_random(min, max):
    r = random.randint(min, max)
    return r

def get_rand_min():
    min = random.randint(1, MAX/2) # return value between 1 and MAX/2
    return min

def get_rand_max(min):
    max = random.randint(min, MAX) # value must be between min and MAX
    return max

def main():
    print() # blank line
    min = get_rand_min()
    print("Min = {}".format(min))
    max = get_rand_max(min)
    print("Max = {}".format(max))
    num = get_random(min, max)
    print("Random number between {} and {} is {}.".format(min, max, num))


# Main code

if __name__ == "__main__":
    main()
