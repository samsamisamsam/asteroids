import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    # Create empty groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while True:
        # Check if user has clicked exit window button, then returns (which auto calls display.quit())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for ast in asteroids:
            if ast.is_colliding(player):
                print("Game over!")
                return
            
        for ast in asteroids:
            for bullet in shots:
                if ast.is_colliding(bullet):
                    ast.split()
                    bullet.kill()

        screen.fill(000000)

        for obj in drawable:
            obj.draw(screen)
        
        # Updates screen's content
        pygame.display.flip()

        # Limits game to 60 fps and stores the time passed since last call in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
