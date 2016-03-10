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
    trainingSample_featureNegative  = [[]]        # Lecture notation: X (partial set):
    trainingSample_featurePositive  = [[]]        # Lecture notation: X (partial set):
    trainingSample_feature          = [[]]        # Lecture notation: X (total set):
    SVM_featureNegative             = [[]]
    SVM_featurePositive             = [[]]
    """
    # -----------------------------
    # Builder
    # -----------------------------
    def parseProblemInstance(self, normalizeData=False, inputFileName = "../resource/input/parameter.txt"):
        file = open(inputFileName)

        # Init feature samples
        self.nbrSamples                     = int(nextMeaningLine(file))
        self.featureDimension               = int(nextMeaningLine(file))
        self.trainingSample_featurePositive = [[] for i in xrange(self.featureDimension)]
        self.trainingSample_featureNegative = [[] for i in xrange(self.featureDimension)]
        self.SVM_featurePositive            = [[] for i in xrange(self.featureDimension)]
        self.SVM_featureNegative            = [[] for i in xrange(self.featureDimension)]
        vect= []
#        SVM = []
        for sample in xrange(self.nbrSamples):
            isSVM   = int(nextMeaningLine(file))
            y       = int(nextMeaningLine(file))
            norm    = 0.
            if (y > 0):
                vect= self.trainingSample_featurePositive
#               SVM = self.SVM_featurePositive
            else:
                vect= self.trainingSample_featureNegative
#                SVM = self.SVM_featureNegative
            for dim in xrange(self.featureDimension):
                xi      = int(nextMeaningLine(file))
                norm    += xi ** 2
                (vect[dim]).append(xi)
#                if (isSVM == SVM_defaultAlphaValue):
#                   (SVM[dim]).append(xi)
            if (normalizeData == True):
                index = len(vect[0])-1
                norm = math.sqrt(norm)
                for dim in xrange(self.featureDimension):
                    vect[dim][index] /= norm
        file.close()

    # -----------------------------
    # Getter
    # -----------------------------
    def getNbrSample(self):
        return self.nbrSamples

    def getNbrPositiveSample(self):
        return len(self.trainingSample_featurePositive[0])

    def getNbrNegativeSample(self):
        return len(self.trainingSample_featureNegative[0])

    def getPositiveSample(self):
        return self.trainingSample_featurePositive

    def getNegativeSample(self):
        return self.trainingSample_featureNegative

    def getPositiveSVM(self):
        return self.SVM_featurePositive

    def getNegativeSample(self):
        return self.SVM_featureNegative

    def getFeatureDimension(self):
        return self.featureDimension

