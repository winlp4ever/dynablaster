import time
import pygame
from objects.sizeable import Sizeable
from objects.passiveAction import PassiveAction
import objects.utils as utils

class Bomb(Sizeable, PassiveAction): # level 2
    def __init__(self, duration=2):
        super(Bomb, self).__init__()
        self.duration = duration

    def _dropped(self, cell):
        self._set_pos(cell.x, cell.y)
        self._set_size(cell.w, cell.h)
        self.timeset = time.time()

    def _boom(self):
        if time.time() - self.timeset >= self.duration:
            print('BOOM')
            return True
        return False

    def _passive_act(self):
        return not self._boom()

    def _rendered(self, screen, **kwargs):
        utils.drawCircle(screen, pos=[int(self.x), int(self.y)], radius=int(self.w / 2), **kwargs)
