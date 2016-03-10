from array import array
from util import *
import math
from matplotlib.mathtext import DELTA





SVM_defaultAlphaValue = 1



class ProblemInstance:
    # -----------------------------
    # Attributes
    # -----------------------------
    """
    trainingSample_feature     = [[]]        # Lecture notation: X:
    trainingSample_Value       = [[]]        # Lecture notation: Y:
    SVM_index                  = []
    """

    # -----------------------------
    # Builder
    # -----------------------------
    def parseProblemInstance(self, normalizeData=False, inputFileName = "../resource/input/parameter.txt"):
        file = open(inputFileName)

        # Init feature samples
        nbrSamples                  = int(nextMeaningLine(file))
        featureDimension            = int(nextMeaningLine(file))
        self.trainingSample_feature = []
        self.trainingSample_value   = []
        self.SVM_index              = []

        for sample in xrange(nbrSamples):
            y       = int(nextMeaningLine(file))
            vect    = []
            norm    = 0.
            self.trainingSample_value.append(y)
            for dim in xrange(featureDimension):
                xi      = int(nextMeaningLine(file))
                norm    += xi ** 2
                vect.append(xi)
            self.trainingSample_feature.append(vect)
            isSVM   = int(nextMeaningLine(file))
            if (isSVM == SVM_defaultAlphaValue):
               self.SVM_index.append(sample)
            if (normalizeData == True):
                norm = math.sqrt(norm)
                for dim in xrange(featureDimension):
                    vect[dim] /= norm
        file.close()

    # -----------------------------
    # Getter
    # -----------------------------
    def getNbrTrainingSample(self):
        return len(self.trainingSample_value)

    def getFeatureDimension(self):
        return len(self.trainingSample_feature[0])

    # Return the array M such as M[d] is the array of the d th dimension of samplea which value is given.
    # if sampleValue=None, all the samples are returnes
    def getSampleFeature(self, sampleValue=None):
        dimension   = self.getFeatureDimension()
        res         = [[] for i in xrange(dimension)]

        for i in xrange(self.getNbrTrainingSample()):
            if ((sampleValue != None) and (sampleValue != self.trainingSample_value[i])):
                continue
            X = self.trainingSample_feature[i]
            for d in xrange(dimension):
                res[d].append(X[d])
        return res

    def getSVM(self):
        dimension   = self.getFeatureDimension()
        res         = [[] for i in xrange(dimension)]

        for index in self.SVM_index:
            X = self.trainingSample_feature[index]
            for d in xrange(dimension):
                res[d].append(X[d])
        return res

    # -----------------------------
    # Local methods
    # -----------------------------
    def evalDiscriminant(self, X, w0):
        res = 0.
        for i in xrange(len(self.SVM_index)):
            index   = self.SVM_index[i]
            Xm      = self.trainingSample_feature[index]
            res     += self.trainingSample_value[index] * radialBasisFunction(X, Xm) + w0

        return res

    def isSeparableTrainingData(self, w0, falseClassified=None):
        res = True
        dim = self.getFeatureDimension()

        for i in xrange(self.getNbrTrainingSample()):
            X = self.trainingSample_feature[i]
            g = self.evalDiscriminant(X, w0)
            print "g = " + str(g)
            if ((g*self.trainingSample_value[i]) < 0):
                if (falseClassified == None):
                    return False
                else:
                    res = False
                    for d in xrange(dim):
                        falseClassified[d].append(X[d])

        return res
