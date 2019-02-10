class Sizeable(object):
    # sizeable objects
    def __init__(self):
        self.w = self.h = self.x = self.y = 0

    def _set_pos(self, x, y):
        self.x = x
        self.y = y

    def _set_size(self, width, height):
        self.w = width
        self.h = height

    def _get_pos(self):
        return self.x, self.y

    def _get_size(self):
        return self.w, self.h
