# Write a function that takes in a non-empty string and that returns a Boolean
# representing whether the string is a palindrome. A palindrome is defined as a 
# string that's written the same forward and backward. Note that single-character 
# strings are palindromes.


def check(string):
    end = len(string)-1
    for front in range(len(string)//2):
        if string[front] != string[end]:
            return "false"
        end -= 1 
    return "true"

print(check("abcdcba"))