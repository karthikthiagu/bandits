# Bandit test bed

import numpy as np

from matplotlib import pyplot as plt

from bandits import Bandit
from behavior import BanditBehavior


def configure():

    # Set the plot
    paperwidth = 11.7
    paperheight = 8.3
    margin = 1.0
    plt.figure(figsize = (paperwidth - 2 * margin, paperheight - 2*margin))
    plt.margins(0.1, 0.0)
    plt.xticks([1] + list(np.arange(0, 1001, 250))[1:])
    plt.yticks(np.arange(0, 2, 0.5))
    plt.ylim((0, 1.6))
    
    simulations = [ (0.0, 'green',  550, 0.9, r'$\epsilon = 0 (greedy)$'),\
                    (0.01, 'red', 800, 1.18, r'$\epsilon = 0.01$'),\
                    (0.1, 'black', 200, 1.4, r'$\epsilon = 0.1$') ]
    return simulations

def runSimulation(simulation, testbed, steps = 1000):
    
    def plotAverageReward():

        # Plotting
        plt.plot(range(steps + 1)[1:], average_reward, color = color)
        # Labeling
        plt.xlabel('Steps')
        plt.ylabel('Average\n Reward', rotation = 'horizontal', labelpad = 30)
        plt.text(x_text, y_text, text)
        # Save
        plt.savefig('plots/average_reward.png')

    epsilon, color, x_text, y_text, text = simulation
    testbed, optimal_reward = testbed['testbed'], testbed['optimal_reward']
    average_reward = [0]
    for step in range(steps + 1)[1 : -1]:
        if step % 100 == 0:
            print '%s percent complete' % str(float(step) / float(steps) * 100)[:5]
        rewards = np.zeros((len(testbed),))
        for index, bandit in enumerate(testbed):
            rewards[index] = bandit.behaveEpsilonGreedy(epsilon)
        average_reward.append( np.mean(rewards) )
    plotAverageReward()

def generateTestbed(N, K):

    np.random.seed(1)
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

    simulations = configure()
    testbed = generateTestbed(2000, 10)
    for simulation in simulations:
        runSimulation(simulation, testbed, steps = 1000)
        flush(testbed['testbed'])

