import pygame
from pygame import mixer
from utilities import Button
from Game import main
from Tutorial import tutorial

# Initialize pygame
pygame.init()

#Title
title_icon = pygame.image.load("asset/icon.png")
pygame.display.set_icon(title_icon)
pygame.display.set_caption("Cards game")

#Screen

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#Font
def get_font(size):
 return pygame.font.Font("asset/Grand9KPixel.ttf", size)
#color
WHITE = (255,255,255)
BLACK = (0,0,0)

# Fps
clock = pygame.time.Clock()

#images
images = {
    "background" : "asset/background.png",
    "play_rectangle" : "asset/Play.png",
    "Quit rectangle" : "asset/Quit.png",
   
}
#sounds:
pygame.mixer.init()
pygame.mixer.music.load("asset/background.mp3")
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)


#Loop
def title_screen():
    
    while True:
        
        #Bg
        bg = pygame.image.load(images["background"])
        screen.blit(bg,(0,0))
        #mouse position
        mouse_position = pygame.mouse.get_pos()
        #Title size text isvisible
        title_TEXT = get_font(50).render("High and Low", True, "#b68f40")
        title_RECT = title_TEXT.get_rect(center=(170, 70))
        screen.blit(title_TEXT, title_RECT)
        #play image position text size  and colorr
        play = pygame.image.load(images["play_rectangle"])
        play_button = Button(play,position=(150,200),text_input="Play",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        #Exit image position text size and color
        Exit = pygame.image.load(images["Quit rectangle"])
        Exit_button = Button(Exit,position=(150,300),text_input="Exit",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        #Credit image position text size and color
        credits = pygame.image.load(images["play_rectangle"])
        credits_button = Button(credits,position=(150,400),text_input="Credits",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        #Event handling
        for button in [play_button,Exit_button,credits_button]:
            button.changeColor(mouse_position)
            button.update(screen)
        #Exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_position):
                    tutorial()
                    pygame.mixer.music.play(-1)
                    
                    
            #using the button to exit
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Exit_button.checkForInput(mouse_position):
                    pygame.quit()
                    quit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if credits_button.checkForInput(mouse_position):
                    pygame.mixer.music.stop()
                    from Credits import Credit_screen
                    Credit_screen()
                    pygame.mixer.music.play(-1)
                    
        clock.tick(60)
        pygame.display.flip()
title_screen()