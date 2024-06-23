#!/usr/bin/python3
# future_age_calculator.py

# Prompt user for current age
current_age = int(input("How old are you? "))

# Calculate future age
current_year = 2023
future_year = 2050
years_to_future = future_year - current_year
future_age = current_age + years_to_future

# Print the result
print(f"In {future_year}, you will be {future_age} years old.")
