import pygame
import os, sys
from grid import Grid
import pyautogui

os.environ["SDL_VIDEO_CENTERED"] = "1"

size = WIDTH, HEIGHT = pyautogui.size()

#Colors dfinition
BLACK = (0,0,0)
GRAY_25 = (63,63,63)
GRAY_50 = (127,127,127)
GRAY_75 = (191,191,191)
WHITE = (255,255,255)
BLUE = (0,14,71)

pygame.init()
pygame.display.set_caption("Conway's Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

scale = 15
offset = 1

run = True
pause = False

grid = Grid(width=WIDTH, height=HEIGHT, scale=scale, offset=offset)
grid.random_2d_array()

while run:
    if pause == False:
        clock.tick(fps)
        screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: #Space - Pause the game on the current state
                pause = not pause
            if event.key == pygame.K_f: #F - Set the board to a full array and pauses it
                grid.full_2d_array()
                pause = True
            if event.key == pygame.K_c: #C - Set the board to a clean array and pauses it
                grid.clean_2d_array()
                pause = True
            if event.key == pygame.K_r: #R - Set the board to a random state and unpauses it if paused
                grid.random_2d_array()
                pause = False
            if event.key == pygame.K_i: #I - Reverses the board and pauses the game
                grid.reverse_array()
                pause = False

            if event.key == pygame.K_x: #X - Quit
                pygame.quit()

        if pause:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                clicked_pos_x = int(mouse_pos_x/scale)
                clicked_pos_y = int(mouse_pos_y/scale)
                grid.grid_array[clicked_pos_x][clicked_pos_y] = 1 - grid.grid_array[clicked_pos_x][clicked_pos_y]
            
    grid.conway(off_color=WHITE, on_color=BLUE, surface=screen, paused=pause)
    pygame.display.update()

pygame.quit()