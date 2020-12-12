from Collide import *
from Projectile import *


class Tower:
    def __init__(self, x, y, hp, cd, range):
        self.pos_x = x
        self.pos_y = y
        self.size_x = 80
        self.size_y = 100
        self.range = range
        self.health = hp
        self.hitbox = Collide(self.pos_x - (self.range - self.size_x) / 2, self.pos_y - (self.range - self.size_y) / 2,
                              self.range, self.range)
        self.targetable = []  # list of all monsters in range
        self.current_target = None  # the current target monster
        self.current_cd = 0
        self.cd = cd
        self.projectile_list = []

    def check_cd(self):
        # Check the cooldown
        if self.current_cd > 0:
            return False
        return True

    def shoot(self):
        if self.check_cd() and self.current_target != None:
            self.projectile_list.append(Projectile(self.pos_x + self.size_x /2, self.pos_y + self.size_y /2, self.current_target, 10))
            self.current_cd = self.cd
        else:
            self.current_cd -= 1
        for p in self.projectile_list:
            if self.current_target != None:
                p.move_to_target() # move the projectile to the target
                p.hit_target() # check if the projectile hit the target


