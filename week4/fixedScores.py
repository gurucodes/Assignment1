__author__ = 'Gurdev'
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
def printScores(score):
    if score <= 0 or score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:

        print("Passable")
    else:
        print("Bad")


def main():
    score = float(input("Enter score: "))
    printScores(score)
main()

