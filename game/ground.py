import pygame
import os

img_ground = pygame.transform.scale2x(pygame.image.load(os.path.join("game/graphics", "ground.png")).convert_alpha())


class Ground:
    VELOCITY = 5
    IMG = img_ground
    WIDTH = img_ground.get_width()

    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    # Moving ground to the left
    def move(self):
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    # Drawing a floor
    def draw(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))
