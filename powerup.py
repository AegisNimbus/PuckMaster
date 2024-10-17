import pygame
import random
import constants as const

class PowerUp:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.radius = 15
        self.active_time = 7000  # 7 seconds
        self.spawn_time = pygame.time.get_ticks()
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            if self.type == "speed":
                color = const.RED
                pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
                pygame.draw.polygon(screen, const.WHITE, [(self.x-5, self.y+5), (self.x+5, self.y), (self.x-5, self.y-5)])
            elif self.type == "size":
                color = const.GREEN
                pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
                pygame.draw.circle(screen, const.WHITE, (int(self.x), int(self.y)), self.radius-5, 2)
            elif self.type == "shield":
                color = const.BLUE
                pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
                pygame.draw.arc(screen, const.WHITE, (self.x-10, self.y-10, 20, 20), 0, 3.14, 2)

def spawn_powerup(min_x, max_x, height):
    x = random.randint(min_x, max_x)
    y = random.randint(100, height - 100)
    type = random.choice(["speed", "size", "shield"])
    return PowerUp(x, y, type)
