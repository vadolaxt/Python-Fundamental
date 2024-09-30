"""
Task 3. Implement a function to find the maximal integer number (m) for a given n
such that: 1 + 2 + ... + m < n.
"""

def findMax(n):
    sum=0
    count=0
    while(sum+count+1 < n):
        count+=1
        sum+=count
    print(count)

findMax(10)
findMax(12)
findMax(16)