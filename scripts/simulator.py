# Bandit test bed
import sys

import numpy as np
import json

from testbed import Testbed
from policy import Policy
from plotter import configure, plot

def runSimulation(simulation, testbed, steps = 1000):

    horizon = range(steps + 1)[1 : ]
    terminal_step = steps
    average_reward = [0]
    optimal_action = []
    for step in horizon:
        # Status
        if step % 100 == 0:
            print '%s percent complete' % str(float(step) / float(steps) * 100)[:5]
        # Temp vars for plotting
        rewards = np.zeros( (testbed.size, ) )
        pulls   = np.zeros( (testbed.size, ) )
        # Run one step for each agent
        for index in range(testbed.size):
            agent, environment = testbed.agents[index], testbed.environments[index]
            arm = agent.decide(simulation['policydetails'])     # Agent uses a policy to decide the arm to pull
            rewards[index] = agent.act(environment, arm)        # Agent pulls the arm and gets a reward from the environment
            pulls[index] = (arm == environment.optimal_arm)     # Check if this is an optimal action
        optimal_action.append( np.mean(pulls) * 100 )           # Update optimal action count
        average_reward.append( np.mean(rewards) )               # Update average reward count

    plot(horizon, average_reward[ : terminal_step], simulation['plotdetails']['average_reward'])   # Plot average rewards vs steps
    plot(horizon, optimal_action[ : terminal_step], simulation['plotdetails']['optimal_action'])   # Plot optimal action vs steps

def loadSimulations(filename):
    simulations = json.load(open(filename, 'r'))
    return simulations

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'Usage : python scripts/simulator.py simulations_details.json'
        exit()
    else:
        _, simulations_details = sys.argv
    configure()
    simulations = loadSimulations(simulations_details)
    testbed = Testbed(2000, 10)
    for simulation in simulations:
        runSimulation(simulation, testbed, steps = 1000)
        testbed.flush()

