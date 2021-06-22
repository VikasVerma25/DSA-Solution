# Write a function that takes in a string of lowercase English-alphabet letters and 
# returns the index of the string's first non-repeating character. 
# The first non-repeating character is the first character in a string that occurs only once. 
# If the input string doesn't have any non-repeating characters, your function should return -1.

# Sample Input:
# string = abcdcaf
# Sample Output:
# 1 
 
# O(n) time, O(1) space
def find(string):
    count = dict()
    # add characters with their count in the dictionary
    for c in string:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
    # if count of character is 1 then return the index
    for i in range(len(string)):
        if count[string[i]] == 1:
            return i
    return -1

print(find("abcdcaf"))