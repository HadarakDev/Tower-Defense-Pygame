from Collide import *

class Monster:
    def __init__(self, health, attack_damage, spd, pos_x, pos_y, size_x, size_y):
        self.health = health
        self.attack_damage = attack_damage
        self.spd = spd # movement speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.hitbox = Collide(pos_x, pos_y, size_x, size_y)

    def move(self):
        self.pos_x = self.pos_x - self.spd
        # update_hitbox
        self.hitbox.update_rect(self.pos_x, self.pos_y)

