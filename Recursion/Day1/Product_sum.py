# Problem Statement:
#  Write a function that takes in a "special" array and returns its product sum.
#  A "special" array is a non-empty array that contains either integers or other
#  "special" arrays. The product sum of a "special" array is the sum of its
#  elements, where "special" arrays inside it are summed themselves and then
#  multiplied by their level of depth.
#  The depth of a "special" array is how far nested it is. For instance, the
#  depth of []is 1; the depth of the inner array in
#  [[]] is 2; the depth of the innermost array in
#  [[[]]] is 3.
#  Therefore, the product sum of [x, y] is x + y; the
#  product sum of [x, [y, z]] is x + 2 * (y + z); the
#  product sum of [x, [y, [z]]] is x + 2 * (y + 3z)

result = 0
# a, [b, [c, [d]]] = 1*a + 1*2*b + 1*2*3*c + 1*2*3*4*d
def product_sum(special_array, multiplyer=1):
    global result
    # take each item of the current array
    for item in special_array:
        # if item is not a integer object then change multiplyer and do recursion
        if not isinstance(item, int):            
            product_sum(item, multiplyer*(multiplyer+1))
        # if it is integer then add to result after multiplying with current multiplyer
        else:
            result += (multiplyer*item)
    return result

print(product_sum([5,2,[7,-1],3,[6,[-13,8],4]]))