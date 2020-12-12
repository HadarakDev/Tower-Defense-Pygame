import pygame





def display_text(win, text, x, y):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(text, False, (0, 0, 0))
    win.blit(textsurface, (x, y))


def display_building_hud():
    # type of tower + vitesse + show range
    print("test")
def display_hud(win, GameInfo):
    pygame.draw.rect(win, (120, 120, 120), (30, 30, 500, 100)) # Display a gray rectangle at (30 x 30),  size (500 x 100)
    pygame.draw.rect(win, (255, 255, 255), (30, 30, 500, 100), 3) # Create a Border

    # Money Info
    pygame.draw.rect(win, (255, 255, 0), (50, 55, 50, 50))
    display_text(win, str(GameInfo.money), 110, 60)

    # # HP Info
    pygame.draw.rect(win, (255, 0, 0), (200, 55, 50, 50))
    display_text(win, str(GameInfo.health), 260, 60)

    #Monsters Waves
    # Coming Soon


def display_projectiles(win, building_list):
    for b in building_list:
        for p in b.projectile_list:
            pygame.draw.rect(win, (120, 255, 120), (p.pos_x, p.pos_y, 10, 10))
            # win.blit(p.image, p.x, p.y)

# This Function display a rectangle placeholder at the location of each monster and the hitbox stored in collide class.
def display_monster_placeholder_and_hitbox(win, monster_list):
    for monster in monster_list:
        pygame.draw.rect(win, (255, 0, 255), (monster.pos_x, monster.pos_y, monster.size_x, monster.size_y)) # display placeholder
        pygame.draw.rect(win, [0, 0, 0], [monster.hitbox.pos_x, monster.hitbox.pos_y, monster.hitbox.size_x, monster.hitbox.size_y], 3) # display hitbox

def display_building_placeholder_and_hitbox(win, building_list):
    for building in building_list:
        pygame.draw.rect(win, (255, 255, 0), (building.pos_x, building.pos_y, building.size_x, building.size_y)) # display placeholder
        pygame.draw.rect(win, [255, 0, 0], [building.hitbox.pos_x, building.hitbox.pos_y, building.hitbox.size_x, building.hitbox.size_y], 3) # display hitbox
        #print(building.current_target)
