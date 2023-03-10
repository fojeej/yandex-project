import pygame
from random import randint
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

lives = 3
score = 0


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(pygame.image.load('data/background.jpg'), (WIDTH, HEIGHT))
    window.blit(fon, (0, 0))
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 30)

    im = pygame.image.load('data/icon.png')
    window.blit(im, (380, HEIGHT - 450))

    string_render = font1.render('Brave Bird', 1, pygame.Color('black'))
    window.blit(string_render, (250, HEIGHT - 400))

    string_render = font2.render('нажмите любую клавишу, чтобы начать игру', 1, pygame.Color('LightSkyBlue'))
    window.blit(string_render, (200, HEIGHT - 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


def game_over(scores):
    scores = score
    fon = pygame.transform.scale(pygame.image.load('data/background.jpg'), (WIDTH, HEIGHT))
    window.blit(fon, (0, 0))
    font1 = pygame.font.Font(None, 80)
    font2 = pygame.font.Font(None, 50)

    string_rendered = font1.render('Game Over', 1, pygame.Color('black'))
    window.blit(string_rendered, (250, HEIGHT - 500))

    string_rendered = font2.render('Очки: ' + str(scores), 1, pygame.Color('DimGray'))
    window.blit(string_rendered, (50, HEIGHT - 100))

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

fall_snd = pygame.mixer.Sound('sounds/fall.wav')

pygame.display.set_caption('Brave Bird')
pygame.display.set_icon(icon_img)

p, s, a = HEIGHT // 2, 0, 0
player = pygame.Rect(WIDTH // 3, p, 43, 43)
frame = 0

status = 'start'
time = 10

pipes = []
bgs = []
crash_pipes = []

speed = 3
gate_size = 200
gate_pos = HEIGHT // 2

bgs.append(pygame.Rect(0, 0, 101, 350))

start_screen()
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    press = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()
    click = press[0] or keys[pygame.K_SPACE]

    if time > 0:
        time -= 1

    frame = (frame + 0.2) % 3

    for i in range(len(bgs) - 1, -1, -1):
        n_bg = bgs[i]
        n_bg.x -= speed // 2

        if n_bg.right < 0:
            bgs.remove(n_bg)

        if bgs[-1].right <= WIDTH:
            bgs.append(pygame.Rect(bgs[-1].right, 0, 640, 980))

    for i in range(len(pipes) - 1, -1, -1):
        pipe = pipes[i]
        pipe.x -= speed

        if pipe.right < 0:
            pipes.remove(pipe)
            if pipe in crash_pipes:
                crash_pipes.remove(pipe)

    if status == 'start':
        if click and time == 0 and len(pipes) == 0:
            status = 'play'

        p += (HEIGHT // 2 - p) * 0.1
        player.y = p

    elif status == 'play':
        if click:
            a = -2
        else:
            a = 0

        p += s
        s = (s + a + 1) * 0.98
        player.y = p

        if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
            pipes.append(pygame.Rect(WIDTH, 0, 52, gate_pos - gate_size // 2))
            pipes.append(pygame.Rect(WIDTH, gate_pos + gate_size // 2, 52, HEIGHT - gate_pos + gate_size // 2))

            gate_pos += randint(-100, 100)
            if gate_pos < gate_size:
                gate_pos = gate_size
            elif gate_pos > HEIGHT - gate_size:
                gate_pos = HEIGHT - gate_size

        if player.top < 0 or player.bottom > HEIGHT:
            status = 'fall'

        for pipe in pipes:
            if player.colliderect(pipe):
                status = 'fall'

            if pipe.right < player.left and pipe not in crash_pipes:
                crash_pipes.append(pipe)
                score += 5
                speed = 3 + score // 100
    elif status == 'fall':
        fall_snd.play()
        s, a = 0, 0
        gate_pos = HEIGHT // 2

        lives -= 1
        if lives > 0:
            status = 'start'
            time = 60
        else:
            status = 'game over'
            time = 120
    else:
        game_over(score)

        # Отрисовка
        window.fill(pygame.Color('black'))
        for bg in bgs:
            window.blit(background_img, bg)
        for pipe in pipes:
            if pipe.y == 0:
                rect = pipe_top_img.get_rect(bottomleft=pipe.bottomleft)
                window.blit(pipe_top_img, rect)
            else:
                rect = pipe_bottom_img.get_rect(topleft=pipe.topleft)
                window.blit(pipe_bottom_img, rect)

        image = bird_img.subsurface(43 * int(frame), 0, 43, 43)
        image = pygame.transform.rotate(image, -s * 2)
        window.blit(image, player)

        text = font1.render('Очки: ' + str(score), 1, pygame.Color('black'))
        window.blit(text, (10, 10))

        text = font1.render('Жизни: ' + str(lives), 1, pygame.Color('black'))
        window.blit(text, (10, HEIGHT - 30))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
