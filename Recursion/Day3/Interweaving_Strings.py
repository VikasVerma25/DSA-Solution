# Write a function that takes in three strings and returns a Boolean representing 
# whether the third string can be formed by interweaving the first two strings.
# To interweave strings means to merge them by alternating their letters 
# without any specific pattern. For instance, the strings "abc" and "123" can be 
# interwoven as "alb2c3", as "abc123", and as "ab1c23" (this list is 
# nonexhaustive). Letters within a string must maintain their relative ordering in 
# the interwoven string.

# Sample Input:
#  one = "abc"
#  two = "123"
#  three = "ab12c3"
# Sample Output:
#  true

# dynamic programming
# keep checking elements of one and three (1st check) & two and three (2nd check), if one and two have common
# characters then we may again need to check two and three (1st check) & one and three (2nd check). 
# we are adding the result (true or false) in the dict so that we can get the result if checking
# the same condition again.

mem = dict()
def interweaving(one, two, three, len1, len2, len3, p1=0, p2=0, p3=0):
        if p3 == len3:                
                return True if p2 == len2 and p1 == len1 else False
        key = f"{p1}*{p2}*{p3}"
        if key in mem:
                return mem[key]
        # when no elements in one to compare
        if p1 == len1:
                if two[p2]==three[p3]:
                        mem[key] = interweaving(one, two, three, len1, len2, len3, p1, p2+1, p3+1)
                else:
                        mem[key] = False
                return mem[key]
        if p2 == len2:
                if one[p1]==three[p3] :
                        mem[key] = interweaving(one, two, three, len1, len2, len3, p1+1, p2, p3+1)
                else:
                        mem[key] = False
                return mem[key]

        first = second = False
        if one[p1] == three[p3]:
                first = interweaving(one, two, three, len1, len2, len3, p1+1, p2, p3+1)
        if two[p2] == three[p3]:
                second = interweaving(one, two, three, len1, len2, len3, p1, p2+1, p3+1)
        mem[key] = first or second
        return first or second

# one = input()
# two = input()
# three = input()
# print(interweaving(one, two, three, len(one), len(two), len(three)))
print(interweaving('abc', 'abcd', 'ababcdc',3,4,7))

