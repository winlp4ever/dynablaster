from objects.cell import Cell

class Wall(Cell):
    def __init__(self, destructible):
        super(Cell, self).__init__(False)
        self.destructible = destructible

    def _boomed(self):
        if self.destructible:
            self.passable = True

    def _rendered(self, **kwargs):
        pygame.draw.rect(screen, rect=[self.x - self.w / 2, self.y - self.h / 2, self.h, self.w], **kwargs)


class WoodWall(Wall):
    def __init__(self):
        super(WoodWall, self).__init__(True)


class StoneWall(Wall):
    def __init__(self):
        super(StoneWall, self).__init__(False)


if __name__ == '__main__':
    w = WoodWall()
    print(w.destructible)
