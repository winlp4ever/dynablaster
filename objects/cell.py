from objects.sizeable import Sizeable


class Cell(Sizeable): # layer 1
    def __init__(self, passable):
        super(Cell, self).__init__()
        self.passable = passable

    def _is_passable(self):
        return self.passable
