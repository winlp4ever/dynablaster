from objects.cell import Cell
import pygame
import objects.utils as utils

color = [255, 255, 255]
class Pave(Cell):
    def __init__(self):
        super(Pave, self).__init__(True)

    def _rendered(self, screen, **kwargs):
        utils.drawRect(screen, rect=[self.x - self.w / 2, self.y - self.h / 2, self.w, self.h], **kwargs)
