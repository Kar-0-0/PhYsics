import math
import sys

import pygame

pygame.init()

width, height = 1080, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PhYsics")
clock = pygame.time.Clock()

game = True

gravity = 0.5  # Movement along the y-axis

circlex = 540  # Circle x pos
circley = 200  # Circle y pos
r, g, b = 255, 255, 255  # RGB values of the circle

left_click = False  # Doesn't drop if circle is on the screen


def drop():
    global circley, r, g, b, left_click, mouse_x
    if circley <= 814:
        gravity = 0.5
        circle = pygame.draw.circle(screen, (r, g, b), (mouse_x, circley), 100)
        r, g, b = 0, 0, 0
        circley += gravity
        if rect.colliderect(circle):
            circley -= gravity

    elif circley >= 814:
        r, g, b = 255, 255, 255
        circley = 200
        gravity = 0
        left_click = False


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    rect = pygame.draw.rect(screen, (0, 0, 0), (400, 500, 300, 10))

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        left_click = True
        mouse_x, mouse_y = pygame.mouse.get_pos()

    if left_click:
        drop()

    pygame.display.update()
