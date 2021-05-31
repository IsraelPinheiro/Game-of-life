import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/self.scale)
        self.rows = int(width/self.scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=self.size)
        self.offset = offset

    def random_2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)

    def clean_2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 0

    def full_2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 1

    def conway(self, off_color, on_color, surface, paused=False):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface,on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface,off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])


        if not paused:
            next = np.ndarray(shape=self.size)
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neigbors = self.get_neigbors(x, y)
                    if state == 0 and neigbors == 3:
                        next[x, y] = 1
                    elif state == 1 and (neigbors<2 or neigbors>3):
                        next[x, y] = 0
                    else:
                        next[x, y] = state

            self.grid_array = next

    def get_neigbors(self, x, y):
        total = 0
        for n in range(-1,2):
            for m in range(-1,2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total

