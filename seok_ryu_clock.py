# -*- coding: utf-8 -*-

import pygame
from math import pi, cos, sin, radians
import datetime
from pygame import gfxdraw

WIDTH, HEIGHT = 1920, 1080
center = (WIDTH / 2, HEIGHT / 2)
clock_radius = 400

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Thảo Nguyên Clock")
clock = pygame.time.Clock()
FPS = 60

CLOCK = (33,35,57)
BACKGROUND = (217,215,211)
RED = (255, 0, 0)
YELLOW = (196,166,0)

fonts = pygame.font.get_fonts()
print(fonts)


def numbers(number, size, position):
    font = pygame.font.Font("Dubai-Regular.ttf", size)
    text = font.render(number, True, CLOCK)
    text_rect = text.get_rect(center=(position))
    screen.blit(text, text_rect)

def write_text(text, size, position, font_file, text_rotate_degrees=0, align="center"):
    font = pygame.font.Font(font_file, size)
    text_surface = font.render(text, True, CLOCK)

    if text_rotate_degrees != 0:
        text_surface = pygame.transform.rotate(text_surface, text_rotate_degrees)

    text_rect = text_surface.get_rect()

    if align == "right":
        text_rect.topright = position
    elif align == 'left':
        text_rect.topleft = position
    else:
        text_rect.center = position
    screen.blit(text_surface, text_rect)


def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + WIDTH / 2, -(y - HEIGHT / 2)


def main():
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill(BACKGROUND)

        # draw circles
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 10, 5)

        outer_radius = clock_radius - 2
        pygame.draw.circle(screen, CLOCK, center, outer_radius, 2)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius + 1, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius, CLOCK)
        gfxdraw.aacircle(screen, int(center[0]), int(center[1]), outer_radius - 1, CLOCK)

        # 24h
        for number in range(1, 25):
            numbers(str(number), 40, polar_to_cartesian(clock_radius + 30, number * 15))

    
        # hour hooks
        for number in range(0, 360, 15):
            width = 3
            if (number % 90) == 0:
                width = 6
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius + 8, number), polar_to_cartesian(clock_radius - 22, number), width)


        # draw dividing lines
        rb = 15
        thetas = [-2*rb,5.5*rb,6.8*rb,17.2*rb,17.5*rb,20.5*rb]
        for theta in thetas:
            pygame.draw.line(screen, CLOCK, polar_to_cartesian(clock_radius - 30, theta), polar_to_cartesian(clock_radius - 335, theta), 2)
        image_path = "1HoonSaemaulundong/pngtree-cartoon-moon-cloud-free-illustration-image_1371955.jpg"
        image = pygame.image.load(image_path)
        image_width, image_height = 200, 200  # Kích thước mới
        image = pygame.transform.scale(image, (image_width, image_height))
        image_x = WIDTH / 2.05 - image_width / 2  # Căn giữa theo chiều ngang
        image_y = HEIGHT / 4 - image_height / 2
        screen.blit(image,(image_x, image_y))
        write_text(u"Thế giới giấc mơ", 50, (WIDTH / 2 + 200, HEIGHT / 2 - 150), "1HoonSaemaulundong\DFVN ED Lavonia.ttf")
        write_text(u"Dậy và đi học", 40, (WIDTH / 2 + 350, HEIGHT / 2 - 40), "1HoonSaemaulundong\DFVN ED Lavonia.ttf", 7, 'right')
        write_text(u"Đi học ", 100, (WIDTH / 2 + 150, HEIGHT / 2 + 130), "1HoonSaemaulundong\DFVN ED Lavonia.ttf", 360, 'right')
        image_TC = "1HoonSaemaulundong/TC.png" 
        image = pygame.image.load(image_TC)
        image_width, image_height = 100, 100  # Kích thước mới
        image_TC = pygame.transform.scale(image, (image_width, image_height))
        image_x = WIDTH / 1.65 - image_width / 2  # Căn giữa theo chiều ngang
        image_y = HEIGHT / 1.48 - image_height / 2
        screen.blit(image_TC,(image_x, image_y))
        write_text(u"Đồng hồ thời gian của Thảo Nguyên ", 50, (WIDTH / 2 + 950, HEIGHT / 2 + 450), "1HoonSaemaulundong\DFVN ED Lavonia.ttf", 360, 'right')
        write_text(u"cho bo ", 10, (WIDTH / 2 - 200, HEIGHT / 2 + 28 ), "Cyberbit.ttf", -350, 'right')
        write_text(u"Đi học Thăng Long", 35, (WIDTH / 2 - 80, HEIGHT / 2 - 110), "1HoonSaemaulundong\DFVN ED Lavonia.ttf", 360-10, 'right')
        write_text(u"Ở nhà", 40, (WIDTH / 2 - 103, HEIGHT / 2 - 220), "1HoonSaemaulundong\DFVN ED Lavonia.ttf", 360-47, 'right')

        current_time = datetime.datetime.now()
        second = current_time.second
        minute = current_time.minute
        hour = current_time.hour

        r = 130
        theta = (hour + minute / 60 + second / 3600) * (360 / 24)
        pygame.draw.line(screen, CLOCK, center, polar_to_cartesian(r, theta), 14)

        
        r = 280
        theta = (minute + second / 60) * (360 / 60)
        pygame.draw.line(screen, CLOCK, center, polar_to_cartesian(r, theta), 10)

        r = 340
        theta = second * (360 / 60)
        pygame.draw.line(screen, YELLOW, center, polar_to_cartesian(r, theta), 4)
        pygame.draw.line(screen, YELLOW, center, polar_to_cartesian(80, (theta + 180) % 360), 4)



        # play button
        gfxdraw.filled_circle(screen, int(center[0]), int(center[1]), clock_radius - 350, YELLOW)
        pygame.draw.circle(screen, CLOCK, center, clock_radius - 350 - 1, 2)
        write_text("PLAY", 46, (WIDTH/2, HEIGHT/2 + 3), "calibri-font-family\calibri-bold.ttf")

        pygame.display.update()

        clock.tick(FPS)

    pygame.quit()

main()
