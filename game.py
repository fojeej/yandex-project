import pygame
from random import randint
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(pygame.image.load('data/background.jpg'), (WIDTH, HEIGHT))
    window.blit(fon, (0, 0))
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 30)

    im = pygame.image.load('../pythonProject/data/icon.png')
    window.blit(im, (380, HEIGHT - 450))

    string_render = font1.render('Brave Bird', 1, pygame.Color('black'))
    window.blit(string_render, (250, HEIGHT - 400))

    string_render = font2.render('для того, чтобы начать нажмите пробел', 1, pygame.Color('LightSkyBlue'))
    window.blit(string_render, (200, HEIGHT - 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def game_over():
    fon = pygame.transform.scale(pygame.image.load('../pythonProject/data/end.jpeg'), (WIDTH, HEIGHT))
    window.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


font1 = pygame.font.Font(None, 35)
font2 = pygame.font.Font(None, 80)

background_img = pygame.image.load('data/background.jpg')
bird_img = pygame.image.load('data/bird.png')
pipe_top_img = pygame.image.load('data/pipe_top.png')
pipe_bottom_img = pygame.image.load('data/pipe_bottom.png')
icon_img = pygame.image.load('data/icon.png')


pygame.display.set_caption('Brave Bird')
pygame.display.set_icon(icon_img)


start_screen()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
