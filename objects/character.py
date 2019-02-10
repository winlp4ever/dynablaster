import readchar
import time

from objects.bomb import Bomb
from objects.sizeable import Sizeable
import objects.utils as utils


class Character(Sizeable): # layer 2
    def __init__(self, map):
        super(Character, self).__init__()
        self.alive = True
        self._set_pos(map[0, 0].x, map[0, 0].y)
        self._set_size(map[0, 0].w, map[0, 0].h)

    def _move(self):
        if self.alive:
            print('player on move.')
        else:
            print('dead already')

    def _get_killed(self):
        self.alive = False
        print('is dead!')

    def _drop_bomb(self, map):
        bomb = Bomb()
        cell = self._curr_cell(map)
        bomb._dropped(cell)
        print('drop bomb.')
        return bomb

    def _rendered(self, screen, **kwargs):
        utils.drawPolygon(screen, pointlist=[(self.x + self.w / 2, self.y + self.h / 2),
                                            (self.x - self.w / 2, self.y + self.h / 2),
                                            (self.x, self.y - self.h / 2)], **kwargs)

    def _curr_cell(self, map):
        return map[int(self.x * map.cols // map.w), int(self.y * map.rows // map.h)]
