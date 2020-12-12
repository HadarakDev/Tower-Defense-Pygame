import pygame
from Collide import *


class Projectile:
    def __init__(self, x, y, target, damage):
        self.pos_x = x
        self.pos_y = y
        self.target = target
        self.damage = damage
        self.hitbox = Collide(self.pos_x, self.pos_y, 40, 40)
        self.hit_status = False

        dest = (self.target.pos_x + self.target.size_x / 2, self.target.pos_y + self.target.size_y / 2)
        src = (self.pos_x, self.pos_y)
        self.path = self.calculate_points_projectile(src, dest, 5)
        self.path_idx = 0

    # Calculate a list of point within the tower and the target.
    def calculate_points_projectile(self, src, dest, count):
        points = []
        dX = dest[0] - src[0]
        dY = dest[1] - src[1]
        interval_X = dX / (count + 1)
        interval_Y = dY / (count + 1)
        for i in range(count):
            points.append((src[0] + interval_X * i, src[1] + interval_Y * i))
        return points

    # Move the projectile to the next point in the projectile path list.
    def move_to_target(self):
        # if the list does not contains enough points it will recalculate the next one.
        if self.path_idx >= len(self.path):
            dest = (self.target.pos_x + self.target.size_x / 2, self.target.pos_y + self.target.size_y / 2)
            src = (self.pos_x, self.pos_y)
            self.path = self.calculate_points_projectile(src, dest, 2)
            self.path_idx = 1
        self.pos_x = self.path[self.path_idx][0]
        self.pos_y = self.path[self.path_idx][1]
        self.path_idx += 1
        self.hitbox.update_rect(self.pos_x, self.pos_y)


    # check if the projectile hit the target and set the status to True
    def hit_target(self):
        if self.hitbox.check_collide(self.target.hitbox) == True:
            self.target.health -= self.damage
            self.hit_status = True

