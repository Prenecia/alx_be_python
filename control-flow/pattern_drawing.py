#!/usr/bin/python3

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Draw the pattern using nested loops
i = 0
while i < size:
    for j in range(size):
        print("*", end="")
    print()
    i += 1
