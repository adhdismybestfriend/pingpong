from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 15:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= height - 150:
            self.rect.y += self.speed


height = 500
width = 600
bgcolor = (200,255,255)
window = display.set_mode((width, height))
window.fill(bgcolor)
clock = time.Clock()

racket = Player('racket.png', 4, 30, 200, 50, 150)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill(bgcolor)
    racket.update()
    racket.reset()   
    display.update()
    clock.tick(60)

