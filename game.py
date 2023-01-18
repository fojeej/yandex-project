import pygame
from random import randint
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

color = ''

live = 3
score = 0

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
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 50)

    string_render = font1.render('Game Over', 1, pygame.Color('black'))
    window.blit(string_render, (250, HEIGHT - 500))

    string_render = font2.render('Очки: ' + str(scores), 1, pygame.Color('grey'))
    window.blit(string_render, (50, HEIGHT - 100))

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

pygame.mixer.music.load('sounds/music.wav')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

fall_wav = pygame.mixer.Sound('sounds/fall.wav')

pygame.display.set_caption('Brave Bird')
pygame.display.set_icon(icon_img)

p, s, a = HEIGHT // 2, 0, 0
play_er = pygame.Rect(WIDTH // 3, py, 43, 43)
fr = 0

stat = 'start'
time = 10

pipe_s = []
bg = []
crash_pipes = []

speed = 3
gate_size = 200
gate_pos = HEIGHT // 2

bg.append(pygame.Rect(0, 0, 77, 266))

start_screen()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = press[0] or keys[pygame.K_SPACE]
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
