import pygame
from pygame import *
pygame.init()

window = pygame.display.set_mode((500, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_model, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_model), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keypr = key.get_pressed()
        if keypr[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keypr[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
        if keypr[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keypr[K_RIGHT] and self.rect.x < 500:
            self.rect.x += self.speed
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    def perehod(self, x, y):
        self.rect.x = x
        self.rect.y = y   
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wight, hight, x, y):
        super().__init__()
        self.image = Surface((wight, hight))
        self.image.fill(( color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def update_wall(self, x, y):
        self.rect.x = x
        self.rect.y = y
        window.blit(self.image, (self.rect.x, self.rect.y))
        


game = True
level = 2
keyy = 0
podnato1 = 0
podnato2 = 0
key_shkaf = 0
win = 0
musorka = 0
taimer = 0
taimer2 = 0
player = Player('player.png', 250, 250, 1)
wall1 = Wall(0, 0, 0, 215, 10, 0, 0)
wall2 = Wall(0, 0, 0, 215, 10, 285, 0)
wall3 = Wall(0, 0, 0, 10, 215, 0, 0)
wall4 = Wall(0, 0, 0, 10, 215, 490, 0)
wall5 = Wall(0, 0, 0, 10, 215, 0, 285)
wall6 = Wall(0, 0, 0, 10, 215, 490, 285)
wall7 = Wall(0, 0, 0, 480, 10, 10, 490)
wall8 = Wall(0, 0, 0, 10, 70, 600, 600)
wall9 = Wall(0, 0, 0, 70, 10, 600, 600)
wall10 = Wall(0, 0, 0, 70, 10, 215, -10)
wall11 = Wall(0, 0, 0, 10, 70, -10, 215)
wall12 = Wall(0, 0, 0, 10, 70, 510, 215)
shkaf = Wall(116,109,99, 50, 50, 600, 600)
locked_shkaf = Wall(116,109,99, 50, 50, 600, 600)
door1 = Wall(255, 255, 255, 10, 70, 0, 215)
door2 = Wall(255, 255, 255, 10, 70, 490, 215)
door3 = Wall(255, 255, 255, 70, 10, 215, 0)
wallsup =[wall1, wall2, wall9, wall10]
wallsleft = [wall3, wall5, wall11]
wallsright = [wall4, wall6, wall8, wall12]
wallsdown = [wall7]
doors = [door1, door2]
font1 = font.SysFont('Arial', 35)
font2 = font.SysFont('Arial', 30)
font3 = font.SysFont('Arial', 22)
question = font1.render('Дверь открыта. Зайти?', True, (255, 255, 255))
question2 = font1.render('Дверь закрыта. Нужен ключ.', True, (255, 255, 255))
question3 = font3.render('Дверь закрыта. У вас есть ключ. Зайти?', True, (255, 255, 255))
question4 = font3.render('Поздравляю вы выйграли. Спасибо за игру!', True, (255, 255, 255))
question5 = font1.render('Шкаф. Обыскать?', True, (255, 255, 255))
question6 = font1.render('Шкаф закрыт. Нужен ключ.', True, (255, 255, 255))
question7 = font3.render('Шкаф закрыт. У вас есть ключ. Обыскать?', True, (255, 255, 255))
question8 = font1.render('Вы нашли ключ от двери.', True, (255, 255, 255))
question9 = font1.render('Вы нашли ключ от шкафа.', True, (255, 255, 255))
question10 = font1.render('Шкаф пуст.', True, (255, 255, 255))
clock = pygame.time.Clock()
clock.tick(60)
background = transform.scale(image.load('fgf.png'), (500, 500))
while game:
    window.blit(background, (0, 0))
    wall1.draw_wall()
    wall2.draw_wall()
    wall3.draw_wall()
    wall4.draw_wall()
    wall5.draw_wall()
    wall6.draw_wall()
    wall7.draw_wall()
    wall8.draw_wall()
    wall9.draw_wall()
    wall10.draw_wall()
    wall11.draw_wall()
    wall12.draw_wall()
    shkaf.draw_wall()
    locked_shkaf.draw_wall()
    door1.draw_wall()
    door2.draw_wall()
    door3.draw_wall()
    player.reset()
    player.update()         
    for door in doors:
        if player.colliderect(door):
            window.blit(question, (50, 400))
    if player.colliderect(door3) and keyy == 0 and win == 0:
        window.blit(question2, (50, 400))
    if player.colliderect(door3) and keyy == 1 and win == 0:
        window.blit(question3, (10, 400))
    if player.colliderect(shkaf) and key_shkaf == 0 and podnato1 == 0:
        window.blit(question5, (10, 400))
    if player.colliderect(locked_shkaf) and key_shkaf == 0 and podnato2 == 0:
        window.blit(question6, (10, 400))
    if player.colliderect(locked_shkaf) and key_shkaf == 1 and keyy == 0:
        window.blit(question7, (10, 400))
    if player.colliderect(shkaf) and key_shkaf == 1 and podnato1 == 0:
        window.blit(question10, (10, 400))
    if player.colliderect(locked_shkaf) and keyy == 1 and podnato2 == 0:
        window.blit(question10, (10, 400))
    for wall in wallsup:
        if player.colliderect(wall):
            player.rect.y += 1
    for wall in wallsdown:
        if player.colliderect(wall):
            player.rect.y -= 1
    for wall in wallsleft:
        if player.colliderect(wall):
            player.rect.x += 1
    for wall in wallsright:
        if player.colliderect(wall):
            player.rect.x -= 1
    for i in pygame.event.get():
        if i.type == QUIT:
            game = False  
        if i.type == pygame.KEYDOWN:
                if i.key == K_e and player.colliderect(door2) and level == 2:
                    door2.update_wall(600, 600)
                    door3.update_wall(600, 600)
                    wall8.update_wall(490, 215)
                    wall9.update_wall(215, 0)
                    player.perehod(15, 235)
                    shkaf.update_wall(250, 30)
                    level = 3
                elif i.key == K_e and player.colliderect(door1) and level == 2:
                    door1.update_wall(600, 600)
                    door3.update_wall(600, 600)
                    wall8.update_wall(0, 215)
                    wall9.update_wall(215, 0)
                    locked_shkaf.update_wall(250, 30)
                    player.perehod(425, 235)
                    level = 1
                elif i.key == K_e and player.colliderect(door3) and level == 2 and keyy == 1:
                    win = 1
                elif i.key == K_e and player.colliderect(door2) and level == 1:
                    door1.update_wall(0, 215)
                    door3.update_wall(215, 0)
                    player.perehod(15, 235)
                    wall8.update_wall(600, 600)
                    locked_shkaf.update_wall(600, 600)
                    wall9.update_wall(600, 600)
                    level = 2
                elif i.key == K_e and player.colliderect(door1) and level == 3:
                    door2.update_wall(490, 215)
                    door3.update_wall(215, 0)
                    player.perehod(425, 235)
                    wall8.update_wall(600, 600)
                    shkaf.update_wall(600, 600)
                    wall9.update_wall(600, 600)
                    level = 2
                elif i.key == K_e and player.colliderect(shkaf) and key_shkaf == 0:
                    key_shkaf = 1
                    podnato1 = 1

                elif i.key == K_e and player.colliderect(locked_shkaf) and key_shkaf == 1:
                    keyy = 1
                    podnato2 = 1
    if podnato1 == 1:
        taimer += 1
        if taimer < 179:
            window.blit(question9, (10, 400))
            if taimer == 180:
                podnato1 = 0
    if podnato2 == 1:
        taimer2 += 1
        if taimer2 < 179:
            window.blit(question8, (10, 400))
            if taimer2 == 180:
                podnato2 = 0
    if win == 1:
        if musorka == 0:
            player.perehod(500, 500)
            for h in wallsup:
                h.update_wall(600, 600)
            for h in wallsdown:
                h.update_wall(600, 600)
            for h in wallsright:
                h.update_wall(600, 600)
            for h in wallsleft:
                h.update_wall(600, 600)
            for h in doors:
                h.update_wall(600, 600)
            door3.update_wall(600, 600)
            player.speed = 0
            musorka = 1
        window.blit(question4, (10, 250))
    display.update()