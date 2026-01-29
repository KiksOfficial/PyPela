import pygame
import sys
import random
import os
import math
from pelu import Mang

pygame.init()

ekraan = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Button Interaction Example")
font = pygame.font.SysFont("courier new", 24)


valge = [255, 255, 255]
must = [0, 0, 0]
punane = [226, 16, 16]
roheline = [16, 226, 86]
blue = [16, 191, 226]
kollane = [226, 226, 16]
orange = [255, 165, 0]

bg_color = valge

input_active = False
user_input = ""
leaderboard = False
new_window_open = False

def get_leaderboard():

    edetabel_ls = []
    
    with open('scoreboard.txt', 'r') as f:
        sisu = f.read()
        for line in sisu.splitlines():
            osad = line.strip().split(':')
            if len(osad) == 2 and osad[1] != '':
                try:
                    edetabel_ls.append([osad[0], int(osad[1])])
                except ValueError:
                    continue
    
    edetabel_ls.sort(key=lambda x: x[1], reverse=True)

    return edetabel_ls

            


def nupud():
    pygame.draw.rect(ekraan, roheline, [300, 50, 200, 80])
    pygame.draw.rect(ekraan, kollane, [300, 150, 200, 80])
    pygame.draw.rect(ekraan, blue, [300, 250, 200, 80])
    pygame.draw.rect(ekraan, orange, [300, 350, 200, 80])
    pygame.draw.rect(ekraan, punane, [300, 450, 200, 80])

    ekraan.blit(font.render("Mängi", True, must), (365, 80))
    ekraan.blit(font.render("Muuda värvi", True, must), (325, 180))
    ekraan.blit(font.render("Autorist", True, must), (345, 280))
    ekraan.blit(font.render("Edetabel", True, must), (345, 380))
    ekraan.blit(font.render("Lahku", True, must), (365, 480))

running_main = True
while running_main:
    ekraan.fill(bg_color)
    nupud()

    if input_active:
        pygame.draw.rect(ekraan, valge, [250, 500, 300, 50])
        pygame.draw.rect(ekraan, must, [250, 500, 300, 50], 2)
        ekraan.blit(font.render(user_input, True, must), (260, 515))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_main = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            
            if 300 <= x <= 500 and 50 <= y <= 130:
                input_active = True

            elif 300 <= x <= 500 and 150 <= y <= 230:
                bg_color = [random.randint(0, 255) for i in range(3)]

            elif 300 <= x <= 500 and 250 <= y <= 330:
                running_main = False
                new_window_open = True
                new_screen = pygame.display.set_mode([800, 600])
                new_screen.fill([0, 0, 0])
                pygame.display.set_caption("Autorist")

                teksti_font = pygame.font.SysFont("courier new", 36)
                pygame.draw.rect(new_screen, punane, [300, 350, 200, 80])
                tekst_pildina = teksti_font.render("Marcus Ariston Kikerpill 11. IT", True, [235, 152, 9])
                new_screen.blit(tekst_pildina, [50, 120])
                new_screen.blit(font.render("Tagasi", True, must), (365, 380))

                pygame.display.flip()

                while new_window_open:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            new_window_open = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            hiir_x,hiir_y = event.pos
                            if 300 <= hiir_x <= 500 and 350 <= hiir_y <= 430:
                                new_window_open = False
                                running_main = True

            
                ekraan = pygame.display.set_mode([800, 600])
                pygame.display.set_caption("Button Interaction Example")
            
            elif 300 <= x <= 500 and 350 <= y <= 430:
                running_main = False
                show_leaderboard = True
                leaderboard_screen = pygame.display.set_mode([800, 600])
                leaderboard_screen.fill([0, 0, 0])
                pygame.display.set_caption("Edetabel")
                leaderboard_screen.blit(font.render("Tagasi", True, valge), (365, 380))

                edetabel = get_leaderboard()
                y_offset = 120               

                for nimi, skoor in edetabel:
                    tekst_pildina = font.render(f"{nimi}: {skoor}", True, valge)
                    leaderboard_screen.blit(tekst_pildina, [50, y_offset])
                    y_offset += 30

                pygame.display.flip()

                while show_leaderboard:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            show_leaderboard = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            hiir_x, hiir_y = event.pos
                            if 300 <= hiir_x <= 500 and 350 <= hiir_y <= 430:
                                show_leaderboard = False
                                running_main = True


            elif 300 <= x <= 500 and 450 <= y <= 530:
                running_main = False

        elif event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                with open(os.path.join(os.getcwd(), 'scoreboard.txt'), 'a') as f:
                    f.write(user_input)
                Mang()

                if Mang() == None:
                    running_main= False
                    running_main = True

                user_input = ""
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode

pygame.quit()
sys.exit()