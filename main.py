import os
import random
import pygame
pygame.init()
__version__ = 0.1

# settings

window_res = window_width, window_height = 3440, 1440
tittle = f"PutinGame v{__version__}"
bg_color = (0, 0, 0)
fps = 60
objects_filename_list = ["putin.png", "putin_2.png"]
objects_count = 50
texture_size = 128, 128


window = pygame.display.set_mode(window_res)
pygame.display.set_caption("PUTIN_ZZZZZ")
window.fill(bg_color)
game_run = True
clock = pygame.time.Clock()


class GameObject:
    def __init__(self, x, y, vel_x, vel_y, texture="putin.png"):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, texture_size)
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def check_cord(self):
        if self.x < 0 or self.x + self.texture.get_width() > window.get_width():
            self.vel_x *= -1
            return False
        if self.y < 0 or self.y + self.texture.get_height() > window.get_height():
            self.vel_y *= -1
            return False

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.check_cord()

        window.blit(self.texture, [self.x, self.y])

    def rand_generate(self):
        self.x = random.randint(0, window.get_width() - self.texture.get_width())
        self.y = random.randint(0, window.get_height() - self.texture.get_height())
        self.vel_x = random.randrange(2, 4)
        self.vel_y = random.randrange(2, 4)


def generate_game_object() -> GameObject:
    img = random.choice(objects_filename_list)
    if not img in os.listdir():
        print(f"файл {img} не найден")
        raise FileNotFoundError
    g = GameObject(x=0,
                   y=0,
                   vel_x=3,
                   vel_y=3,
                   texture=img)
    g.rand_generate()
    return g


game_objects = [generate_game_object() for _ in range(objects_count)]


def parse_events():
    for event in pygame.event.get():
        # print(event)
        global game_run
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                game_run = False
            elif event.unicode == "r":
                print("R")
            elif event.key == 1073741891:
                pygame.display.set_mode((800, 600))
            elif event.key == 1073741892:
                pygame.display.set_mode((1920, 1000))
            print(event)


def game_update():
    for obj in game_objects:
        obj.update()


while game_run:
    clock.tick(fps)
    window.fill(bg_color)
    parse_events()
    game_update()
    pygame.display.update()
pygame.quit()
