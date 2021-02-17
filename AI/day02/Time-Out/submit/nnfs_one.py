import matplotlib.pyplot as plt
import tensorflow.keras as keras
import numpy as np
import tqdm
np.random.seed(42)

def showImg(X_train, y_train) :
    plt.figure(figsize=[6,6])
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.title("Label: %i"%y_train[i])
        plt.imshow(X_train[i].reshape([28,28]),cmap='gray')

def iterate_minibatches(inputs, targets, batchsize, shuffle=False):
    assert len(inputs) == len(targets)
    if shuffle:
        indices = np.random.permutation(len(inputs))
    for start_idx in tqdm.tqdm(range(0, len(inputs) - batchsize + 1, batchsize)):
        if shuffle:
            excerpt = indices[start_idx:start_idx + batchsize]
        else:
            excerpt = slice(start_idx, start_idx + batchsize)
        yield inputs[excerpt], targets[excerpt]
        
class Layer:

    def __init__(self):
        pass
    
    def forward(self, feature):
        return #Need Some code 

    def backward(self, feature, grad_output):
        #Need Some code 
        return #Need Some code 

class Loss:

    def __init__(self):
        pass
    
    def forward(self, logits, targets):
        pass
    
    def backward(self, logits, targets):
        pass

class Dense(Layer):
    
    def __init__(self, input_units, output_units, learning_rate=0.1):
        #Need Some code 
        
    def forward(self, features):
        return #Need Some code 
    
    def backward(self, features, df_ddense):
        #Need Some code
        return #Need Some code 

class Model:
    def __init__(self, loss: Loss):
        #Need Some code 
    
    def add(self, layer :Layer):
        #Need Some code 

    def fit(self, x: np.array, y: np.array, batch_size: int=32, shuffle: bool=True, epochs: int=5):
        train_log = []
        #Need Some code
            plt.plot(train_log,label='train accuracy')
            plt.legend(loc='best')
            plt.grid()
            plt.draw()
            plt.pause(0.001)
        input("Press [enter] to continue.")

    def forward(self, features: np.array) -> list:
        #Need Some code 
        return #Need Some code 

    def predict(self, features):

        #Need Some code 
        return #Need Some code 

    def train(self, features: np.array, target: np.array):
    
        #Need Some code    
        return #Need Some code 


