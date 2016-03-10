from ProblemInstance import ProblemInstance
from util import *
import matplotlib.pyplot as plt
import math
from cupshelpers.ppds import normalize





def plotSample(pbInstance, falseClassified):
    positiveSample  = pbInstance.getSampleFeature(sampleValue=1)
    negativeSample  = pbInstance.getSampleFeature(sampleValue=-1)
    SVM             = pbInstance.getSVM()

    plt.plot(positiveSample[0], positiveSample[1],  '+', color='red',   label='Positive samples', mew=2, ms=10)
    plt.plot(negativeSample[0], negativeSample[1],  '_', color='blue',  label='Negative samples', mew=2, ms=10)
    plt.plot(SVM[0],            SVM[1],             '*', color='cyan',  label='Svm', ms=10)
    plt.plot(falseClassified[0], falseClassified[1], '^', color='black',  label='False classified')

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
    fc = [[] for d in xrange(pbInstance.getFeatureDimension())]
    isSeparable = pbInstance.isSeparableTrainingData(0, falseClassified=fc)
    if (isSeparable == True):
        print "The samples are separable"
    else:
        print "The samples are not separable.  The wrong classified points are:"
    plotSample(pbInstance, fc)



