import pygame
import math

# CONSTANTES E VARIÁVEIS GLOBAIS
DARK_BLUE = (0, 0, 139)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 75, 10)
BLACK = (0, 0, 0)
GAME_WIDTH, GAME_HEIGHT = 256, 192
SCALE_FACTOR = 4
WINDOW_WIDTH = GAME_WIDTH * SCALE_FACTOR
WINDOW_HEIGHT = GAME_HEIGHT * SCALE_FACTOR

# CLASSE DO PLAYER
class player:
    def __init__(self, x, y, key_left, key_right, image_path, ):
        self.x = x
        self.y = y
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale_by(self.original_image, 5)

# MUDANDO COR DO PLAYER 1
        if key_left == pygame.K_LEFT:  # serve pra identificar o player 1
            green_image = self.original_image.copy()  # cria uma copia indepen
            arr = pygame.surfarray.pixels3d(green_image)  # acess all pixels
            arr[:, :, 0] = 0  # R
            arr[:, :, 1] = 255  # G
            arr[:, :, 2] = 0  # B
            del arr
            self.original_image = green_image


# MUDANDO COR DO PLAYER 2
        if key_left == pygame.K_a:  # serve pra identificar o player 2
            orange_image = self.original_image.copy()  # cria copia independent
            arr = pygame.surfarray.pixels3d(orange_image)  # acess all pixels
            arr[:, :, 0] = 255  # R
            arr[:, :, 1] = 75  # G
            arr[:, :, 2] = 10  # B
            del arr
            self.original_image = orange_image

        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

        self.angle = 0  # 0° pointing upward
        self.rotation_speed = 3  # rotation speed
        self.moving = False

        self.key_left = key_left
        self.key_right = key_right

    def toggle_movement(self):
        self.moving = not self.moving  # altern on and off

    def update(self):
        keys = pygame.key.get_pressed()

        # Ship rotation
        if keys[self.key_left]:
            self.angle += self.rotation_speed
        if keys[self.key_right]:
            self.angle -= self.rotation_speed

        # Update rotated image without distortion
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Move forward; image "top" is considered the front
        if self.moving:
            rad = math.radians(self.angle - 270)  # subtract oto align
            self.rect.x += math.cos(rad) * 6
            self.rect.y -= math.sin(rad) * 6  # inverted for pygame coordinates

        if self.rect.centerx < 0:
            self.rect.centerx = WINDOW_WIDTH
        elif self.rect.centerx > WINDOW_WIDTH:
            self.rect.centerx = 0

        if self.rect.centery < 0:
            self.rect.centery = WINDOW_HEIGHT
        elif self.rect.centery > WINDOW_HEIGHT:
            self.rect.centery = 0


# MOVIMENTO DO TIRO
def move_shot(shot):
    global shot_move
    movement = shot_move
    shot.x += movement[0]
    shot.y += movement[1]


# CRIANDO OS JOGADORES
# jogador 1
player1 = player(
    x=WINDOW_WIDTH // 5,
    y=WINDOW_HEIGHT // 5,
    key_left=pygame.K_LEFT,
    key_right=pygame.K_RIGHT,
    image_path=("atividade007\\warplane\\aviao.png"))

# jogador 2
player2 = player(
    x=WINDOW_WIDTH * 4 // 5,
    y=WINDOW_HEIGHT * 4 // 5,
    key_left=pygame.K_a,
    key_right=pygame.K_d,
    image_path=("atividade007\\warplane\\aviao.png"))
