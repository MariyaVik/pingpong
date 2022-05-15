from pygame import *

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



background_color = (150, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

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

        display.update()
        clock.tick(FPS)