import pygame
import random
import math
import time

class Mang():
    def __init__(self):
        pygame.init()

        elud = 3
        skoor = 0
        minus_timer = 0
        minus_timer2 = 0

        ekraan = pygame.display.set_mode([1000, 750])
        heli_kolks = pygame.mixer.Sound("banger_music.mp3")
        heli_kolks.set_volume(1)
        heli_kolks.play()

        pygame.display.set_caption("Mäng")
        pilt = pygame.image.load("hunt.png")
        banger = pygame.image.load("banger.jpg")

        pilt = pygame.transform.scale(pilt, (100, 100))
        pilt_x = 30
        pilt_y = 530
        samm = 15
        dia_speed = samm / math.sqrt(2)

        background = pygame.transform.scale(banger, (1000, 750))

        pilt2 = pygame.image.load("muna.png")
        pilt2 = pygame.transform.scale(pilt2, (60, 100)) 
        pilt2_x = random.randint(1, 1000)
        pilt2_y = 130

        muna = pygame.image.load("muna2.png")
        muna = pygame.transform.scale(muna, (60, 100)) 

        pygame.key.set_repeat(1, 10)

        kukkuv = pilt2

        running = True
        while running:
            ekraan.blit(background, (0, 0))
            if elud <= 0:

                teksti_font = pygame.font.SysFont("Badeen Display", 100)
                tekst_pildina = teksti_font.render('GAME OVER', True, [255, 0, 0])

                text_rect = tekst_pildina.get_rect()
                text_rect.center = (400, 300)
                pygame.display.update()

                pygame.time.wait(3000)
                heli_kolks.stop()
                ekraan = pygame.display.set_mode([800, 600])

                running = False

                with open('scoreboard.txt', 'a') as f:
                    f.write(':' + str(skoor) + '\n')
                
                return
                    
            for i in range(1, elud + 1):
                elu = pygame.image.load("elud.png")
                elu = pygame.transform.scale(elu, (50, 50))
                ekraan.blit(elu, (10 + i * 70, 10))
            
            teksti_font = pygame.font.SysFont("Badeen Display", 50)
            tekst_pildina = teksti_font.render(str(skoor), 1, [0, 0, 0])
            ekraan.blit(tekst_pildina, [10, 10])
            
            ekraan.blit(pilt, (pilt_x, pilt_y))
            ekraan.blit(kukkuv, (pilt2_x, pilt2_y))
            
            pilt2_y += 10
            
            if minus_timer > 0:
                minus_font = pygame.font.SysFont("Badeen Display", 50)
                minus_pildina = minus_font.render('-15', 1, [247, 0, 25])
                ekraan.blit(minus_pildina, [10, 50])
                minus_timer -= 1
            
            if minus_timer2 > 0:
                minus_font = pygame.font.SysFont("Badeen Display", 50)
                minus_pildina = minus_font.render('-1', 1, [247, 0, 25])
                ekraan.blit(minus_pildina, [10, 50])
                minus_timer -= 1

            
            if pilt2_y > 800:
                if kukkuv == pilt2:
                    skoor -=1
                    minus_timer2 = 120
                
                kukkuv = muna if random.randint(1, 10) == 5 else pilt2
                pilt2_x = random.randint(1, 740)
                pilt2_y = 0
            

            if pilt_y > 800:
                pilt_y = 0
            
            if pilt_y < 0:
                pilt_y = 800
                
            if pilt_x < 000:
                pilt_x = 1000
            
            if pilt_x > 1000:
                pilt_x = 0

            rect = pilt.get_rect(topleft=(pilt_x, pilt_y))
            rect2 = kukkuv.get_rect(topleft=(pilt2_x, pilt2_y))
                
            if rect.colliderect(rect2):
                pauk = pygame.mixer.Sound("pauk.mp3")
                pauk.set_volume(0.2)
                pauk.play()

                if kukkuv == muna:
                    skoor -= 15
                    elud -= 1
                    minus_timer = 120
                else:
                    minus_timer2 = 0
                    skoor += 1

                kukkuv = muna if random.randint(1, 10) == 5 else pilt2
                pilt2_x = random.randint(1, 740)
                pilt2_y = 0
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                pilt_y -= dia_speed
                pilt_x -= dia_speed
            elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                pilt_y -= dia_speed
                pilt_x += dia_speed
            elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                pilt_y += dia_speed
                pilt_x -= dia_speed
            elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                pilt_y += dia_speed
                pilt_x += dia_speed
            else:
                if keys[pygame.K_UP]:
                    pilt_y -= samm
                if keys[pygame.K_DOWN]:
                    pilt_y += samm
                if keys[pygame.K_LEFT]:
                    pilt_x -= samm
                if keys[pygame.K_RIGHT]:
                    pilt_x += samm

        pygame.quit()
