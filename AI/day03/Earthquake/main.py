import numpy as np
import rnn_model
import torch
import data_handler
import sklearn.utils
import matplotlib.pyplot as plt
import torch.optim as optim

import torch.nn as nn

NEED_TO_CREATE_NPY = True

LR = 0 # TODO
BATCH_SIZE = 0 # TODO
EPOCHS = 0 # TODO

net = None # TODO

if NEED_TO_CREATE_NPY:
    pass  # TODO

dataset = None # TODO
labels = None  # TODO

dataset, labels = data_handler.create_batchs(dataset, labels, 100)
print(dataset.shape)

for epoch in range(EPOCHS):
    pass  # TODO

# TODO
plt.show()
