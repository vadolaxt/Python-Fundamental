"""
Task 4. Implement a function to find the n^th Fibonacci value
(Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...)
    F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1
F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 ...
0  1  1  2  3  5  8  13 21 34 55  89  144 233 ...
    − function: find_fibonacci
    − parameter: n.
    − Output: n^th Fibonacci value.
"""

def find_fibonacci(n):
    if n <= 1:
        return n
    else:
        return find_fibonacci(n - 1) + find_fibonacci(n - 2)

print(find_fibonacci(8))
print(find_fibonacci(1))
print(find_fibonacci(12))



