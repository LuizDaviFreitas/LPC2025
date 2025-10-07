import pygame

pygame.init()
pygame.mixer.init()

white = (255, 255, 255)
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

 # Classe Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("atividade006/nave.png").convert_alpha()  # carrega imagem
        self.image = pygame.transform.scale_by(self.image, 0.1)  # reduz pra 5% do tamanho original
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Criação do grupo de sprites
all_sprites = pygame.sprite.Group()
player = Player(400, 300)
all_sprites.add(player)

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    all_sprites.update()       # atualiza todos os sprites
    all_sprites.draw(screen)   # desenha todos os sprites
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

