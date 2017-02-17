# The bandit test bed

import numpy as np

class Bandit:

    def __init__(self, K = 10):
        self.K = K
        seeds = np.random.choice(100, self.K + 1, replace = False)
        np.random.seed(seeds[-1])
        expected_rewards = np.random.normal(loc = 0.0, scale = 1.0, size = self.K)
       
        self.arms = list()
        for i in range(self.K):
            arm = { 'random'   : np.random.RandomState(seeds[i]),\
                    'expected' : expected_rewards[i] }
            self.arms.append(arm)
       
        print 'Created a %d-armed bandit' % self.K

if __name__ == '__main__':

    bandit_instance = Bandit(10)

