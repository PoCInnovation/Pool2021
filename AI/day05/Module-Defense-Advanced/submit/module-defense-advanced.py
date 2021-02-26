
import argparse
import gym
import numpy as np
from itertools import count
from collections import namedtuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

SavedAction = namedtuple('SavedAction', ['log_prob', 'value'])
Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward', 'savedAction'))

BATCH_SIZE = # Need Some Code    
GAMMA = # Need Some Code
LEARNING_RATE = # Need Some Code
NB_EPISODE = # Need Some Code
NB_ITERATION = # Need Some Code
eps = # Need Some Code

class Memory(object):

    def __init__(self, capacity: int):
        # Need Some Code
    
    def clear(self):
        # Need Some Code

    def push(self, *args: list):
        # Need Some Code

    def batch(self):
        return self.memory
    
    def __len__(self):
        return # Need Some Code


class Neural(nn.Module):
    def __init__(self, input_size, n_actions):
        super(Neural, self).__init__()
        self.affine1 = # Need Some Code
        # actor's layer
        self.action_head = # Need Some Code
        # critic's layer
        self.value_head = # Need Some Code

    def forward(self, x):
        x = # Need Some Code

        # actor: choses action to take from state s_t 
        # by returning probability of each action
        action_prob = # Need Some Code

        state_values = # Need Some Code
        # return values for both actor and critic as a tuple of 2 values:
        # 1. a list with the probability of each action over the action space
        # 2. the value from state s_t 
        return # Need Some Code, # Need Some Code

class Agent:
    def __init__(self, env, neural, optimizer):
        # Need Some Code
        self.init()

    def init(self):
        pass
    
    def save(self, path: str):
        pass

    def load(self, path: str):
        pass

    def take_action(self, state) -> [int]:
        probs, state_value = # Need Some Code
        # create a categorical distribution over the list of probabilities of actions
        m = # Need Some Code
        # and sample an action using the distribution
        action = # Need Some Code
        # action = action to take
        return # Need Some Code (One value), # Need Some Code (tuple)        

    def calc_qvals(self, rewards):
        # Need Some Code
        return # Need Some Code

    def learn(self):
        transitions = self.memory.batch(BATCH_SIZE)
        # On passe d'un tableau de transition a une transition de tableau
        # On met * pour passer l'arg à la fonction zip puis * pour unzip sous forme de list
        batch: Transition = Transition(*zip(*transitions))
        batch_savedActions = # Need Some Code
        batch_qvals = # Need Some Code


        policy_losses = [] # list to save actor (policy) loss
        value_losses = [] # list to save critic (value) loss

        # Need Some Code (loss)

        # Need Some Code (Reset Grad)

       
        loss =  # Need Some Code (sum up all the values of policy_losses and value_losses)

        # Need Some Code (perform backprop)
        

def main():
    env = gym.make("Assault-ram-v0")
    print(env.observation_space)
    print(env.action_space)
    neural = # Need Some Code
    optimizer = # Need Some Code
    agent: Agent =  # Need Some Code
    episode_rewards = []
    running_reward = 10
    # run inifinitely many episodes
    for episode in range(NB_EPISODE):
        # Need Some Code
        for i in range(1, NB_ITERATION):
           # Need Some Code
            if done == True or i == NB_ITERATION - 1:
                # Need Some Code
                agent.learn()
                break
            # Need Some Code
            episode_rewards.append(reward)
        print(f"episode: {episode}, iteration {i}, mean {np.mean(episode_rewards)}")

if __name__ == '__main__':
    main()