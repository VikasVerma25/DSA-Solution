# You're given two positive integers representing the height of a staircase and 
# the maximum number of steps that you can advance up the staircase at a 
# time. Write a function that returns the number of ways in which you can 
# climb the staircase.
# For example, if you were given a staircase of height = 3 and maxSteps = 2 you 
# could climb the staircase in 3 ways. You could take 1 step, 1 step, then 1 step, 
# you could also take 1 step, then 2 steps , and you could take 1 step, then 2 
# steps , and you could take 2 steps, then 1 step

'''
for maxsteps=2, height=2| for maxsteps=2, height=3 | for maxsteps=2, height=4
1,1                     | 1,1,1                    | 1,1,1,1
2                       | 1,2                      | 1,1,2
                        | 2,1                      | 1,2,1
                        |                          | 2,2,1
                        |                          | 2,2
so, no. of ways to reach height=5 ==> ways(5) = ways(4) + ways(3)
=> ways(h) = ways(h-1) + ways(h-2)

for any no. of allowed steps, ex. (1, 2, 4, 6)
ways(h) = ways(h-1) + ways(h-2) + ways(h-4) + ways(h-6)
'''

def staircase_ways(height, maxsteps):
    if height == 0:
        return 1
    total = 0
    for i in range(1, maxsteps+1):
        if height-i >= 0:
            total += staircase_ways(height-i, maxsteps)
    return total

print(staircase_ways(4, 2))


# better way without recursion
# dynamic programming
def staircase_ways(height, maxsteps):
    # base case
    if height == 0:
        return 1
    no_ways = [1]
    # for a height of staircase
    for i in range(1, height+1):
        total = 0
        # for all allowed steps
        for j in range(1, maxsteps+1):
            if i-j >= 0:
                total += no_ways[i-j]
        # add the number of ways to the list (remembering)
        no_ways.append(total)
    # return number of ways for given height
    return no_ways[height]

print(staircase_ways(4, 2))
