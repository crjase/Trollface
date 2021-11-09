import pygame
import sys
import ctypes
import threading
import time


# Initializations
pygame.init()
clock = pygame.time.Clock()
pygame.mixer.init()

# Screensize
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Image loading
image = pygame.image.load('Image.jpg')
image = pygame.transform.scale(image, (screensize))


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


pygame.mixer.music.load('Audio.mp3')
pygame.mixer.music.play()


def timer():
    count = 0
    while True:
        count += 1
        time.sleep(1)
        if count >= 60:
            break
    global running
    running = False
threading.Thread(target=(timer)).start()


running = True
while running:


    screen.blit(image, (0, 0))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False


    clock.tick(60)
    pygame.display.update()

sys.exit()