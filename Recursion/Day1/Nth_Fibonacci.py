# Problem Statement: 
# The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the 
# second number is 1 and the nth number is the sum of the (n - 1)th and (n - 2)th numbers. Write a 
# function that takes in an integer n and returns the nth Fibonacci number.

# Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = 0 and 
# F1= 1. For the purpose of this question, the first Fibonacci number is F0; therefore, getNthFib(1) is 
# equal to F0, getNthFib(2) is equal to F1, etc.

# Sample Input 
# n = 6
# Sample Output 
# 5  

def getNthFib(n):
    # base case (return 0 and 1 for n  equal to 1 and 2)
    if n == 1 or n == 2:
        return n-1
    # nth element is sum of (n-1)th and (n-2)th elements
    else:
        return getNthFib(n-1) + getNthFib(n-2)
    
print(getNthFib(int(input())))
