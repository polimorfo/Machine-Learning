 class ComputationalGraph(object):
 
 def forward (inputs):
 # 1 pass inputs to input gates
 # forward the computational graph
    for gate in self.graph.nodes_topologically_sorted():
    gate.forward()
 return loss # the final gate in the graps output the loss
 
 def backguard():
     for gate in reversed (self.graph.nodes_topologically_sorted()):
     gate.backguard() # little piece of backp`rop(chain rule applied)
 return input_gradients
