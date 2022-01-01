from generate import make_map
import pygame
from typing import List
import sys

SMALL = 15
MEDIUM = 20
LARGE = 25

ICON_SIZE = 34
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 900
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)

WALL_W = 3
PATH_W = 30
# display the graphic
def display(map:List[List[int]]) -> None :

    pygame.init()
    # create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # title caption and icon 
    pygame.display.set_caption("maze")
    icon = pygame.image.load('image/icon.png')
    icon = pygame.transform.scale(icon, (ICON_SIZE, ICON_SIZE))
    pygame.display.set_icon(icon)

    # init variables
    menu = True
    size = None
    map = None

    # draw text
    def draw_text(text, text_rect, surface, x, y):
        text_rect.topleft = (x,y)
        surface.blit(text, text_rect)

   # show title 
    def draw_menu():
        # set size and pos for title
        t = pygame.image.load('image/title.jpg')
        t.set_colorkey(WHITE)
        x = (SCREEN_WIDTH - t.get_width()) // 2
        y = (SCREEN_HEIGHT - t.get_height()) // 4
        
        font = pygame.font.SysFont(None, 50)

        # set size and pos for the size of maze option 
        text_1 = font.render('small maze', 1, BLACK) 
        text_1_rect = text_1.get_rect()
        x_1= (SCREEN_WIDTH - text_1_rect.width) // 2
        y_1= (SCREEN_HEIGHT) // 1.5
        draw_text(text_1, text_1_rect, screen, x_1, y_1)

        text_2 = font.render('medium maze', 1, BLACK)
        text_2_rect = text_2.get_rect() 
        x_2 = (SCREEN_WIDTH - text_2_rect.width) // 2
        y_2 = y_1 + text_1_rect.height * 2
        draw_text(text_2, text_2_rect, screen, x_2, y_2)

        text_3 = font.render('large maze', 1, BLACK)
        text_3_rect = text_3.get_rect() 
        x_3 = (SCREEN_WIDTH - text_3_rect.width) // 2
        y_3 = y_2 + text_2_rect.height * 2
        draw_text(text_3, text_3_rect, screen, x_3, y_3)
        screen.blit(t, (x,y))

        return text_1_rect, text_2_rect, text_3_rect
    
    def drawMaze(map, size): 
        maze_size = (size+1)*WALL_W + size*PATH_W
        x_cor = (SCREEN_WIDTH - maze_size) // 2
        y_cor = (SCREEN_HEIGHT - maze_size) // 2
        screen.fill(BLACK)
        
        x_pos = x_cor
        y_pos = y_cor
        for ver in map:
            for snei in ver.select_nei:
                left_nei = False
                right_nei = False
                top_nei = False
                bottom_nei = False
                if snei.id == ver.id - 1:
                    left_nei = True
                if snei.id == ver.id + 1:
                    right_nei = True
                if snei.id == ver.id - size:
                    top_nei = True
                if snei.id == ver.id + size:
                    bottom_nei = True
            if not left_nei:
                # this is |
                pygame.draw.rect(screen, RED, (x_cor, y_cor, WALL_W, PATH_W))
            if not right_nei:
                pygame.draw.rect(screen, RED, (x_cor+WALL_W, y_cor, WALL_W, PATH_W))
            if not top_nei:
                # this is _
                pygame.draw.rect(screen, RED, (x_cor, y_cor, WALL_W, PATH_W))
            if not bottom_nei:
                pygame.djaw.rect(screen, RED, (x_cor, y_cor-WALL_W, PATH_W, WALL_W))
            x_cor = (ver.id % size) * (WALL_W + PATH_W)
            y_cor = (ver.id % size) * (WALL_W + PATH_W)
        # draw |
        pygame.draw.rect(screen, RED, (x_cor, y_cor, WALL_W, PATH_W))
    # menu loop
    while True:

        # if on menu screen
        if menu:
            # load screen color 
            screen.fill((234,225,176))
            # add title
            sm_mz, md_mz, lg_mz = draw_menu()
        # detect event
        else:
            drawMaze(map, size) 
        for event in pygame.event.get():

            # if quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:
                    pass
                if sm_mz.collidepoint(event.pos):
                    map = make_map(SMALL)
                    size = SMALL
                    menu = False
                    print("click small maze")
                    
                if md_mz.collidepoint(event.pos):
                    map = make_map(MEDIUM)
                    size = MEDIUM
                    menu = False
                    print("click medium maze")

                if lg_mz.collidepoint(event.pos):
                    map = make_map(LARGE)
                    size = LARGE
                    menu = False
                    print("click large maze")
        pygame.display.update()