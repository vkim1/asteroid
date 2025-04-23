import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        for any in asteroids:
            if player.collision_check(any):
                print("Game over!")
                pygame.exit()
            for bullet in shots:
                if bullet.collision_check(any):
                    any.split()
                    bullet.kill()




        

if __name__== "__main__":
    main()
