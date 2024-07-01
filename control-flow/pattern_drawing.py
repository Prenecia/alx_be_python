#!/usr/bin/python3

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
for _ in range(size):
    for _ in range(size):
        print("*", end="")
    print()
