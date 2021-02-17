from nnfs_one import Layer
from nnfs_one import Loss
import numpy as np

class ReLU(Layer):

    def __init__(self):
        pass
    
    def forward(self, features):
        return #Need Some code 
    
    def backward(self, features, grad_output):
        #Need Some code 
        return #Need Some code 

class Sigmoid(Layer):

    def __init__(self):
        pass
    
    def forward(self, features):
        return #Need Some code 

    def backward(self, features, df_ddense):
        #Need Some code 
        return #Need Some code 

class Softmax_crossentropy_with_logits(Loss):
    
    def __init__(self):
        pass

    def forward(self, logits, targets) -> np.array :
        #Need Some code 
    
        return #Need Some code 

    def backward(self, logits, targets):
        #Need Some code 
    
        return #Need Some code 
