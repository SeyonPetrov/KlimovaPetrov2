from pygame import *


class Camera:
    def __init__(self):
        self.new_x = 0

    def shift(self, obj):
        obj.rect.x += self.new_x * (1 / 10)

    def target(self, target, orient):
        self.new_x = (target.rect.x + target.rect.w // 2 - 1080 // 2) * orient
