from pygame import *

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width :
            self.rect.y += self.speed

    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width :
            self.rect.y += self.speed

background_color = (150, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

img_rocket = 'images/racket.png'
img_ball = 'images/ball.png'

rocket1 = Player(img_rocket, 10, 200, 50, 200, 5)
rocket2 = Player(img_rocket, win_width - 60, 200, 50, 200, 5)
ball = GameSprite(img_ball, 200, 200, 50, 50, 2)

speed_ball_x = 3
speed_ball_y = 3

clock = time.Clock()
FPS = 60

#основной цикл
finish = False
run = True 

while run:
    for e in event.get():
        if e.type == QUIT:
           run = False
    
    if not finish:
        window.fill(background_color)

        rocket1.update1()
        rocket2.update2()
        ball.rect.x += speed_ball_x
        ball.rect.y += speed_ball_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
           speed_ball_y *= -1

        if sprite.collide_rect(ball, rocket1) or sprite.collide_rect(ball, rocket2):
            speed_ball_x *= -1

        rocket1.reset()
        rocket2.reset()
        ball.reset()

        display.update()
        clock.tick(FPS)