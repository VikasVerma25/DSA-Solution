# You're given a string of length 12 or smaller, containing only digits. Write a 
# function that returns all the possible IP addresses that can be created by 
# inserting three .s in the string. An IP address is a sequence of four positive 
# integers that are separated by .s, where each individual integer is within the 
# range 0 - 255, inclusive. An IP address isn't valid if any of the individual 
# integers contains leading 0s. For example, "192.168.0.1" is a valid IP address, 
# but "192.168.00.1" and "192.168.0.01" aren't, because they contain "00" and 
# 01, respectively. Another example of a valid IP address is "99.1.1.10"; 
# conversely, "991.1.1.0" isn't valid, because "991" is greater than 255. Your 
# function should return the IP addresses in string format and in no particular 
# order. If no valid IP addresses can be created from the string, your function 
# should return an empty list. Note: check out our Systems Design 
# Fundamentals on SystemsExpert to learn more about IP addresses!

def validIP(string, part="", ip="", answer=[], i=0, count = 0):
    strlen = len(string)
    # return back if part or string is not valid or we have more than 4 parts count
    if (len(part)>1 and part[0]=='0') or (part!="" and int(part)>255) or count>4 or strlen<4:
        return answer
    # adding part to ip
    if ip == "": ip += part
    else: ip += "."+part
    # add ip to answer if it reached length of string+3(dots)
    if len(ip) == strlen+3:
        answer.append(ip)
    # taking part of 1 character
    if strlen-i >= 1:
        validIP(string, string[i:i+1], ip, answer, i+1, count+1)
    # taking part of 2 characters
    if strlen-i >= 2:
        validIP(string, string[i:i+2], ip, answer, i+2, count+1)
    # taking part of 3 characters
    if strlen-i >= 3:
        validIP(string, string[i:i+3], ip, answer, i+3, count+1)
    return answer

print(validIP("1921680"))



