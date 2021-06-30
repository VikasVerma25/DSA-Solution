# Write a function that, given a string, returns its longest palindromic 
# substring. A palindrome is defined as a string that's written the same forward 
# and backward. Note that single-character strings are palindromes. You can 
# assume that there will only be one longest palindromic substring.
# Sample Input:
# string = abaxyzzyxf
# Sample Output:
# xyzzyx

# O(n^3) time, O(1) space
def longestPalindrome(string):
    if checkPalindrome(string):
        return string
    longest = ''
    # get all substrings
    for i in range(len(string)):
        for j in range(i,len(string)):
            current = string[i:j+1] 
            # check if the substring is palindrome
            # if it is palindrome and longer than previous palindrom then set longest to current
            if checkPalindrome(current) and len(current)>len(longest):
                longest = current  
    # return the longest palindrome
    return longest

def checkPalindrome(string):
    start = 0
    end = len(string)-1    
    while start <= end:
        if string[start] != string[end]:
            return False
        end -= 1
        start += 1
    return True

print(longestPalindrome("abaxyzzyxf"))

####### dynamic programming #######
# O(n^2) time, O(n^2) space
def longest(string):
    l = len(string)
    m = [[0 for i in range(l)]for j in range(l)]
    ans = ""
    for d in range(l):   # diagonal
        i = 0
        for j in range(d,l):
            if d == 0:
                m[i][j] = 1
            elif d == 1 and string[i] == string[j]:
                m[i][j] = 1
            else:
                if string[i] == string[j] and m[i+1][j-1] == 1:
                    m[i][j] = 1
            if m[i][j] == 1 and len(string[i:j+1]) > len(ans):
                ans = string[i:j+1]
            i += 1
    return ans
print(longest("abaxyzzyxf"))
            