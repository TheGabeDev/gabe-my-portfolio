#Write a program that calculates the area of a regular polygon.
#You will need to use the math.tan and math.radians functions in the calculation.
#Write a program that prompts the user to input the number of sides (an int)
#and the side (a float).
#The program should display the area rounded to two decimal points.

import math

def main():
    
    number_sides = int(input('Enter the number of sides: '))
    side_length = float(input("Enter the side's length: "))

    print(f'{area(side_length, number_sides):.2f}')

def apothem(sideL, numSides):
    apothem = sideL / (2 * math.tan(math.radians(180 / numSides)))

    return apothem

def area(sideL, numSides):
    perimeter = numSides * sideL

    area = 0.5 * perimeter * apothem(sideL, numSides)

    return area

if __name__ == "__main__":
    main()

