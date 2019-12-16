import pygame
import os

img_bird = [pygame.transform.scale2x(pygame.image.load(os.path.join("game/graphics", "bird" + str(x) + ".png")))
            for x in range(1, 4)]


def blit_rotate_center(surface, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)

    surface.blit(rotated_image, new_rect.topleft)


class Bird:
    MAX_ROTATION = 25
    BIRDS = img_bird
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.BIRDS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        displacement = self.vel * self.tick_count + 0.5 * 3 * self.tick_count ** 2

        if displacement >= 16:
            displacement = (displacement / abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.BIRDS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.BIRDS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.BIRDS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.BIRDS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.BIRDS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.BIRDS[1]
            self.img_count = self.ANIMATION_TIME * 2

        blit_rotate_center(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)
