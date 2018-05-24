#forward pass 3Layers NN

f = lambda x: 1.0/(1.0 + np.exp(-x))#sigmoid activation function
x = np.random.randn (3,1)#random input vector of 3 numbers
h1= f(np.dot(W1,x)+b1) # calculate first hidden layer activations (4x1)
h2 = f (np.dot(W2,h1) + b2) # calculate second hidden layer activations (4x1)
out = np.dot (W3,h2)+b3 # output neuron 1x1
