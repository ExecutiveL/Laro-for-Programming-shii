import pygame
from Cards import Laro
from utilities import Button
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
def get_font(size):
    return pygame.font.Font("asset/Grand9KPixel.ttf", size)


def main():
    #screen
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Higher or Lower')
    
    game = Laro()
    game.start_game()
    
    #Music
    pygame.mixer.init()
    pygame.mixer.music.load("asset/Game_background.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)   
   
     
    while True:
         Background = pygame.image.load("asset/game_background.png")
         screen.blit(Background,(0,0))
         
         mouse_position = pygame.mouse.get_pos()
         higher = pygame.image.load("asset/Play.png")
         Higher_button = Button(higher,position=(600,500),text_input="Higher",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
         lower = pygame.image.load("asset/Play.png")
         lower_button = Button(lower,position=(200,500),text_input="Lower",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
         
         for button in [Higher_button,lower_button]:
            button.changeColor(mouse_position)
            button.update(screen)
            
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            #using the button to exit
            if event.type == pygame.MOUSEBUTTONDOWN:
             if Higher_button.checkForInput(mouse_position):
                 result = game.round_start("Higher")
                 if result:
                    print("tama")
                    
                 else:
                    print("mali")
             if lower_button.checkForInput(mouse_position):
                 result = game.round_start("Lower")
                 if result:
                    print("tama")
                    
                 else:
                    print("mali")
                    
        #card sa hand
         current_card = game.get_current_card()
         if current_card:
               card_image = game.load_card_image(current_card)
               if card_image:
                   card_image = pygame.transform.scale(card_image,(75,115))
               screen.blit(card_image,(297,210))
               
         back = pygame.image.load("asset/Back1.png")
         back = pygame.transform.scale(back,(75,115)) 
         screen.blit(back,(427,210))
                     
         score_font = get_font(36)
         score_text = score_font.render(f"Score: {game.get_score()}", True, BLACK)
         screen.blit(score_text, (10, 10))
                     
         clock.tick(60)
         pygame.display.flip()
