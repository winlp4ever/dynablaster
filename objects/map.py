from objects.sizeable import Sizeable
from objects.pave import Pave
from objects.wall import Wall
from objects.cell import Cell
import numpy as np


class Map(Sizeable):
    def __init__(self, mapcode):
        self.events = []
        assert isinstance(mapcode, np.ndarray)
        self.rows, self.cols = mapcode.shape
        self.labyrinth = np.empty_like(mapcode, dtype=object)
        for i in range(self.rows):
            for j in range(self.cols):
                self.labyrinth[i, j] = Pave() if mapcode[i, j] == 0 else Wall()

    def _set_cell_coords(self, i, j):
        assert 0 <= i < self.rows and 0 <= j < self.cols
        self.labyrinth[i, j]._set_pos(self.w / self.cols * (j + 0.5), self.h / self.rows * (i + 0.5))
        self.labyrinth[i, j]._set_size(self.h / self.rows, self.w / self.cols)

    def _set_all_cell_coords(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self._set_cell_coords(i, j)

    def _rendered(self, screen, **kwargs):
        for i in range(self.rows):
            for j in range(self.cols):
                self.labyrinth[i, j]._rendered(screen, **kwargs)

    def __getitem__(self, ind):
        return self.labyrinth[ind]
