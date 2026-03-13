import matplotlib.pyplot as plt
import numpy as np

q_rewards = np.load("q_rewards.npy")
dqn_rewards = np.load("dqn_rewards.npy")

plt.plot(q_rewards,label="Q Learning")
plt.plot(dqn_rewards,label="Deep Q Learning")

plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Algorithm Comparison")

plt.legend()
plt.show()