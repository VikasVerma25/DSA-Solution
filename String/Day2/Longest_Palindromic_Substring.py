# Write a function that, given a string, returns its longest palindromic 
# substring. A palindrome is defined as a string that's written the same forward 
# and backward. Note that single-character strings are palindromes. You can 
# assume that there will only be one longest palindromic substring.

# O(n^2) time, O(n) space
def longestPalindrome(string):
    if checkPalindrome(string):
        return string
    substring = []
    append = substring.append
    # get all substrings
    for i in range(len(string)):
        for j in range(i,len(string)):
            append(string[i:j+1])    
    longest = ''    
    for current in substring:
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