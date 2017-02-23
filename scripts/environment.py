# The bandits

import numpy as np

class Environment:

    def __init__(self, K = 10):
        self.K = K
        self.expected_rewards = np.random.normal(loc = 0.0, scale = 1.0, size = self.K)
        self.optimal_arm = np.argmax(self.expected_rewards)
        self.optimal_reward = np.max(self.expected_rewards)

    def pull(self, arm):
        return np.random.normal(loc = self.expected_rewards[arm], scale = 1.0)

if __name__ == '__main__':
    pass
