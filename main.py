import pygame
from constants import *

def main():
   print(f"Starting asteroids!")

   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")
   
   pygame.init()
   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   fpsClock = pygame.time.Clock()
   dt = 0

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            print(f"Closing game!")
            return

      pygame.Surface.fill(screen, (0,0,0))
      pygame.display.flip()

      dt = fpsClock.tick(60) / 1000
      

if __name__ == "__main__":
  main()
