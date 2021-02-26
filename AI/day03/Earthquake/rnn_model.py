import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class Network(nn.Module):
    def __init__(self, hidden_size, output_size):
        pass # TODO

    def init_hidden(self):
        pass # TODO

    def forward(self, t, hidden):
        pass # TODO

def train(network, optimizer, train_set, train_labels, batch_size=32):
    pass # TODOe


def test(network, test_set, test_labels, batch_size=32):
    pass # TODO
