import pygame 
 
class Fighter(): 
     def __init__(self ,x, y): 
      self.rect = pygame.Rect((x, y, 80, 180)) 
      self.vel_y = 0 
      self.jump = False 
      self.attack_type = 0 
 
     def move(self, screen_width, screen_height): 
      SPEED = 10 
      GRAVITY = 2 
      dx = 0 
      dy = 0 
 
      #get keypresses 
      key = pygame.key.get_pressed() 
          
      #movement 
      if  key[pygame.K_a]: 
         dx = -SPEED 
      if  key[pygame.K_d]: 
         dx = SPEED 
 
      #jump 
      if  key[pygame.K_w] and self.jump == False: 
         self.vel_y = -30 
         self.jump = True 
      #attack 
      if key[pygame.K_r] or key[pygame.K_t]:

         #determine which attack type was used
         if key[pygame.K_r]:
            self.attack_type = 1
         if self.key[pygame.K_t]:
            self.attack_type = 2
         
         #determine which attack type was used  
         if key[pygame.K_r] : 
            self.attack_type = 1 
         if key[pygame.K_t] : 
            self.attack_type = 2 
 
      #apply gravity 
      self.vel_y += GRAVITY 
      dy += self.vel_y 
 
 
      #ensure players stays on screen 
      if self.rect.left + dx < 0: 
         dx = - self.rect.left 
      if self.rect.right + dx > screen_width: 
         dx = screen_width - self.rect.right 
      if self.rect.bottom + dy > screen_height - 50: 
        self.vel_y = 0 
        self.jump = False 
        dy = screen_height - 50 - self.rect.bottom 
 
      #update player position  
      self.rect.x += dx     
      self.rect.y += dy 
 
 
     def attack(self): 
        pass
      
 
     def draw(self, surface): 
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
