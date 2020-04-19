from sdl2 import *

from grid import Grid
from input import Input

import ctypes

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

FPS = 60

def main(stepTime=0.1, width=50, height=50):
    SDL_Init(SDL_INIT_VIDEO|SDL_INIT_TIMER)
    window = SDL_CreateWindow(b'Life',
                              SDL_WINDOWPOS_UNDEFINED,
                              SDL_WINDOWPOS_UNDEFINED,
                              SCREEN_WIDTH,
                              SCREEN_HEIGHT,
                              SDL_WINDOW_SHOWN)
    renderer = SDL_CreateRenderer(window, -1, 0)

    SDL_ShowCursor(False)

    SDL_SetRenderDrawBlendMode(renderer, SDL_BLENDMODE_BLEND)

    # If you want fullscreen, borderless
    # make the scaled rendering look smoother
    #SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear")
    #SDL_RenderSetLogicalSize(renderer, SCREEN_WIDTH, SCREEN_HEIGHT)

    input = Input()

    grid = Grid(width, height)

    cellWidth = SCREEN_WIDTH//width
    cellHeight = SCREEN_HEIGHT//height

    event = SDL_Event()

    running = True
    simulate = False
    lastStepTime = SDL_GetTicks()
    while running:
        startTime = SDL_GetTicks()
        input.beginNewFrame()
        while SDL_PollEvent(ctypes.byref(event)):
            if event.type == SDL_QUIT:
                running = False
            if event.type == SDL_KEYDOWN:
                input.keyDownEvent(event)
            elif event.type == SDL_KEYUP:
                input.keyUpEvent(event)
            elif event.type == SDL_MOUSEBUTTONDOWN:
                input.buttonDownEvent(event)
            elif event.type == SDL_MOUSEBUTTONUP:
                input.buttonUpEvent(event)
            elif event.type == SDL_MOUSEMOTION:
                input.mouseMoveEvent(event)

        if input.wasKeyPressed(SDLK_ESCAPE):
            running = False

        if input.wasKeyPressed(SDLK_SPACE):
            simulate = not simulate

        if input.wasKeyPressed(SDLK_r):
            grid.randomize()
        if input.wasKeyPressed(SDLK_c):
            grid.clear()

        cellX = input.mouseX // cellWidth
        cellY = input.mouseY // cellHeight
        if (input.wasButtonPressed(SDL_BUTTON_LEFT) or
            (input.isButtonHeld(SDL_BUTTON_LEFT) and
             (grid.x != cellX or grid.y != cellY))):
            grid.toggleCell(cellX, cellY)
        grid.x = cellX
        grid.y = cellY

        currentTime = SDL_GetTicks()
        if simulate and (currentTime - lastStepTime >= 1000*stepTime):
            grid.step()
            lastStepTime = SDL_GetTicks()

        # Clear the window
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderClear(renderer);
        # Draw grid
        grid.draw(renderer, SCREEN_WIDTH, SCREEN_HEIGHT)
        # Flip window
        SDL_RenderPresent(renderer);

        msPerFrame = 1000 // FPS
        elapsedTime = SDL_GetTicks() - startTime
        if elapsedTime < msPerFrame:
            SDL_Delay(msPerFrame - elapsedTime)

    SDL_DestroyRenderer(renderer)
    SDL_DestroyWindow(window)
    SDL_Quit()

if __name__ == "__main__":
    main()
