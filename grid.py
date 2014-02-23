from sdl2 import *

import copy
import random

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.x = 0
        self.y = 0

        self.grid = None
        self.oldGrid = None

        self.clear()

    def step(self):
        self.oldGrid = copy.deepcopy(self.grid)

        for j in range(self.height):
            for i in range(self.width):
                neighborCount = self._countNeighbors(i, j)
                if self.grid[j][i]:
                    self.grid[j][i] = 2 <= neighborCount <= 3
                else:
                    self.grid[j][i] = neighborCount == 3

    def draw(self, renderer, w, h):
        rect = SDL_Rect()
        rect.w = w//self.width
        rect.h = h//self.height

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        for j in range(self.height):
            for i in range(self.width):
                rect.x = i * rect.w
                rect.y = j * rect.h
                if self.grid[j][i]:
                    SDL_RenderFillRect(renderer, rect)
                if i == self.x and j == self.y:
                    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 127);
                    SDL_RenderFillRect(renderer, rect)
                    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);

    def randomize(self):
        self.grid = [[bool(random.randint(0, 1)) for x in range(self.width)]
                for y in range(self.height)]

    def clear(self):
        self.grid = [[False for x in range(self.width)]
                for y in range(self.height)]

    def toggleCell(self, x, y):
        self.grid[y][x] = not self.grid[y][x]

    def checkPoint(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)

    def getNeighbors(self, x, y):
        neighbors = []

        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if (x != i or y != j) and self.checkPoint(i, j) and self.oldGrid[j][i]:
                    neighbors.append((i, j))

        return neighbors

    def _countNeighbors(self, x, y):
        neighbors = self.getNeighbors(x, y)
        return sum([self.oldGrid[y][x] for x, y in neighbors])
