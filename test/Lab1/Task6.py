"""
Task 6. Implement functions to evaluate values of the following Algebra problems:
1. S(n)=1-2+3-4+...+ ((-1)^(n+1) ).n , n>0
2. S(n)=1+1.2+1.2.3+...+1.2.3...n, n>0
3. S(n)=1^2+2^2+3^2+....+n^2 , n>0
4. S(n)=1+1/2+1/(2.4)+1/(2.4.6)+...+1/(2.4.6...2n), n>0
"""

def f1(n):
    sumF1=0;
    for i in range(1,n+1):
       if(i%2==0):
           sumF1+=i*-1
       else:
           sumF1+=i
    return sumF1
print(f1(3))
print(f1(8))
print("-----")

def f2(n):
    countF2=1
    tempF2=1
    sumF2=0
    for i in range(1,n+1):
        tempF2*=countF2
        sumF2+=tempF2
        countF2+=1
    return sumF2
print(f2(3))
print(f2(6))
print("-----")

def f3(n):
    sumF3 = 0
    for i in range(1,n+1):
       sumF3+=i**2
    return sumF3
print(f3(2))
print(f3(4))
print("-----")

def f4(n):
     sumF4=1
     tempF4=1
     for i in range(1,n): # range(start, end, step)
         tempF4*= (2*i)
         sumF4+= (1/tempF4)
     return sumF4
print(f4(1))
print(f4(4))
