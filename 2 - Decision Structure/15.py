"""
Make a Program that asks for the 3 sides of a triangle. The program should inform if the values can be a triangle.
Indicate, if the sides form a triangle, whether it is: equilateral, isosceles or scalene.
Tips:
Three sides form a triangle when the sum of any two sides is greater than the third;
Equilateral Triangle: three equal sides;
Isosceles Triangle: any two equal sides;
Scalene Triangle: three different sides;
"""

side1 = float(input('Side 1: '))
side2 = float(input('Side 2: '))
side3 = float(input('Side 3: '))

if side1 == side2 == side3 and side1 == side3 == side2:
    print('Equilateral triangle')
elif side1 == side2 or side2 == side3 or side1 == side3:
    print('Isosceles triangle')
elif side1 != side2 != side3 and  side1 != side3 != side2:
    print('Scalene triangle')

