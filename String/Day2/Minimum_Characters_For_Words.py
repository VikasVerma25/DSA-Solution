# Write a function that takes in an array of words and returns the smallest array 
# of characters needed to form all of the words. The characters don't need to be 
# in any particular order. For example, the characters ["y", "r", "o", "u"] are 
# needed to form the words ["your", "you", "or", "yo"]. Note: the input words 
# won't contain any spaces; however, they might contain punctuation and/or 
# special characters.

def minCharacters(wordarray):
    minchars = dict()
    for word in wordarray:
        # in every word, if count of a character is more than previous count, update the value
        for i in range(len(word)):
            count = word.count(word[i]) 
            if word[i] not in minchars or count > minchars[word[i]]:
                minchars[word[i]] = count 
    
    return [ key for key in minchars for i in range(minchars[key])]

print(minCharacters(["this", "that", "did", "deed", "them!", "a"]))