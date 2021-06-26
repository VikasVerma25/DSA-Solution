# Write a function that takes in a string and returns its longest substring without 
# duplicate characters. You can assume that there will only be one longest 
# substring without duplication.

# Sample Input:
# string = "clementisacap"
# Sample Output:
# mentisac

def substring(string):
    # for storing elements with index
    elements = dict()
    start = 0
    longest = ""
    for i in range(len(string)):
        # when character is found in dictionary
        if string[i] in elements:
            # create a substring from start till this index (not including)
            subs = string[start:i]
            # set longest substring
            if len(subs) > len(longest):
                longest = subs
            # we have a new start = index value of already present character(previous) + 1
            newstart = elements[string[i]] + 1
            # delete all characters(keys) from dictionary which are before newstart
            for j in range(start, newstart):
                elements.pop(string[j])
            # new start index value that will be used for next subarray
            start = newstart
        # reaching last index, where character is not in dictionary
        elif i == len(string)-1:
            subs = string[start:i+1]
            if len(subs) > len(longest):
                longest = subs
        # add character to dictionary
        elements[string[i]] = i

    # return longest substring
    return longest

# print(substring("clementisacap"))
print(substring("clementisacap"))