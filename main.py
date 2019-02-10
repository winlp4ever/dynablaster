import time
import pygame
import sys

from objects.character import Character
from cell import Cell

keymap = {pygame.K_w: 'w', pygame.K_d: 'd'}

def detect_click():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            key = event.key
            return key if key in keymap.keys() else None


def main():
    # init pygame env
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    # init game
    cell = Cell(True)
    player = Character(cell)
    events = []

    while True:
        pressed = detect_click()
        if pressed is not None:
            key = keymap[pressed]
            if key == 'd':
                events.append(player._drop_bomb(cell))
            elif key == 'w':
                player._move()
        new_events = []
        for event in events:
            b = event._passive_act()
            if b:
                new_events.append(event)
        events = new_events
        time.sleep(0.01)


if __name__ == '__main__':
    main()
