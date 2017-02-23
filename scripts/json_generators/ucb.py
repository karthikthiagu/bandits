import json

with open('data/ucb.json', 'w') as f:

    sims = list()
    ############################### SIMULATION-1 ##########################################
    data = dict()

    data['policydetails'] = dict()
    data['policydetails']['policyname'] = 'ucb'
    data['policydetails']['param'] = 2

    data['plotdetails'] = dict()
    data['plotdetails']['average_reward'] = dict()
    data['plotdetails']['average_reward']['color'] = 'blue'
    data['plotdetails']['average_reward']['x_text'] = 240
    data['plotdetails']['average_reward']['y_text'] = 1.5
    data['plotdetails']['average_reward']['text'] = r'$UCB$'
    data['plotdetails']['average_reward']['figure'] = 1
    data['plotdetails']['average_reward']['xlabel'] = 'Steps'
    data['plotdetails']['average_reward']['ylabel'] = 'Average\nReward'

    data['plotdetails']['optimal_action'] = dict()
    data['plotdetails']['optimal_action']['color'] = 'blue'
    data['plotdetails']['optimal_action']['x_text'] = 600
    data['plotdetails']['optimal_action']['y_text'] = 85
    data['plotdetails']['optimal_action']['text'] = r'$UCB$'   
    data['plotdetails']['optimal_action']['figure'] = 2
    data['plotdetails']['optimal_action']['xlabel'] = 'Steps'
    data['plotdetails']['optimal_action']['ylabel'] = '%\nOptimal\nAction'

    sims.append(data)
    ############################### SIMULATION-1 ##########################################


    ############################### SIMULATION-2 ##########################################
    data = dict()

    data['policydetails'] = dict()
    data['policydetails']['policyname'] = 'epsilonGreedy'
    data['policydetails']['param'] = 0.1

    data['plotdetails'] = dict()
    data['plotdetails']['average_reward'] = dict()
    data['plotdetails']['average_reward']['color'] = 'black'
    data['plotdetails']['average_reward']['x_text'] = 1000
    data['plotdetails']['average_reward']['y_text'] = 1.4
    data['plotdetails']['average_reward']['text'] = r'$\epsilon = 0.1$'
    data['plotdetails']['average_reward']['figure'] = 1
    data['plotdetails']['average_reward']['xlabel'] = 'Steps'
    data['plotdetails']['average_reward']['ylabel'] = 'Average\nReward'
    #data['plotdetails']['average_reward']['filename'] = 'plots/ucb_average_reward.png'

    data['plotdetails']['optimal_action'] = dict()
    data['plotdetails']['optimal_action']['color'] = 'black'
    data['plotdetails']['optimal_action']['x_text'] = 750
    data['plotdetails']['optimal_action']['y_text'] = 70
    data['plotdetails']['optimal_action']['text'] = r'$\epsilon = 0.1$'
    data['plotdetails']['optimal_action']['figure'] = 2
    data['plotdetails']['optimal_action']['xlabel'] = 'Steps'
    data['plotdetails']['optimal_action']['ylabel'] = '%\nOptimal\nAction'
    #data['plotdetails']['optimal_action']['filename'] = 'plots/ucb_optimal_action.png'
    

    sims.append(data)
     ############################### SIMULATION-2 ##########################################

    ############################### SIMULATION-3 ##########################################
    data = dict()

    data['policydetails'] = dict()
    data['policydetails']['policyname'] = 'softmax'
    data['policydetails']['param'] = 0.1

    data['plotdetails'] = dict()
    data['plotdetails']['average_reward'] = dict()
    data['plotdetails']['average_reward']['color'] = 'green'
    data['plotdetails']['average_reward']['x_text'] = 500
    data['plotdetails']['average_reward']['y_text'] = 1.1
    data['plotdetails']['average_reward']['text'] = r'$T = 0.1$'
    data['plotdetails']['average_reward']['figure'] = 1
    data['plotdetails']['average_reward']['xlabel'] = 'Steps'
    data['plotdetails']['average_reward']['ylabel'] = 'Average\nReward'
    data['plotdetails']['average_reward']['filename'] = 'plots/ucb_average_reward.png'

    data['plotdetails']['optimal_action'] = dict()
    data['plotdetails']['optimal_action']['color'] = 'green'
    data['plotdetails']['optimal_action']['x_text'] = 500
    data['plotdetails']['optimal_action']['y_text'] = 58
    data['plotdetails']['optimal_action']['text'] = r'$T = 0.1$'
    data['plotdetails']['optimal_action']['figure'] = 2
    data['plotdetails']['optimal_action']['xlabel'] = 'Steps'
    data['plotdetails']['optimal_action']['ylabel'] = '%\nOptimal\nAction'
    data['plotdetails']['optimal_action']['filename'] = 'plots/ucb_optimal_action.png'
    

    sims.append(data)
     ############################### SIMULATION-3 ##########################################33   

    # Dump into a json
    print sims
    json.dump(sims, f)

