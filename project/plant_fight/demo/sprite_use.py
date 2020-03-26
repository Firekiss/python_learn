import pygame, sys

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, topleft):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft


pygame.init()

SIZE = width, height = 480, 800
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)

sprite_1 = Block(RED, 100, 100, (50, 50))
sprite_2 = Block(GREEN, 100, 100, (100, 100))

screen = pygame.display.set_mode(SIZE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sprite_1.image, sprite_1.rect)
    screen.blit(sprite_2.image, sprite_2.rect)
    ret = pygame.sprite.collide_rect(sprite_1, sprite_2)
    print(ret)
    pygame.display.flip()


