# Given a non-empty string of lowercase letters and a non-negative integer 
# representing a key, write a function that returns a new string obtained by
# shifting every letter in the input string by k positions in the alphabet, where k
# is the key. Note that letters should "wrap" around the alphabet; in other 
# words, the letter z shifted by one returns the letter a

# Sample Input:
# string = xyz
# key = 2
# Sample Output:
# zab

# ord() returns ASCII value of character then we can increment to it 
# and again convert to character using chr()

def encryptor(string, key):
    key = key % 26
    # to store already encrypted character
    for i in range(len(string)):
        ascii = ord(string[i])
        ascii += key
        if ascii > 122:
            ascii = 96 + (ascii-122)
        string[i] = chr(ascii)        
    return "".join(string)

# string = input("string = ")
# key = int(input("key = "))
# print(encryptor(list(string), key))
print(encryptor(list("xyz"), 2))
