import pygame
import sys
from constants import *
from player import *
from asteroids import *
from asteroidfield import *

def main():
   print(f"Starting asteroids!")

   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")
   
   pygame.init()
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   asteroids = pygame.sprite.Group()
   
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   fpsClock = pygame.time.Clock()
   dt = 0

   Player.containers = (updatable, drawable)
   player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

   Asteroid.containers = (asteroids, updatable, drawable)
   AsteroidField.containers = (updatable)

   asteroid_field = AsteroidField()

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            print(f"Closing game!")
            return

      pygame.Surface.fill(screen, (0,0,0))
      
      for p in updatable:
         p.update(dt)

      for p in drawable:
         p.draw(screen)   
      pygame.display.flip()

      for a in asteroids:
         if a.check_collision(player):
            print(f"Game Over!")
            sys.exit()


      dt = fpsClock.tick(60) / 1000
      

if __name__ == "__main__":
  main()
