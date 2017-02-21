# The bandits

import numpy as np

class Bandit:

    def __init__(self, K = 10):
        self.K = K
        #seeds = np.random.choice(10000, self.K + 1, replace = False)
        #np.random.seed(seeds[-1])
        self.expected_rewards = np.random.normal(loc = 0.0, scale = 1.0, size = self.K)
        self.optimal_arm = np.argmax(self.expected_rewards)
        self.optimal_reward = np.max(self.expected_rewards)

        self.arms = list()

        #for i in range(self.K):
            #arm = { 'random'   : np.random.RandomState(seeds[i]),\
            #        'expected' : self.expected_rewards[i]}
            #self.arms.append(arm)
    
    def pull(self, arm):
        #nums = self.arms[arm]['random'].normal(loc = self.arms[arm]['expected'], scale = 1.0, size = 25)
        nums = np.random.normal(loc = self.expected_rewards[arm], scale = 1.0, size = 25)       
        return np.random.choice(nums)

if __name__ == '__main__':

    bandit = Bandit(10)
    reward = bandit.pull(3)
    print reward

