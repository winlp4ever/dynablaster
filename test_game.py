import pygame
from objects.map import Map
from objects.character import Character
import numpy as np
import time
import json

with open('./settings.json', 'r') as f:
    settings = json.load(f)

pygame.init()

screen = pygame.display.set_mode(settings["screen_size"])
screen.fill(settings["background_color"])
code = np.zeros(shape=settings["map_size"])
map = Map(code)

map._set_size(*settings["screen_size"])
map._set_all_cell_coords()

player = Character(map)


keymap = {pygame.K_w: 'w', pygame.K_d: 'd'}

def detect_click():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); #sys.exit() if sys is imported
        if event.type == pygame.KEYDOWN:
            key = event.key
            return key if key in keymap.keys() else None

clock = pygame.time.Clock()
exit = False
events = []


while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    screen.fill(settings["background_color"])
    map._rendered(screen, **settings['pave']['rendering'])
    player._rendered(screen, **settings['character']['rendering'])

    pressed = detect_click()
    if pressed is not None:
        key = keymap[pressed]
        if key == 'd':
            events.append(player._drop_bomb(map))
        elif key == 'w':
            player._move()
    new_events = []
    for event in events:
        b = event._passive_act()
        event._rendered(screen, **settings['bomb']['rendering'])
        if b:
            new_events.append(event)
    events = new_events

    pygame.display.flip()

pygame.quit()
