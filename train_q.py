from game import GameEnv
from q_agent import choose_action, update_q
import matplotlib.pyplot as plt
import pygame

env = GameEnv()

episodes = 500
rewards = []

for ep in range(episodes):

    state = env.reset()
    done = False
    total = 0

    while not done:

        # pygame eventleri kontrol et
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        action = choose_action(state)

        next_state, reward, done = env.step(action)

        update_q(state, action, reward, next_state, done)

        state = next_state
        total += reward

        env.render()

    rewards.append(total)

plt.plot(rewards)
plt.title("Q Learning Performance")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.show()