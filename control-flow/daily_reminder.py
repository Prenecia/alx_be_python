#!/usr/bin/python3

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Provide a customized reminder
reminder = f"'{task}' is a {priority} priority task"
if time_bound.lower() == 'yes':
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

print("Reminder:", reminder)
