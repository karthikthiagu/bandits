# Bandit test bed

import numpy as np

from matplotlib import pyplot as plt

from bandits import Bandit
from behavior import BanditBehavior

def runSimulation(testbed, epsilon, color, steps = 1000):
    
    def plotAverageReward():
      
        #fig = plt.figure()
        #ax = fig.add_subplot(111)
        #ax.margins(x = 0.1, y = 0)
        plt.margins(0.1, 0.0)
        plt.xticks([1] + list(np.arange(0, 1001, 250))[1:])
        plt.yticks(np.arange(0, 2, 0.5))
        plt.plot(range(steps + 1)[1:], average_reward, color = color)
        plt.plot([1, 1000], [optimal_reward, optimal_reward], color = 'blue')
        plt.xlabel('Steps')
        plt.ylabel('Average Reward')

    testbed, optimal_reward = testbed['testbed'], testbed['optimal_reward']
    epsilon = epsilon
    average_reward = [0]
    for step in range(steps - 1):
        if step % 100 == 0:
            print '%s percent complete' % str(float(step) / float(steps) * 100)[:5]
        rewards = np.zeros((len(testbed),))
        for index, bandit in enumerate(testbed):
            rewards[index] = bandit.behaveEpsilonGreedy(epsilon)
        average_reward.append( np.mean(rewards) )
    plotAverageReward()

def generateTestbed(N, K):

    testbed = list()
    optimal_reward = np.zeros((N, ))
    for i in range(N):
        bandit = Bandit(K)
        behave = BanditBehavior(bandit)
        testbed.append(behave)
        optimal_reward[i] = bandit.optimal_reward

    optimal_reward = np.mean(optimal_reward)
    print optimal_reward
    return {'testbed' : testbed, 'optimal_reward' : optimal_reward}

def flush(testbed):
    for bandit in testbed:
        bandit.flush()

if __name__ == '__main__':

    testbed = generateTestbed(2000, 10)
    for epsilon, color in [(0.0, 'green'), (0.01, 'red'), (0.1, 'black') ]:
        runSimulation(testbed, epsilon, color, steps = 1000)
        flush(testbed['testbed'])

    plt.savefig('average-reward-steps.png')
    
