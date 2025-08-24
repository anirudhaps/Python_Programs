#returning more than one value from a function

def getSumAvg(a,b):
    s = sum([a,b]) #sum() takes a list of numbers as an argument
    avg = s/2.
    return (s,avg)

print(getSumAvg(3,5)[0])
print(getSumAvg(3,5)[1])
