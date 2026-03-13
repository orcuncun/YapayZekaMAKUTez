import torch
import torch.nn as nn
import torch.optim as optim
import random

ACTIONS = 4

class DQN(nn.Module):
    """Basit bir yapay sinir ağı mimarisi."""
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2,64),  # Giriş katmanı: X ve Y koordinatları
            nn.ReLU(),        # Aktivasyon fonksiyonu
            nn.Linear(64,64), # Gizli katman
            nn.ReLU(),
            nn.Linear(64,ACTIONS) # Çıkış: 4 hareketin Q değerleri
        )

    def forward(self,x):
        return self.net(x)

class Agent:
    def __init__(self):
        self.model = DQN() # Modelin oluşturulması
        self.optimizer = optim.Adam(self.model.parameters(),lr=0.001) # Ağırlık güncelleyici
        self.gamma = 0.9
        self.epsilon = 0.2

    def choose_action(self,state):
        """Sinir ağını kullanarak en iyi hareketi tahmin eder."""
        if random.random() < self.epsilon:
            return random.randint(0,3) # Keşif

        s = torch.tensor(state,dtype=torch.float32) # Durumu tensöre çevir
        qvals = self.model(s) # Ağı tahmin için çalıştır
        return torch.argmax(qvals).item() # En yüksek değerli eylemi dön

    def train(self,state,action,reward,next_state,done):
        """Geri yayılım (Backpropagation) ile ağı eğitir."""
        s = torch.tensor(state,dtype=torch.float32)
        ns = torch.tensor(next_state,dtype=torch.float32)

        q = self.model(s)[action] # Tahmin edilen Q değeri

        # Hedef değer hesaplama (Bellman)
        with torch.no_grad():
            target = reward + self.gamma * torch.max(self.model(ns))

        # Hata (Loss) hesaplama: MSE (Mean Squared Error)
        loss = (q-target)**2

        # Ağırlıkların güncellenmesi
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()