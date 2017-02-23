import numpy as np

from agent import Agent
from environment import Environment

class Testbed:

    def __init__(self, N, K):

        np.random.seed(1)

        self.size = N
        self.agents = []
        self.environments = []
        self.optimal_reward = 0
        
        # Generate Bandits
        optimal_rewards = np.zeros((N, ))
        for i in range(N):
            environment = Environment(K)
            agent = Agent(K)
            self.agents.append(agent)
            self.environments.append(environment)
            optimal_rewards[i] = environment.optimal_reward
        self.optimal_reward = np.mean(optimal_rewards)

        print self.optimal_reward
    
    # Flush testbed
    def flush(self):
        for agent in self.agents:
            agent.flush()

if __name__ == '__main__':

    testbed = Tesetbed(2000, 10)

