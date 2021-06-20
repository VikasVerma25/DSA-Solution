# Problem Statement:
#  Write a function that takes in an array of unique integers and returns an
#  array of all permutations of those integers in no particular order.
#  If the input array is empty, the function should return an empty array

def permutations(myarray, k = 0, result = []):
    # when reached to end of a iteration, append the array
    if k == len(myarray):
        # append adds the reference of object so make a copy otherwise all elements will be same
        result.append(myarray.copy())

    for i in range(k, len(myarray)):
        # swapping elements
        myarray[i], myarray[k] = myarray[k], myarray[i]
        # move to next index 
        permutations(myarray, k+1, result)
        # get back to previous state of array
        myarray[i], myarray[k] = myarray[k], myarray[i]
    return result

print(permutations([1,2,3,4]))
