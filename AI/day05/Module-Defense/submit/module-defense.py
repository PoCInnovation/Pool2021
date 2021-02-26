import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import gym
from collections import namedtuple
import numpy as np
import random

Transition = namedtuple('Transition', ('state', 'action', 'next_state', 'reward'))
BATCH_SIZE = 128     
GAMMA = 0.999        
LEARNING_RATE = 0.001
NB_EPISODE = 50_000
NB_ITERATION = 500

class PGN(nn.Module):
    def __init__(self, input_size, n_actions):
       # Need code

    def forward(self, x):
        return  # Need COde

class Memory(object):

    def __init__(self, capacity: int):
        # Need Code
    
    def clear(self):
        # Need Code

    def push(self, *args: list):
        """push a transition"""
        # Need Code

    def batch(self, batch_size):
        return # Need Code
    
    def __len__(self):
        return len(self.memory)


class Agent:
    def __init__(self, env, neural, optimizer):
        # Need COde

    def init(self):
        pass
    
    def save(self, path: str):
        pass

    def load(self, path: str):
        pass

    def take_action(self, state) -> [int]:
        logits_v = # Need Code
        prob_v = # Need Code
        action = # Need Code
        return # Need COde

    def calc_qvals(self, rewards):
        # Need Code
        return # Need Code

    def learn(self):
        transitions = self.memory.batch(BATCH_SIZE)
        # On passe d'un tableau de transition a une transition de tableau
        # On met * pour passer l'arg à la fonction zip puis * pour unzip sous forme de list
        batch: Transition = Transition(*zip(*transitions))
        batch_qvals = []
        batch_qvals.extend(self.calc_qvals(batch.reward))

        optimizer.zero_grad()
        states_v = # Need Code
        batch_actions_t = # Need Code
        batch_qvals_v = # Need Code

        logits_v = # Need Code
        log_prob_v = F.log_softmax(logits_v, dim=1)
        log_prob_actions_v = batch_qvals_v * log_prob_v[range(len(states_v)), batch_actions_t]
        loss_v = # Need Code 

        # Need 3 lines of code
       

if __name__ == '__main__':
    env = gym.make("CartPole-v1")
    # Need Code
    for episode in range(NB_EPISODE):
        new_state = env.reset()
        done = False
        i = 0
        for i in range(NB_ITERATION):
            env.render()
            state = new_state
            # Need 2 lines of code
            if done == True:
                agent.memory.push(state, action, None, reward)
                episode_rewards.append(reward)
                print(f"episode: {episode}, iteration {i}, mean {np.mean(episode_rewards)}")
                # Need 1 lines of code
                break
            # Need 1 lines of code
            episode_rewards.append(reward)
        print(f"episode: {episode}, iteration {i}, mean {np.mean(episode_rewards)}") 