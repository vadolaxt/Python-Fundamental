"""
Task 1. Implement a function to input a, b, and c; then check whether these values are
a triangle. If yes, what is the type of the triangle?
− Isosceles Triangle: Two sides are equal
− Equilateral Triangle: Three sides are identical
− Scalene Triangle: All three sides are different
"""

def isTriangle(a, b, c):
    if(a<=1 or b<=1 or c<=1):
       print("Not a triangle")
    elif (a+b>c or a+c>b or b+c>a):
        if a==b==c:
            print("Equilateral Triangle")
        elif a==b or a==c or b==c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")

isTriangle(1,2,1)
isTriangle(0,0,0)
isTriangle(5,5,5)
isTriangle(5,5,2)
isTriangle(5,3,2)