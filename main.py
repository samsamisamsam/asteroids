import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Check if user has clicked exit window button, then returns (which auto calls display.quit())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fills the screen with black
        pygame.Surface.fill(screen, 000000)
        # Updates screen's content
        pygame.display.flip()

if __name__ == "__main__":
    main()
