import numpy as np
import cv2

class Blob():
    def __init__(self, size=10):
        self.SIZE = size
        self.x = np.random.randint(0, self.SIZE)
        self.y = np.random.randint(0, self.SIZE)

    def __str__(self):
        return (f"{self.x}, {self.y}")

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def action(self, choice):
        if choice == 0:
            self.move(x=1, y=1)
        elif choice == 1:
            self.move(x=-1, y=-1)
        elif choice == 2:
            self.move(x=-1, y=1)
        elif choice == 3:
            self.move(x=1, y=-1)

    def move(self, x=False, y=False):
        self.x += x
        self.y += y

        if self.x < 0:
            self.x = 0
        elif self.x > self.SIZE - 1:
            self.x = self.SIZE - 1
        if self.y < 0:
            self.y = 0
        elif self.y > self.SIZE - 1:
            self.y = self.SIZE - 1

class BlobEnv():
    def __init__(self, stepAllowed=200, size=10):
        self.done = False
        self.SIZE = size
        self.d = {1:(255,175,0), 2:(0,255,0), 3:(0,0,255)}
        self.player = Blob(size=size)
        self.food = Blob(size=size)
        self.enemy = Blob(size=size)
        self.stepAllowed = stepAllowed
        self.currentStep = 0
        self.action_reward = 0
        self.MOVE_PENALTY = 1
        self.ENEMY_PENALTY = 300
        self.FOOD_REWARD = 25
        self.PLAYER_N = 1
        self.FOOD_N = 2
        self.ENEMY_N = 3

    def show(self):
        env = np.zeros((600, 600, 3), dtype=np.uint8)
        env[self.food.y * 60:self.food.y * 60 + 60, self.food.x * 60:self.food.x * 60 + 60] = self.d[self.FOOD_N]
        env[self.player.y * 60:self.player.y * 60 + 60, self.player.x * 60:self.player.x * 60 + 60] = self.d[self.PLAYER_N]
        env[self.enemy.y * 60:self.enemy.y * 60 + 60, self.enemy.x * 60:self.enemy.x * 60 + 60] = self.d[self.ENEMY_N]
        cv2.imshow("", np.array(env))
        if self.action_reward == self.FOOD_REWARD or self.action_reward == -self.ENEMY_PENALTY:
            if cv2.waitKey(500) & 0xFF == ord("q"):
                return
        else:
            if cv2.waitKey(100) & 0xFF == ord("q"):
                return

    def doAction(self, action: int):
        if self.currentStep >= self.stepAllowed:
            self.done = True
            print(f"\033[93mWARNING: You already reached the max step: ({self.currentStep}/{self.stepAllowed})\033[0;37;40m")
            return (self.player-self.food, self.player-self.enemy), (self.player-self.food, self.player-self.enemy), self.action_reward, self.done
        elif self.action_reward == self.FOOD_REWARD:
            self.done = True
            print(f"\033[93mWARNING: You already reached the food.\nUse BlobEnv().action_reward to know when to break.\033[0;37;40m")
            return (self.player-self.food, self.player-self.enemy), (self.player-self.food, self.player-self.enemy), self.action_reward, self.done
        elif self.action_reward == -self.ENEMY_N:
            self.done = True
            print(f"\033[93mWARNING: You already reached the enemy.\nUse BlobEnv().action_reward to know when to break.\033[0;37;40m")
            return (self.player-self.food, self.player-self.enemy), (self.player-self.food, self.player-self.enemy), self.action_reward, self.done
        else:
            self.currentStep += 1
        obs = (self.player-self.food, self.player-self.enemy)
        self.action_reward = 0

        self.player.action(action)

        if self.player.x == self.enemy.x and self.player.y == self.enemy.y:
            self.action_reward = -self.ENEMY_PENALTY
            self.done = True
        elif self.player.x == self.food.x and self.player.y == self.food.y:
            self.action_reward = self.FOOD_REWARD
            self.done = True
        else:
            self.action_reward = -self.MOVE_PENALTY
        new_obs = (self.player-self.food, self.player-self.enemy)
        return obs, new_obs, self.action_reward, self.done

    def getObs(self):
        return self.player-self.food, self.player-self.enemy

    def resetEpisode(self):
        self.action_reward = 0
        self.player = Blob()
        self.food = Blob()
        self.enemy = Blob()
        self.currentStep = 0
        self.done = False