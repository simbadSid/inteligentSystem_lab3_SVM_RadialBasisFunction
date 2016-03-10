from ProblemInstance import ProblemInstance
from util import *
import matplotlib.pyplot as plt
import math
from cupshelpers.ppds import normalize





def plotSampleAndDiscriminant(pbInstance):
    positiveSample = pbInstance.getPositiveSample()
    negativeSample = pbInstance.getNegativeSample()
    plt.plot(positiveSample[0], positiveSample[1], '+', color='red',  label='Positive samples', mew=5, ms=10)
    plt.plot(negativeSample[0], negativeSample[1], '_', color='blue',  label='Negative samples', mew=5, ms=10)

    print positiveSample[1]
    print negativeSample[1]

    plt.plot(-1, -1)
    plt.plot(10, 10)
    plt.plot()
    plt.grid()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    pbInstance = ProblemInstance()
    pbInstance.parseProblemInstance(normalizeData=False)

    plt.figure()
    plotSampleAndDiscriminant(pbInstance)



