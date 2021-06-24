# Write a function that takes in a list of numbers and returns a dictionary 
# containing the following statistics about the numbers: the mean, median, 
# mode, sample variance, sample standard deviation, and 95% confidence 
# interval for the mean. 
# Note that: 
# a. You can assume that the given list contains a large-enough number of 
#    samples from a population to use a z-score of 1.96. 
# b. If there's more than one mode, your function can return any of them. 
# c. You shouldn't use any libraries. 
# d. Your output values will automatically be rounded to the fourth 
#    decimal.

# Sample Input:
# input_list = [2,1,3,4,4,5,6,7]
# Sample Output:
# {
#     "mean": 4.0,
#     "median": 4.0,
#     "mode": 4.0,
#     "sample_variance": 4.0,
#     "sample_standard_deviation": 2.0,
#     "mean_confidence_interval":[2.6141, 5.3859],
# }

def stats(inputList):
    inputlen = len(inputList)
    answer = {'mean':None,"median":None,"mode":None,
        "sample_variance":None,"sample_standerd_deviation":None,
        "mean_confidence_interval":None}
    mean = answer["mean"] = round(sum(inputList)/inputlen, 4)
    modedict = dict()
    squaresum = 0
    for n in inputList:
        squaresum += (n - mean)**2
        modedict[n] = 1 if n not in modedict else modedict[n]+1
    answer["sample_variance"] = round(squaresum/(inputlen-1), 4)
    sd = answer["sample_standerd_deviation"] = round(answer["sample_variance"]**0.5, 4)
    max = modedict[inputList[0]]
    for i in modedict:
        if modedict[i] > max:
            max = modedict[i]
            answer["mode"] = i
    answer["median"] = round((answer["mode"] + 2*answer["mean"])/3, 4)
    answer["mean_confidence_interval"] = [round(mean-1.96*sd/(inputlen**0.5),4),round(mean+1.96*sd/(inputlen**0.5),4)]
    return answer
print(stats([2,1,3,4,4,5,6,7]))