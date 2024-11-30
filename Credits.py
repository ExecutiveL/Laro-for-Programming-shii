import pygame
from utilities import Button


pygame.init()

title_icon = pygame.image.load("asset/icon.png")
pygame.display.set_icon(title_icon)
pygame.display.set_caption("Credits")

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

def get_font(size):
 return pygame.font.Font("asset/Grand9KPixel.ttf", size)

pygame.mixer.init()
pygame.mixer.music.load("asset/background.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

WHITE = (255,255,255)
BLACK = (0,0,0)




def Credit_screen():
    while True:
        
        mouse_position = pygame.mouse.get_pos()
        
        screen.fill((59,92,29))
        title_TEXT = get_font(40).render("This Game Is Made By:", True, "#b68f40")
        title_RECT = title_TEXT.get_rect(center=(380, 70))
        screen.blit(title_TEXT, title_RECT)
        name_1 = get_font(20).render("Arellano, Marochelle", True, "#b68f40")
        name_1_rect = name_1.get_rect(center=(380, 150))
        screen.blit(name_1, name_1_rect)
        name_2 = get_font(20).render("Irabon, Ralp Lawrence", True, "#b68f40")
        name_2_rect = name_2.get_rect(center=(380, 200))
        screen.blit(name_2, name_2_rect)
        name_3 = get_font(20).render("Javier, Marco Angelo", True, "#b68f40")
        name_3_rect = name_3.get_rect(center=(380, 250))
        screen.blit(name_3, name_3_rect)
        name_4 = get_font(20).render("Oliquiano, Prima Sophia", True, "#b68f40")
        name_4_rect = name_4.get_rect(center=(380,300))
        screen.blit(name_4, name_4_rect)
        
        return_menu = pygame.image.load("asset/Play.png")
        return_button = Button(return_menu,position=(380,500),text_input="Return to menu",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        for button in [return_button]:
            button.changeColor(mouse_position)
            button.update(screen)
         
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button.checkForInput(mouse_position):
                        pygame.mixer.music.stop()
                        from menu import title_screen
                        title_screen()
                        pygame.mixer.music.play(-1)
                    
        pygame.display.flip()
