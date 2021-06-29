# Write a function that takes in a string made up of parentheses (( and )). The 
# function should return an integer representing the length of the longest 
# balanced substring with regards to parentheses. A string is said to be balanced 
# if it has as many opening parentheses as it has closing parentheses and if no 
# parenthesis is unmatched. Note that an opening parenthesis can't match a 
# closing parenthesis that comes before it, and similarly, a closing parenthesis 
# can't match an opening parenthesis that comes after it.

# Sampe Input:
# string = "(()))("
# Sample Ouput:
# 4

# O(n) time, O(1) space
def longestBalanced(string):
    open = 0
    close = 0
    longest = 0
    for i in range(len(string)):
        if string[i] == "(":
            open += 1 
        else:
            close += 1
        # check for longest and set open, close to 0    
        if close > open:
            if open+(close-1) > longest:
                longest = open+close-1
            open = close = 0
        # for last parentheses
        if i == len(string)-1:
            if open == close:
                if open+close > longest:
                    longest = open+close
            elif open > close:
                if 2*close > longest:
                    longest = 2*close
    return longest

print(longestBalanced("))(()))(((()))("))


