"""
Task 7. Implement a function called draw_pyramid(n) - This function takes
as an input one integer value n and then outputs on the
console a pyramid as in the figure below for example for
n=4:
//...X
//..XXX
//.XXXXX
//XXXXXXX
"""
def pyramid(n):
    c=""
    l=""
    for i in range(n):
        for j in range(n-i):
            l+=" "
        for k in range( (i+1)*2-1):
            c+="X"
        print(l+c)
        l = ""
        c = ""
pyramid(4)
