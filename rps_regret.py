import random

class Strategy:
    def __init__(self):
        self.regrets = [0,0,0]
        self.prbs = [(1/3), (1/3), (1/3)]
        self.strategy_sum = [0, 0, 0]
    def get_action(self):
        rand = random.random()
        if rand < self.prbs[0]:
            return 0
        if rand < self.prbs[0] + self.prbs[1]:
            return 1
        return 2
    def update_regrets(self, my_action, opponent_action):
        utility = payoff_matrix[my_action][opponent_action]
        for i in range(3):
            self.regrets[i] += payoff_matrix[i][opponent_action] - utility
        positive_regrets = []
        for regret in self.regrets:
            positive_regrets.append(regret if regret > 0 else 0)
        if sum(positive_regrets) == 0:
            self.prbs = [(1/3), (1/3), (1/3)]
        else:
            regret_sum = sum(positive_regrets)
            for i in range(3):
                self.prbs[i] = positive_regrets[i] / regret_sum
                self.strategy_sum[i] += self.prbs[i]
    def avg_strategy(self):
        return [x / sum(self.strategy_sum) for x in self.strategy_sum]
        
        
    
#rock = 0, paper = 1, scissors = 2
payoff_matrix = [ [0, -1, 1],
                  [1, 0, -1],
                  [-1, 1, 0] ]

def simulate_rps(strategy, opponent_strategy, iterations):
    for i in range(iterations):
        my_action = strategy.get_action()
        rand = random.random()
        if rand < opponent_strategy[0]:
            opponent_action = 0
        elif rand < opponent_strategy[0] + opponent_strategy[1]:
            opponent_action = 1
        else:
            opponent_action = 2
        strategy.update_regrets(my_action, opponent_action)

def rps_equilibrium(strategy1, strategy2, iterations):
    for i in range(iterations):
        action1 = strategy1.get_action()
        action2 = strategy2.get_action()
        strategy1.update_regrets(action1, action2)
        strategy2.update_regrets(action2, action1)


