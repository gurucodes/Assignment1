__author__ = 'Gurdev'
"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        test = int(input("Enter integer:"))
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)


