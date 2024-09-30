"""
Task 2. Implement a program to check a given point (x1, y1) belongs to the rectangle
(x, y, w, and h). Notice that, (x, y) represents the location of the upper left corner, and
w, h are the width and the height of a given rectangle.
"""

rec = [2, 2, 4, 3] # khai bao HCN bang mang
def checkPoint(x, y):
    xmax= rec[0]+rec[2]
    ymin= rec[1]-rec[3]
    if (rec[0] <= x <= xmax and ymin <= y <= rec[1]):
        print("The point belongs to the rectangle")
    else:
        print("The point dont belong to the rectangle")
checkPoint(3,1)
checkPoint(1,1)