from game import GameEnv
from q_agent import choose_action, update_q
import matplotlib.pyplot as plt
import pygame
import numpy as np 

env = GameEnv()

episodes = 500
rewards = []

for ep in range(episodes):# Belirlenen toplam deneme sayısı kadar dön

    state = env.reset()# Her deneme başında oyunu sıfırla
    done = False
    total = 0# Toplam ödülü takip et

    while not done:

        # pygame eventleri kontrol et # Pygame'in donmasını engellemek için event kontrolü
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        action = choose_action(state)# Ajan karar verir

        next_state, reward, done = env.step(action)# Çevre tepki verir

        # Algoritmayı güncelle (Öğrenme burada gerçekleşir)
        update_q(state, action, reward, next_state, done)

        state = next_state
        total += reward# Skor tablosunu güncelle

        env.render()# Ekrana çiz

    rewards.append(total)

plt.plot(rewards)
plt.title("Q Learning Performance")
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.show()
np.save("q_rewards.npy", np.array(rewards)) 
print("Q-Learning verileri 'q_rewards.npy' olarak kaydedildi.")