import numpy as np

from policy import Policy

class Agent:
    
    def __init__(self, K):
        self.K = K
        self.arms_value = np.zeros((self.K, ))
        self.arms_pulls  = np.zeros((self.K, ))

    def flush(self):
        self.arms_value = np.zeros((self.K, ))
        self.arms_pulls = np.zeros((self.K, ))

    def estimate(self, arm, reward):
        self.arms_pulls[arm] += 1
        alpha = 1.0 / self.arms_pulls[arm]
        self.arms_value[arm] += alpha * (reward - self.arms_value[arm])

    def act(self, environment, arm):
        reward = environment.pull(arm)
        self.estimate(arm, reward)
        return reward

    def decide(self, policy):
        policyname, param = policy['policyname'], policy['param']
        arm = Policy(self.arms_value, self.arms_pulls, param).select[policyname]()
        return arm

