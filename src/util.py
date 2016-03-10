import os
import math



DEFAULT_COMMENT = "#"



def isEndOfFile(file):
    return (file.tell() == os.fstat(file.fileno()).st_size)

def nextMeaningLine(file, commentString=DEFAULT_COMMENT):
    while (not isEndOfFile(file)):
        res = file.readline().strip()
        if (res.startswith(commentString)):
            continue
        elif (res == "\n" or res == ""):
            continue
        else:
            return res
    raise Exception("No useful string found in the file " + file.name)

def vectorLength(vector):
    res = 0
    for i in xrange(len(vector)):
        res += math.pow(vector[i], 2)
    return math.sqrt(res)

def vectorTimeScallar(vector, scallar):
    for i in xrange(len(vector)):
        vector[i] *= scallar

def lowestValue(a, b):
    if (a < b):
        return a
    else:
        return b

def biggestValue(a, b):
    if (a > b):
        return a
    else:
        return b

def radialBasisFunction(X, center):
    if (len(X) != len(center)):
        raise Exception("The dimension of the two input vectors is not the same")

    res = 0.
    for dim in xrange(len(X)):
        res += (X[dim] - center[dim]) **2

    return math.exp(res/2.)
