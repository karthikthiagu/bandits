# Algorithms describing the bandit-behavior
import operator

import numpy as np

class Policy:
    
    def __init__(self, arms_value, arms_pulls, time, param):
        self.arms_value = arms_value
        self.arms_pulls = arms_pulls
        self.time = time
        self.K = self.arms_value.shape[0]
        self.param = param
        self.select = {'epsilonGreedy' : self.epsilonGreedy, 'softmax' : self.softmax, 'ucb' : self.ucb}
        
    def epsilonGreedy(self):

        greedy_arm = np.argmax(self.arms_value)
        decide_arm = np.random.uniform()
        if decide_arm < 1 - self.param:
            arm = greedy_arm
        else:
            arm = np.random.choice(range(self.K))
        return arm

    def softmax(self):
        def softmax_helper(x, t):
            x_norm = x - np.max(x)
            x_norm_t = x_norm / t
            e_x_norm_t = np.exp(x_norm_t)
            sum_e_x_norm_t = np.sum(e_x_norm_t)
            return e_x_norm_t / sum_e_x_norm_t

        # PDF
        pdf = softmax_helper(self.arms_value, self.param)
        arms_pdf = zip(range(self.K), pdf)
        sorted_arms_pdf = sorted(arms_pdf, key = operator.itemgetter(1))
        arms, pdf = zip(*sorted_arms_pdf)
        # CDF
        cdf = np.zeros(self.K + 1)
        for i in range(self.K + 1)[1 : ]:
            cdf[i] = cdf[i - 1] + pdf[i - 1]
        decide_arm = np.random.uniform()
        # Sample
        for i in range(self.K + 1)[1 : ]:
            if decide_arm < cdf[i]:
                arm = arms[i - 1]
                break

        return arm

    def ucb(self):
        if np.sum( self.arms_value == np.zeros((self.K, )) ) >= 1:
            for arm in range(self.K):
                if self.arms_value[arm] == 0:
                    return arm
        else:
            estimates = self.arms_value + self.param * np.sqrt(np.log(self.time) * np.power(self.arms_pulls, -1))
            arm = np.argmax(estimates)
            return arm

if __name__ == '__main__':

    bandit = Bandit(10)
    behave = BanditBehavior(bandit)
    count = 0
    for i in range(10):
        print '------------------'
        reward, arm = behave.behaveSoftmax(1.0)
        print '------------------'

