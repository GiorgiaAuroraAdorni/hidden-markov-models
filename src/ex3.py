import numpy as np


def state_probability(pi, A, s, T):
    """
    :param pi: initial state ditribution π
    :param A: transition matrix
    :param s: state
    :param T: time
    :return prob[s]: the probability of state s at time t
    """
    prob = np.array(pi)
    for i in range(T):
        prob = np.matmul(prob, A)
    return prob[s]


pi = np.array([0.6, 0.3, 0.1])
A = np.array([[0.7, 0.2, 0.1], [0.4, 0.4, 0.2], [0.2, 0.3, 0.5]])
s = 2
T = 2

prob = state_probability(pi, A, s, T)
print(prob)
