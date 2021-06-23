# Write a function that takes in an array of strings and groups anagrams 
# together. Anagrams are strings made up of exactly the same letters, where 
# order doesn't matter. For example, "cinema" and "iceman" are anagrams; 
# similarly, "foo" and "ofo" are anagrams. Your function should return a list of 
# anagram groups in no particular order.

# Sample Input:
# words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
# Sample Output:
# [["yo","oy"], ["flop","olfp"], ["act","tac","cat"], ["foo"]]

# O(m*n*logn) time, O(mn) space where m is number of words and n is length of longest word
def group(words):
    group = dict()
    for word in words:
        # sort the word and 
        key = "".join(sorted(word))  # sorted into list and converted to string
        # add key-word or append the word for key (if already there) to dictionary
        if key in group:
            group[key].append(word)
        else:
            group[key] = [word]
    return list(group.values())

print(group(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))