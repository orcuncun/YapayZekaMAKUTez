import pygame

WIDTH, HEIGHT = 400, 400
GRID = 40

class GameEnv:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = pygame.Rect(40,40,GRID,GRID)
        self.goal = pygame.Rect(320,320,GRID,GRID)

        self.traps = [
            pygame.Rect(120,120,GRID,GRID),
            pygame.Rect(200,200,GRID,GRID)
        ]

    def reset(self):
        self.player.topleft = (40,40)
        return self.get_state()

    def get_state(self):
        return (self.player.x//GRID, self.player.y//GRID)

    def step(self, action):

        if action == 0:  # up
            self.player.y -= GRID
        elif action == 1:  # down
            self.player.y += GRID
        elif action == 2:  # left
            self.player.x -= GRID
        elif action == 3:  # right
            self.player.x += GRID

        self.player.x = max(0, min(WIDTH-GRID, self.player.x))
        self.player.y = max(0, min(HEIGHT-GRID, self.player.y))

        reward = -0.01
        done = False

        if self.player.colliderect(self.goal):
            reward = 10
            done = True

        for t in self.traps:
            if self.player.colliderect(t):
                reward = -5
                done = True

        return self.get_state(), reward, done

    def render(self):

        self.screen.fill((0,0,0))

        pygame.draw.rect(self.screen,(0,255,0),self.goal)

        for t in self.traps:
            pygame.draw.rect(self.screen,(255,0,0),t)

        pygame.draw.rect(self.screen,(0,0,255),self.player)

        pygame.display.flip()
        self.clock.tick(10)