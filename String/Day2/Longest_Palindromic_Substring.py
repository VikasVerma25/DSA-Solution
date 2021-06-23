# Write a function that, given a string, returns its longest palindromic 
# substring. A palindrome is defined as a string that's written the same forward 
# and backward. Note that single-character strings are palindromes. You can 
# assume that there will only be one longest palindromic substring.

def longestPalindrome(string):
    substring = []
    append = substring.append
    # get all substrings
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            append(string[i:j])
    
    longest = ''
    for current in substring:
        start = 0
        end = len(current)-1
        ispal = True
        while start < end:
            if current[start] != current[end]:
                ispal = False
                break
            end -= 1
            start += 1
        if ispal and len(current)>len(longest):
            longest = current
    return longest

print(longestPalindrome("abaxyzzyxf"))