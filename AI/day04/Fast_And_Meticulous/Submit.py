import numpy as np
import matplotlib.pyplot as plt
import pickle
import time

from BlobEnv import BlobEnv
from collections import namedtuple

EPISODES = 0        # TODO
SHOW_EVERY = 0      # TODO

LEARNING_RATE = 0   # TODO
DISCOUNT = 0        # TODO

epsilon = 0         # TODO
EPS_DECAY = 0       # TODO

MEM_SIZE = 0        # TODO

start_q_table = None # It can also be a path to a Qtable

stepAllowed = 200
BlobEnv = BlobEnv(stepAllowed=stepAllowed)

def init_Qtable():
    q_table = {}
    # TODO: init the Qtable using BlobEnv.SIZE and np.random.uniform()
    return q_table

def select_action(epsilon, q_table, state):
    # TODO: select action to do according to epsilon and Qtable
    return action

if start_q_table is None:
    pass
    # TODO: Init the Qtable
else:
    pass
    # TODO: Load the Qtable using pickle

class Memory():
    def __init__(self, mem_size):
        # TODO: init a namedtuple stocking state, action, reward and next_state
        # TODO: init memory
        # TODO: init mem_size

    def add(self, state, action, reward, next_state):
        # TODO: add element to your memory (pay attention to mem_size)

    def train(self, q_table):
        # TODO: update q_table according to your memory

        return q_table

episode_rewards = []
memory = Memory(MEM_SIZE)

for episode in range(EPISODES):
    if 1 ==1 # TODO:
        show = True
    else:
        show = False

    episode_reward = 0
    obs = BlobEnv.getObs()

    for i in range(stepAllowed):
        pass
        # TODO: select an action
        # TODO: do an action
        # TODO: add to your memory
        if show:
            # TODO: show your agent and the environement
        episode_reward += reward
        if 1 == 1 # TODO:
            break

    # TODO: train your agent
    # TODO: update epsilon
    # TODO: Don't forget to reset the env after each episode
    episode_rewards.append(episode_reward)

# TODO: Save the current qtable

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,)) / SHOW_EVERY, mode="valid")
plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"reward {SHOW_EVERY}ma")
plt.xlabel("episode #")
plt.show()
