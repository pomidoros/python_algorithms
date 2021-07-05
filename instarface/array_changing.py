import pygame


class FirstSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(COLORS['GREEN'])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5


WIDTH = 800
HEIGHT = 800
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

COLORS = {
    'BLACK': (0, 0, 0),
    'GREEN': (0, 255, 0)
}

all_sprites = pygame.sprite.Group()
spr = FirstSprite()
all_sprites.add(spr)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(COLORS['BLACK'])
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
