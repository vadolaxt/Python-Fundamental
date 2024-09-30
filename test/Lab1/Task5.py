"""
Task 5. Implement a function called taxi_fare that computes the fare of a taxi ride
based on two inputs: the distance in kilometers (d) and the amount of waiting time in
minutes (t). The fare is calculated like this:
− the first km is 10,000 VND
− every additional km is 5,000 VND
− over 10km, each additional km is 2,000 VND
− and every minute of waiting is 1,000 VND.
"""
def taxi_fare(d, t):
    sum=0
    fee=0
    for i in range(0,d+1):
        if(d<=1):
            fee=10000
            sum+=fee
        elif(d>1 and d<=10):
            fee=5000
            sum+=fee
        else:
            fee=1000
            sum+=fee
    return sum +t*1000

print(taxi_fare(3,1))
print(taxi_fare(20,5))
print(taxi_fare(8,3))
