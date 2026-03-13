import torch
import torch.nn as nn
import torch.optim as optim
import random

ACTIONS = 4

class DQN(nn.Module):

    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(2,64),
            nn.ReLU(),
            nn.Linear(64,64),
            nn.ReLU(),
            nn.Linear(64,ACTIONS)
        )

    def forward(self,x):
        return self.net(x)


class Agent:

    def __init__(self):

        self.model = DQN()
        self.optimizer = optim.Adam(self.model.parameters(),lr=0.001)

        self.gamma = 0.9
        self.epsilon = 0.2

    def choose_action(self,state):

        if random.random() < self.epsilon:
            return random.randint(0,3)

        s = torch.tensor(state,dtype=torch.float32)

        qvals = self.model(s)

        return torch.argmax(qvals).item()

    def train(self,state,action,reward,next_state,done):

        s = torch.tensor(state,dtype=torch.float32)
        ns = torch.tensor(next_state,dtype=torch.float32)

        q = self.model(s)[action]

        with torch.no_grad():
            target = reward + self.gamma * torch.max(self.model(ns))

        loss = (q-target)**2

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()