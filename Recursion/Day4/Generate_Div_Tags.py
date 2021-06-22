# Write a function that takes in a positive integer numberOfTags and returns a list of all the 
# valid strings that you can generate with that number of matched <div></div> tags.
# A string is valid and contains matched <div></div> tags if for every opening tag <div>, there 
# is a closing tag </div> that comes after the opening tag and that isn't used as a closing tag 
# for another opening tag. Each output string should contain exactly same numberOfTags 
# opening tags and numberOfTags closing tags.
# For example, given numberOfTags=2. the valid strings to return would be:
# [
# "<div></div><div></div>",
# "<div><div></div></div>"
# ]
# Note that the output strings don't need to be in any particular order.

'''
Add opening tag first (if we have remaining opening tags). 
> Then we can either add openning tag (if we have remaining opening tags)
> or clossing tag (if remaining clossing tag is less than opening tag)
'''

def generate(openingleft, clossingleft, prefix="", result=[]):
    if openingleft > 0:
        # prefix += "<div>"
        generate(openingleft-1, clossingleft, prefix+"<div>", result)
    if openingleft < clossingleft:
        # prefix += "</div>"
        generate(openingleft, clossingleft-1, prefix+"</div>", result)
    if clossingleft == 0:
        result.append(prefix)        
    return result

# numberOfTags = input("Enter no of tags: ")
# generate(numberOfTags, numberOfTags)
print(generate(3,3))
