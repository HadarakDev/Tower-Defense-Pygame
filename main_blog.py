import pygame
from GameInformation import *
from Monster import *
from Tower import *
from display_blog import *


def clear_projectiles(building_list):
    for b in building_list:
        for p in b.projectile_list:
            if p.hit_status == True:
                b.projectile_list.remove(p)

def clear_monsters(monster_list):
    for m in monster_list:
        if m.health <= 0:
            monster_list.remove(m)



# Get the list of monsters which are in the range of each tower.
def get_targeatable_monsters(monster_list, building_list):
    for b in building_list:
        b.targetable = []
        for m in monster_list:
            if b.hitbox.check_collide(m.hitbox) == True:
                b.targetable.append(m)

# Get the target for each tower in the list of targetable monsters.
def current_tower_target(building_list):
    for b in building_list:
        for m in b.targetable:
            if b.current_target == None:
               b.current_target = m

            if b.current_target.pos_x <= m.pos_x:
                b.current_target = m

        if len(b.targetable) == 0:
           b.current_target = None


# Function which check if  escape or red cross are pressed and quit the game.
def check_input_exit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

def move_monsters(monster_list):
    for monster in monster_list:
        monster.move()

def shoot_towers(building_list):
    for b in building_list:
        points = b.shoot()


if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock()

    GameInfo = GameInformation(100, 100, 1920, 1080)

    win = pygame.display.set_mode((GameInfo.screen_X, GameInfo.screen_Y)) # Create a pygame Game Window with size 1920 x 1080

    background_image = pygame.image.load("images/map_blog.png").convert() # Load an image with pygame

    background_image_scale = pygame.transform.scale(background_image, (GameInfo.screen_X, GameInfo.screen_Y)) # Scale the image to 1920 x 1080

    # list which will contains all monsters entities
    monster_list = []

    # create 2 monsters entities
    first_monster = Monster(10, 3, 5, 1250, 450, 50, 80)
    second_monster = Monster(10, 3, 2, 1500, 750, 50, 80)

    # add entities into the list
    monster_list.append(first_monster)
    monster_list.append(second_monster)

    building_list = []
    tower_1 = Tower(1000, 300, 10, 60, 400)
    building_list.append(tower_1)

    while True: # Infinite Game Loop

        # for b in building_list:
        #     print(len(b.projectile_list))





        clock.tick(30)
        check_input_exit() # Call Function to quit with escape or red cross

        win.blit(background_image, (0, 0)) # Display the background image

        display_hud(win, GameInfo)
        get_targeatable_monsters(monster_list, building_list)
        current_tower_target(building_list)

        shoot_towers(building_list)
        move_monsters(monster_list)


        display_monster_placeholder_and_hitbox(win, monster_list)
        display_building_placeholder_and_hitbox(win, building_list)
        display_projectiles(win, building_list)
        clear_projectiles(building_list)
        clear_monsters(monster_list)

        # dest = (first_monster.pos_x + first_monster.size_x / 2, first_monster.pos_y + first_monster.size_y / 2)
        # src = (tower_1.pos_x, tower_1.pos_y)
        # points = calculate_points_projectile(src, dest, 8)

        pygame.draw.rect(win, (255, 255, 0), (first_monster.pos_x + first_monster.size_x / 2, first_monster.pos_y + first_monster.size_y / 2, 5, 5))

        # points = calculate_points_projectile(src, dest, 8)
        # for p in points:
        #     pygame.draw.rect(win, (255, 0, 0), (p[0], p[1], 5, 5))

        pygame.display.flip() # Update the display on the window