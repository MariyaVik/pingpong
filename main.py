from pygame import *

# классы
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, width, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (width, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 0:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - rocket_height:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 0:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - rocket_height:
           self.rect.y += self.speed

# игровая сцена
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
# шрифты
font.init()
font = font.Font('fonts/wellwaitfree_regular.otf', 35)
text_lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
text_lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

# картинки
img_ball = 'images/tenis_ball.png'
img_rocket = 'images/racket.png'

# константы
rocket_width = 50
rocket_height = 150
ball_size = 50
ball_speed_x = 3
ball_speed_y = 3
 
# флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60
 
# создание мяча и ракеток  
racket1 = Player(img_rocket, 30, 200, 4, rocket_width, rocket_height) 
racket2 = Player(img_rocket, 520, 200, 4, rocket_width, rocket_height)
ball = GameSprite(img_ball, 200, 200, 4, ball_size, ball_size)

# игровой цикл
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
    
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            ball_speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            ball_speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(text_lose1, (200, 200))
            game_over = True
    
        if ball.rect.x > win_width - ball_size:
            finish = True
            window.blit(text_lose2, (200, 200))
            game_over = True
    
        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)
