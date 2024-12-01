import pygame
from utilities import Button
from Game import main
pygame.init()

title_icon = pygame.image.load("asset/icon.png")
pygame.display.set_icon(title_icon)
pygame.display.set_caption("Cards game")

WHITE = (255,255,255)
BLACK = (0,0,0)
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

def get_font(size):
 return pygame.font.Font("asset/Grand9KPixel.ttf", size)
def tutorial():
    
    while True:
        mouse = pygame.mouse.get_pos()
        
        screen.fill((59,92,29))
        tutorial_text = get_font(24).render("Welcome to High and Low!", True, WHITE)
        screen.blit(tutorial_text, (250, 20))
        a_text = get_font(24).render("Earn money by guessing the value of the next card", True, WHITE)
        screen.blit(a_text, (80, 80))
        b_text = get_font(22).render("Press the Higher button if you think the next card is higher", True, WHITE)
        screen.blit(b_text, (50, 130))
        c_text = get_font(22).render("Otherwise press the lower button if you think the card is lower", True, WHITE)
        screen.blit(c_text, (30, 260))
        c_text = get_font(24).render("Win the Game by Earning 1 Million dollars", True, WHITE)
        screen.blit(c_text, (150, 400))
        higher = pygame.image.load("asset/test.png")
        Higher_button = Button(higher,position=(400,225),text_input="Higher",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        lower = pygame.image.load("asset/test.png")
        lower_button = Button(lower,position=(400,350),text_input="Lower",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        Play_text = pygame.image.load("asset/play.png")
        Play_button = Button(Play_text,position=(400,500),text_input="Play The Game",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        for button in [Higher_button,lower_button]:
            button.update(screen)
            
        for buttons in [Play_button]:
            buttons.changeColor(mouse)
            buttons.update(screen)
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Play_button.checkForInput(mouse):
                    pygame.mixer.music.stop()
                    main()
                    pygame.mixer.music.play(-1)
        pygame.display.flip()
        
