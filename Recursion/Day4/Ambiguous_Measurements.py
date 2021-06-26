# This problem deals with measuring cups that are missing important measuring labels. 
# Specifically, a measuring cup only has two measuring lines. a Low (L) line and a High (H) 
# line. This means that these cups can't precisely measure and can only guarantee that the 
# substance poured into them will be between the Land H line. For example, you might have 
# a measuring cup that has a Low line at 400ml and a high line at 435ml. This means that 
# when you use this measuring cup, you can only be sure that what you're measuring is 
# between 400ml and 435ml. You're given a list of measuring cups containing their low and 
# high lines as well as one low integer and one high integer representing a range for a target 
# measurement. Write a function that returns a Boolean representing whether you can use 
# the cups to accurately measure a volume in the specified [Low, high] range (the range is 
# inclusive).
# Note that:
# • Each measuring cup will be represented by a pair of positive integers [L, H]. where 0 <= L <= H
# • You'll always be given at least one measuring cup, and the low and high input 
# parameters will always satisfy the following constraint: 0 <= Low <= high.
# • Once you've measured some liquid, it will immediately be transferred to a larger bowl 
# that will eventually (possibly) contain the target measurement.
# • You can't pour the contents of one measuring cup into another cup.

def helpmeasure(cups, low, high, l=0, h=0):
    # measured
    if low <= l < h <= high:
        return True
    # can not measure
    if l > high or h > high:
        return False
    # keep measuring with cups, return true when condition satisfied 
    for cup in cups:
        if helpmeasure(cups, low, high, l+cup[0] , h+cup[1]):
            return True
    return False

def measure(cups, low, high):
    # sort the cups in descending  order
    cups.sort(key = lambda x: x[1], reverse = True)
    return helpmeasure(cups, low, high)

print(measure([ [200,210],[450,465],[800,850] ], 2100, 2300))
