from pygame.rect import Rect

class Collide:
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.hitbox_rect = Rect(pos_x, pos_y, size_x, size_y) # rectangle hitbox

    # Update the rectangle hitbox
    def update_rect(self, pos_x, pos_y):
        self.hitbox_rect = Rect(pos_x, pos_y, self.size_x, self.size_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    # check if this object collide with another one
    def check_collide(self, entity):
        if self.hitbox_rect.colliderect(entity.hitbox_rect) == True:
            return True
        else: 
            return False