# You're given two non-empty strings: a big string and a small string. Write a 
# function that returns the smallest substring in the big string that contains all 
# of the small string's characters.
# Note that:
# The substring can contain other characters not found in the small string. The 
# characters in the substring don't have to be in the same order as they appear 
# in the small string. If the small string has duplicate characters, the substring 
# has to contain those duplicate characters (it can also contain more, but not 
# fewer). You can assume that there will only be one relevant smallest substring.

# Sample Input:
# bigString = "abcd$ef$axb$c$"
# smallString = "$$abf"
# Sample Output:
# f$axb$

def substring(big, small):
    # pointers
    left = -1
    right = -1
    ans = ""
    # for storing all character of small string with count
    required = dict()
    # for checking and matching elements with required
    found = dict()
    for ch in small:
        required[ch] = required[ch]+1 if ch in required else 1
        found[ch] = 0
    # for counting required characters
    matched = 0
    while True:
        flag1, flag2 = 0, 0
        # add required elements in found dictionary and increase matched value 
        while right < len(big)-1 and matched < len(small):
            right += 1
            if big[right] in required:
                found[big[right]] += 1
                if found[big[right]] <= required[big[right]]:
                    matched += 1
            flag1 = 1

        # remove elements and decrease matched value if it becomes less than required
        while left < right and matched == len(small):            
            left += 1            
            possible_ans = big[left:right+1]
            # change the ans if it is smaller
            if len(possible_ans) < len(ans) or ans == "":
                ans = possible_ans
            if big[left] in found:
                found[big[left]] -= 1
                if found[big[left]] < required[big[left]]:
                    matched -= 1
            flag2 = 1
        # break main loop if none of the two loops is entered
        if flag1 == 0 and flag2 == 0:
            break
    return ans

print(substring("abcd$ef$axb$c$", "$$abf"))
    
            
        

