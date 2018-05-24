class Neuron:
    def neuron_tick(inputs):
"""inputs and weights are 1D numpy arrays and bias is a scalar"""
    cell_body_sum = np.sum (inputs * self.weights) + self.bias
    firing_rate = 1. / (1. + math.exp(-cell_body_sum)) #sigmoid
    return firing_rate
