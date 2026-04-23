import pygame
import sys

_screen = None
_clock = None
_run = False

def init(width = 512, height = 512):
    global _screen, _clock, _run

    pygame.init()
    _screen = pygame.display.set_mode((width, height))
    _clock = pygame.time.Clock()
    _run = True

def quit():
    pygame.quit()
    sys.exit()

def run(update, draw, target_fps = 60):
    global _run, _clock, _screen

    while _run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _run = False

        dt = _clock.tick(target_fps) / 1000

        update(dt)

        _screen.fill((0, 0, 0)) # clear to black
        draw(_screen)

        pygame.display.flip()

