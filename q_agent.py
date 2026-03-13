import random

ACTIONS = [0,1,2,3]

alpha = 0.1
gamma = 0.9
epsilon = 0.2

Q = {}

def choose_action(state):

    if random.random() < epsilon:
        return random.choice(ACTIONS)

    qvals = [Q.get((state,a),0) for a in ACTIONS]
    return ACTIONS[qvals.index(max(qvals))]


def update_q(state,action,reward,next_state,done):

    old = Q.get((state,action),0)

    future = max([Q.get((next_state,a),0) for a in ACTIONS])

    new = old + alpha*(reward + gamma*future - old)

    Q[(state,action)] = new