# Write a function that takes in a string of words separated by one or more 
# whitespaces and returns a string that has these words in reverse order. For 
# example, given the string "tim is great", your function should return "great is 
# tim". For this problem, a word can contain special characters, punctuation, 
# and numbers. The words in the string will be separated by one or more 
# whitespaces, and the reversed string must contain the same whitespaces as 
# the original string. For example, given the string "whitespaces 4" you would 
# be expected to return "4 whitespaces". Note that you're not allowed to to 
# use any built-in split or reverse methods/functions. However, you are 
# allowed to use a built-in join method/function. Also note that the input 
# string isn't guaranteed to always contain words.

# Sample Input:
# string = "Demo is the best!"
# Sample Output:
# best! the is Demo

# O(n) time, O(n) space
# reversing complete string and reversing each word
def reverse(string):
    if " " not in string:
        return string
    tempword = []
    answer = ""
    # start from end 
    for i in range(len(string)-1,-1,-1):        
        # if space is found add tempword to answer, also add the space and empty tempword
        if string[i] == " ":
            answer += "".join(tempword)+string[i]
            tempword = []            
        # if character is not a space add it to beginning of tempword (to get reversed word)
        else:
            tempword.insert(0,string[i])
        # when reached last character which is not a space
        if i == 0 and string[i] != " ":
            answer += "".join(tempword)
    return answer
print(reverse(" Demo   is the best!"))