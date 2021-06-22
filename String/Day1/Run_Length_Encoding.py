# Write a function that takes in a non-empty string and returns its run-length 
# encoding. From Wikipedia, "run-length encoding is a form of lossless data 
# compression in which runs of data are stored as a single data value and count, 
# rather than as the original run." For this problem, a run of data is any sequence 
# of consecutive, identical characters. So, the run "AAA" would be run-lengthencoded as "3A". To make things more complicated, however, the input string 
# can contain all sorts of special characters, including numbers. And since encoded 
# data must be decodable, this means that we can't naively run-length-encode 
# long runs. For example, the run "AAAAAAAAAAAA" (12 A’s), can't naively be 
# encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA"
# or "1AA". Thus, long runs (runs of 10 or more characters) should be encoded in 
# a split fashion; the aforementioned run should be encoded as "9A3A".

# Sample Input:
# string = AAAAAAAAAAAAABBCCCCDD
# Sample Output:
# 9A4A2B4C2D

def runlength(string):
    ch = string[0]
    count = 0
    result = ""
    for i in range(len(string)):
        # if character is being matched increase count
        if ch == string[i]:
            count += 1
        else:
            # add the result, set ch to current character and count to 1
            if count%9 == 0: result += f"9{ch}"*(count//9)
            else: result += f"9{ch}"*(count//9) + f"{count%9}{ch}"
            count = 1
            ch = string[i]
        if i == len(string)-1:
            # when it reaches last add to the result
            if count%9 == 0: result += f"9{ch}"*(count//9)
            else: result += f"9{ch}"*(count//9) + f"{count%9}{ch}"
    return result

print(runlength("AAAAAAAAAAAAABBCCCCDDVFQQQQ$$%^^^444999"))

            

        
