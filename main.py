import pygame

pygame.init()

#create game window
SCREEN_WIDTH = 933
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("MFDoom")

#load background image
bg_image = pygame.image.load("background.jpg").convert_alpha()

#function for drawing background
def draw_bg():
  screen.blit(bg_image,(0,0))


#game loop
run = True
while run:

#draw background
      draw_bg()


      #event handler
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            run = False

      #update display
      pygame.display.update()

#exit pygame
pygame.quit()
