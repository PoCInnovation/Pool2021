import random
from collections import namedtuple
from Envi import Env

Transition = # Define namedtuple
BATCH_SIZE = #Define batch size
GAMMA = # Define gamma
LEARNING_RATE = 0.001

class Memory(object):

    def __init__(self, capacity: int):
        # Need some code
    
    def clear(self):
        self.memory: list = []
        self.position: int = 0

    def push(self, *args: list):
        """push a transition"""
        # Need some code

    def batch(self, batch_size):
        return # Need some code

    def __len__(self):
        return # Need some code

class Agent:
    def __init__(self, env: Env):
        # Need some code
        self.init_v()

    def init_v(self):
        map = env.get_map()
        for j in range(len(map)):
            if map[j] == 'T':
                self.V[j] = 10

    def save_v(self, path: str):
        with open(path, 'w') as f:
            for v_f in self.V:
                f.write(str(round(v_f, 4)) + " ")

    def load_v(self, path: str):
        with open(path, 'r') as f:
            self.V = f.read().split(" ")
            del self.V[len(self.V) - 1]
            for k in range(len(self.V)):
                self.V[k] = float(self.V[k])

    def greedy_step(self) -> int:
        actions = [1, 2, 3, 4]
        # Need some Code
        # Tips: Predict takes an action and return [next_state of agent] 
        # Tips : self.V is an array with value for all state so self.V[state] return the value function for that state
        return # Return Action (an int between 1 and 4)

    def take_action(self, eps_t: int) -> [int]:
        # Need some code (if .... return/ else .... return WARNING: cf return type)
        # Tips second line : Need to use greedy_step function that return an int between 1 and 4 and wrap that int into an array ([int])
        # Tips first line : random.randint/random.uniform
    
    def learn(self):
        transitions = self.memory.batch(BATCH_SIZE)
        # On passe d'un tableau de transition a une transition de tableau
        # On met * pour passer l'arg à la fonction zip puis * pour unzip sous forme de list
        batch: Transition = Transition(*zip(*transitions))
        for state, next_state, reward in zip(batch.state, batch.next_state, batch.reward):
            # Need one line of code (look above there is a formula with v[s] = ....)

if __name__ == '__main__':
    print("Bienvenue dans L-Antique Game n°1 ! Vous allez apprendre toutes sortes de choses sur le Reinforcement Learning !")
    env: Env = Env("./ressources/maze.txt")
    agent: Agent = Agent(env)
    i = 0
    eps = 0.9
    # agent.load_v("save.txt")
    while i < 10000:
        if i % 10 == 0:
            eps = max(eps * 0.9998, 0.05)
        state: list = env.get_env()
        action: list = agent.take_action(eps)
        next_state, reward = env.step(action[0])
        agent.memory.push(state, action, next_state, reward)
        env.render(agent.V, eps, 0.1)
        i += 1
        if i > 128:
            agent.learn()
    agent.save_v("./ressources/save.txt")

def dummy_test() :
    isTired = False
    assert (isTired)
    print("\n\033[92mVery good ! go to last step ...\033[0m\n")
