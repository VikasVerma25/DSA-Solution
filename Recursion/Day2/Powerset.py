# Write a function that takes in an array of unique integers and returns its 
# powerset. The powerset P(X) of a set X is the set of all subsets of X.
# For example, the powerset of [1,2] is [[], [1], [2], [1,2]].
# Note that the sets in the powerset do not need to be in any particular 
# order.

''' [1,2,3]                          
                                           []                     add 1 or don't add
                                        /      \                                                                       
                                   [1]              []            add 2 or don't add
                                 /    \           /     \
                             [1,2]     [1]      [2]      []       add 3 or don't add
                             /  \      / \      /  \     / \
 powerset =>          [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []    O(n*2^n) time   
'''

def powerset(myset, anslist = [], subset = [], i = 0):
    # if reached last element of set then append subset to anslist
    if i == len(myset):
        anslist.append(subset)
        return
    # add next index element to subset
    powerset(myset, anslist, subset+[myset[i]], i+1)
    # not adding next element index to subset
    powerset(myset, anslist, subset, i+1)
    return anslist

print(powerset([1,2,3]))
