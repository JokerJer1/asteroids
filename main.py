# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from asteroid import *
import sys
from shot import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #instantiate screen and game clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    

    #instantiate player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    

    #add player to groups
    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    Shot.containers = (shots, drawable, updatable)


    

    asteroid_field = AsteroidField()

    #instantiate player
    player = Player( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    #infinite game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        for things in drawable:
            things.draw(screen)
        
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
