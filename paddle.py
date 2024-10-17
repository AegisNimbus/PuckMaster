import pygame
import math
import constants as const


class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.original_radius = const.PADDLE_SIZE
        self.radius = self.original_radius
        self.original_speed = const.PADDLE_SPEED
        self.speed = self.original_speed
        self.mass = const.PADDLE_MASS
        self.angle = 0
        self.shield = False

    def check_vertical_bounds(self, height):
        # top
        if self.y - self.radius <= 0:
            self.y = self.radius
        # bottom
        elif self.y + self.radius > height:
            self.y = height - self.radius

    def check_left_boundary(self, width):
        if self.x - self.radius <= 0:
            self.x = self.radius
        elif self.x + self.radius > int(width / 2):
            self.x = int(width / 2) - self.radius

    def check_right_boundary(self, width):
        if self.x + self.radius > width:
            self.x = width - self.radius
        elif self.x - self.radius < int(width / 2):
            self.x = int(width / 2) + self.radius

    def move(self, up, down, left, right, time_delta):
        dx, dy = self.x, self.y
        self.x += (right - left) * self.speed * time_delta
        self.y += (down - up) * self.speed * time_delta

        dx = self.x - dx
        dy = self.y - dy

        self.angle = math.atan2(dy, dx)

    def set_size(self, new_radius):
        self.radius = new_radius

    def reset_size(self):
        self.radius = self.original_radius

    def set_speed(self, new_speed):
        self.speed = new_speed

    def reset_speed(self):
        self.speed = self.original_speed

    def draw(self, screen, color):
        position = (int(self.x), int(self.y))

        pygame.draw.circle(screen, color, position, int(self.radius), 0)
        pygame.draw.circle(screen, (0, 0, 0), position, int(self.radius), 2)
        pygame.draw.circle(screen, (0, 0, 0), position, int(self.radius - 5), 2)
        pygame.draw.circle(screen, (0, 0, 0), position, int(self.radius - 10), 2)
        if self.shield:
            pygame.draw.circle(screen, (0, 255, 255), position, int(self.radius + 5), 3)

    def get_pos(self):
        return self.x, self.y

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y

    def collides_with_powerup(self, powerup):
        distance = ((self.x - powerup.x) ** 2 + (self.y - powerup.y) ** 2) ** 0.5
        return distance < (self.radius + powerup.radius)
