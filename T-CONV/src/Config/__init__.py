import os
#import _pickle as cPickle
import numpy as np

# from blocks.initialization import IsotropicGaussian, Constant
# from blocks.algorithms import Momentum

#import Data as data

n_begin_end_pts = 5  # how many points we consider at the beginning and end of the known trajectory


tgtcls = np.load('/Users/xinchengzhu/Downloads/arrival-clusters.npy')
#with open(os.path.join(data.path, 'arrival-clusters.pkl')) as f: tgtcls = cPickle.load(f)
