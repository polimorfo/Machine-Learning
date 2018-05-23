#BackProp with Numpy example

import numpy as np

#nonLinearity --> Activation function --> sigmoid
def nonlin (x, deriv = False):
    if (deriv==True):
        return x*(1-x)
    return 1/(1+ np.exp(-x))

#input data
X= np.array ([[0,0,1],
              [0,1,1],
              [1,0,1],
              [1,1,1]])
              
#output data
y = np.array ([[0],
               [1],
               [1],
               [0]])

np.random.seed(1)

#randomly initialize our weights with mean 0
syn0 = 2 * np.random.random ((3,4))-1
syn1=2* np.random.random((4,1))-1
