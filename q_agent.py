import random

ACTIONS = [0,1,2,3] # Tanımlı hareketler
alpha = 0.1         # Öğrenme hızı (Learning Rate)
gamma = 0.9         # Gelecekteki ödüllerin önem katsayısı (Discount Factor)
epsilon = 0.2       # Keşif oranı (Keşfetme vs. Bilgiyi kullanma dengesi)

Q = {} # Q-Tablosu: Sözlük yapısında (durum, eylem) çiftlerini tutar

def choose_action(state):
    """Epsilon-Greedy stratejisi ile bir hareket seçer."""
    if random.random() < epsilon:
        return random.choice(ACTIONS) # Rastgele seçim (Exploration)

    # Tablodaki en yüksek değerli eylemi seç (Exploitation)
    qvals = [Q.get((state,a),0) for a in ACTIONS]
    return ACTIONS[qvals.index(max(qvals))]

def update_q(state,action,reward,next_state,done):
    """Bellman denklemini kullanarak Q değerini günceller."""
    old = Q.get((state,action),0) # Eski değer

    # Sonraki durumdaki en iyi tahmin (Max Q)
    future = max([Q.get((next_state,a),0) for a in ACTIONS])

    # Q-Learning Güncelleme Formülü
    new = old + alpha*(reward + gamma*future - old)
    Q[(state,action)] = new