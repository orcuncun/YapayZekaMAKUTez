from game import GameEnv
from dqn_agent import Agent
import matplotlib.pyplot as plt
import pygame

env = GameEnv()
agent = Agent()

episodes = 500
rewards = []

for ep in range(episodes):

    state = env.reset()
    done = False
    total = 0

    while not done:

        # pygame eventleri okunmalı
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        action = agent.choose_action(state)

        next_state, reward, done = env.step(action)

        agent.train(state, action, reward, next_state, done)

        state = next_state
        total += reward

        env.render()

    rewards.append(total)

plt.plot(rewards)
plt.title("Deep Q Learning Performance")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.show()