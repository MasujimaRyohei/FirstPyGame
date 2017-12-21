#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCREEN_SIZE = (640, 480)

# Initializing pygame
pygame.init()

# Make window(SCREEN_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Set string of title ber
pygame.display.set_caption(u"MAKE A WINDOW")

# Main game loop
while True:
    # Filling window blue
    screen.fill((0,0,255))

    # Update window
    pygame.display.update()

    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
