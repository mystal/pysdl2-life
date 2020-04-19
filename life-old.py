#!/usr/bin/env python2
import pygame

import copy
import random
import sys
import time

def main(stepTime=1, width=100, height=100):
    pygame.init()

    oldGrid = [[False for x in xrange(width)] for y in xrange(height)]
    grid = [[bool(random.randint(0, 1)) for x in xrange(width)] for y in xrange(height)]

    screen = pygame.display.set_mode((400, 400))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

        oldGrid = copy.deepcopy(grid)

        screen.fill((255, 255, 255))
        for j in xrange(height):
            for i in xrange(width):
                neighborCount = _countNeighbors(oldGrid, i, j)
                if 2 < neighborCount < 5:
                    grid[j][i] = True
                    #TODO draw black
                else:
                    grid[j][i] = False
        pygame.display.flip()

        time.sleep(stepTime)

def _countNeighbors(grid, x, y):
    pass

if __name__ == "__main__":
    main()
