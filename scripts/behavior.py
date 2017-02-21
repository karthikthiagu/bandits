# Algorithms describing the bandit-behavior
import numpy as np

from bandits import Bandit

class BanditBehavior:
    
    def __init__(self, bandit):
        self.bandit = bandit
        self.K = self.bandit.K
        self.arms_value = np.zeros((self.K, ))
        self.arms_pulls  = np.zeros((self.K, ))

    def flush(self):
        self.arms_value = np.zeros((self.K, ))
        self.arms_pulls = np.zeros((self.K, ))

    def estimate(self, arm, reward):
        self.arms_pulls[arm] += 1
        alpha = 1.0 / self.arms_pulls[arm]
        self.arms_value[arm] += alpha * (reward - self.arms_value[arm])

    def behaveEpsilonGreedy(self, epsilon):

        greedy_arm = np.argmax(self.arms_value)
        random = np.random.uniform(0, 1, 25)
        random = np.random.choice(random)
        if random < 1 - epsilon:
            arm = greedy_arm
        else:
            arm = np.random.choice(range(self.K))
        reward = self.bandit.pull(arm)
        self.estimate(arm, reward)
        return reward

if __name__ == '__main__':

    bandit = Bandit(10)
    behave = BanditBehavior(bandit)
    for i in range(100):
        reward = behave.behaveEpsilonGreedy(0.1)

    '''
    Observations : if you don't do it in an epsilon greedy manner, and instead do it 
    with a probability that is biased towards the current value estimate, you will
    observe oscillations.
    Refer the following snippet:

    p_explore = epsilon / self.K
    p_greedy  = 1 - epsilon
    p_epsilonGreedy = np.ones(self.K) * p_explore
    p_epsilonGreedy[greedy_arm] += p_greedy
    arm = np.random.choice(self.K, size = 1, replace = True, p = p_epsilonGreedy)
    '''
