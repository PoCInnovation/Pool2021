# -*- coding: utf-8 -*-

import numpy as np

LR = 0.01

def getData() :
    return np.linspace(-6, 6, 30), np.linspace(-6, 6, 30)

def sigmoid_activation(input):
    return # Need some code

def linear_activation(input):
    return input

def d_sigmoid_d_input(input):
    # Need some code
    return # Need some code

def d_linear_d_input(input):
    shape = np.shape(input)
    d_l_d_input =  np.ones(shape)
    return d_l_d_input

def mean_squared_error(predict, target):
    return np.mean((predict - target) **2)

class Neurone :
    def __init__(self, nb_features) :
        self.nb_features = nb_features
        self.w = np.ones((nb_features, 1))
        self.b = np.ones(1)
        self.grad_w = np.zeros((nb_features, 1))
        self.grad_b = np.zeros(1)

    def forward(self, input):
        return input@self.w + self.b

    def backward(self, pre_activation, activation, inputs, target):
        d_f_d_neurone = inputs
        d_l_d_i = (activation - target)
        self.grad_w = np.sum(inputs*(d_l_d_i*d_linear_d_input(pre_activation)))
        self.grad_b = np.sum(d_l_d_i*d_linear_d_input(pre_activation))
    
    def backward_sigmoid(self, pre_activation, activation, inputs, target):
        # Need Some Code

    def resetGrad(self):
        self.grad_w = np.zeros((self.nb_features, 1))
        self.grad_b = np.zeros(1)

if __name__=='__main__':
    x, y = getData()
    x = np.expand_dims(x, 1)
    y = np.ones((30,1))
    neurone : Neurone = Neurone(1)
    epochs = 2
    print("Start of training")
    for epoch in range(epochs):
        for i in range(np.shape(x)[0]):
            pre_activation = neurone.forward(x[i])
            activation = linear_activation(pre_activation)
            loss = mean_squared_error(activation, y[i])
            print(f"loss = {loss}")
            neurone.backward(pre_activation, activation, x[i], y[i])
            neurone.w = neurone.w - (LR * neurone.grad_w)
            neurone.b = neurone.b - (LR * neurone.grad_b)
            neurone.resetGrad()
    print("End of training")

