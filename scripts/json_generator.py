import json

with open('data/epsilonGreedy.json', 'w') as f:

    sims = list()
    ############################### SIMULATION-1 ##########################################
    data = dict()

    data['policydetails'] = dict()
    data['policydetails']['policyname'] = 'epsilonGreedy'
    data['policydetails']['param'] = 0.0

    data['plotdetails'] = dict()
    data['plotdetails']['average_reward'] = dict()
    data['plotdetails']['average_reward']['color'] = 'green'
    data['plotdetails']['average_reward']['x_text'] = 550
    data['plotdetails']['average_reward']['y_text'] = 0.9
    data['plotdetails']['average_reward']['text'] = r'$\epsilon = 0 (greedy)$'
    data['plotdetails']['average_reward']['figure'] = 1
    data['plotdetails']['average_reward']['xlabel'] = 'Steps'
    data['plotdetails']['average_reward']['ylabel'] = 'Average\nReward'

    data['plotdetails']['optimal_action'] = dict()
    data['plotdetails']['optimal_action']['color'] = 'green'
    data['plotdetails']['optimal_action']['x_text'] = 300
    data['plotdetails']['optimal_action']['y_text'] = 24
    data['plotdetails']['optimal_action']['text'] = r'$\epsilon = 0 (greedy)$'   
    data['plotdetails']['optimal_action']['figure'] = 2
    data['plotdetails']['optimal_action']['xlabel'] = 'Steps'
    data['plotdetails']['optimal_action']['ylabel'] = '%\nOptimal\nAction'

    sims.append(data)
    ############################### SIMULATION-1 ##########################################

    ############################### SIMULATION-2 ##########################################
    data = dict()

    data['policydetails'] = dict()
    data['policydetails']['policyname'] = 'epsilonGreedy'
    data['policydetails']['param'] = 0.01

    data['plotdetails'] = dict()
    data['plotdetails']['average_reward'] = dict()
    data['plotdetails']['average_reward']['color'] = 'red'
    data['plotdetails']['average_reward']['x_text'] = 800
    data['plotdetails']['average_reward']['y_text'] = 1.18
    data['plotdetails']['average_reward']['text'] = r'$\epsilon = 0.01$'
    data['plotdetails']['average_reward']['figure'] = 1
    data['plotdetails']['average_reward']['xlabel'] = 'Steps'
    data['plotdetails']['average_reward']['ylabel'] = 'Average\nReward'

    data['plotdetails']['optimal_action'] = dict()
    data['plotdetails']['optimal_action']['color'] = 'red'
    data['plotdetails']['optimal_action']['x_text'] = 750
    data['plotdetails']['optimal_action']['y_text'] = 45
    data['plotdetails']['optimal_action']['text'] = r'$\epsilon = 0.01$'
    data['plotdetails']['optimal_action']['figure'] = 2
    data['plotdetails']['optimal_action']['xlabel'] = 'Steps'
    data['plotdetails']['optimal_action']['ylabel'] = '%\nOptimal\nAction'

    sims.append(data)
    ############################### SIMULATION-2 ##########################################

    ############################### SIMULATION-3 ##########################################
    data = dict()

    data['policydetails'] = dict()
    data['policydetails']['policyname'] = 'epsilonGreedy'
    data['policydetails']['param'] = 0.1

    data['plotdetails'] = dict()
    data['plotdetails']['average_reward'] = dict()
    data['plotdetails']['average_reward']['color'] = 'black'
    data['plotdetails']['average_reward']['x_text'] = 200
    data['plotdetails']['average_reward']['y_text'] = 1.4
    data['plotdetails']['average_reward']['text'] = r'$\epsilon = 0.1$'
    data['plotdetails']['average_reward']['figure'] = 1
    data['plotdetails']['average_reward']['xlabel'] = 'Steps'
    data['plotdetails']['average_reward']['ylabel'] = 'Average\nReward'
    data['plotdetails']['average_reward']['filename'] = 'plots/epsilonGreedy_average_reward.png'

    data['plotdetails']['optimal_action'] = dict()
    data['plotdetails']['optimal_action']['color'] = 'black'
    data['plotdetails']['optimal_action']['x_text'] = 100
    data['plotdetails']['optimal_action']['y_text'] = 70
    data['plotdetails']['optimal_action']['text'] = r'$\epsilon = 0.1$'
    data['plotdetails']['optimal_action']['figure'] = 2
    data['plotdetails']['optimal_action']['xlabel'] = 'Steps'
    data['plotdetails']['optimal_action']['ylabel'] = '%\nOptimal\nAction'
    data['plotdetails']['optimal_action']['filename'] = 'plots/epsilonGreedy_optimal_action.png'
    

    sims.append(data)
     ############################### SIMULATION-3 ##########################################33   

    # Dump into a json
    print sims
    json.dump(sims, f)

