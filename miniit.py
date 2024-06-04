#attack
if key[pygame.K_r] or key[pygame.K_t]:
    self.attack(surface, target)
    #determine which attack type was used
    if key[pygame.K_r]:
        self.attack_type = 1
    if key [pygame.K_r]:
        self.attack_type = 2



def attack(self, surface, target):
    self.attacking = True
    attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
    if attacking_rect.colliderect(target.rect):
        target.health -=10

    pygame.draw.rect(surface, (0, 255, 0), attacking_rect)
    eufuenfe8

