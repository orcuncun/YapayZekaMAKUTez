import pygame

# Sabit Değerler: Ekran boyutları ve ızgara sistemi
WIDTH, HEIGHT = 400, 400
GRID = 40

class GameEnv:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock() # Oyun hızını kontrol etmek için

        # Nesnelerin tanımlanması (Oyuncu, Hedef, Tuzaklar)
        self.player = pygame.Rect(40,40,GRID,GRID) # Mavi Kare
        self.goal = pygame.Rect(320,320,GRID,GRID) # Yeşil Kare (Hedef)
        self.traps = [
            pygame.Rect(120,120,GRID,GRID), # Kırmızı Kareler (Tuzak)
            pygame.Rect(200,200,GRID,GRID)
        ]

    def reset(self):
        """Her yeni denemede (episode) karakteri başlangıç noktasına döndürür."""
        self.player.topleft = (40,40)
        return self.get_state()

    def get_state(self):
        """Piksel konumlarını ızgara koordinatlarına (ör: 0, 1, 2) dönüştürür."""
        return (self.player.x//GRID, self.player.y//GRID)

    def step(self, action):
        """Ajanın bir eylem yapmasını sağlar ve sonuçlarını (ödül, bitti mi) döner."""
        if action == 0: self.player.y -= GRID # YUKARI
        elif action == 1: self.player.y += GRID # AŞAĞI
        elif action == 2: self.player.x -= GRID # SOL
        elif action == 3: self.player.x += GRID # SAĞ

        # Ekran dışına çıkmasını engelle (Sınır kontrolü)
        self.player.x = max(0, min(WIDTH-GRID, self.player.x))
        self.player.y = max(0, min(HEIGHT-GRID, self.player.y))

        reward = -0.01 # Her adım için küçük bir negatif ceza (Hızlı gitmeye teşvik)
        done = False # Episode bitti mi kontrolü

        # Hedefe ulaşma kontrolü
        if self.player.colliderect(self.goal):
            reward = 10 # Büyük ödül
            done = True

        # Tuzağa düşme kontrolü
        for t in self.traps:
            if self.player.colliderect(t):
                reward = -5 # Büyük ceza
                done = True

        return self.get_state(), reward, done

    def render(self):
        """Görselleştirme: Kareleri ekrana çizer."""
        self.screen.fill((0,0,0)) # Arka plan siyah
        pygame.draw.rect(self.screen,(0,255,0),self.goal) # Hedef yeşil
        for t in self.traps:
            pygame.draw.rect(self.screen,(255,0,0),t) # Tuzaklar kırmızı
        pygame.draw.rect(self.screen,(0,0,255),self.player) # Oyuncu mavi
        pygame.display.flip()
        self.clock.tick(10) # Oyun hızı (10 FPS)