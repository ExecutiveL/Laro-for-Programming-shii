import pygame
from Cards import Laro
from utilities import Button
from utilities import ImageButton
from pygame import mixer


pygame.init()
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)

title_icon = pygame.image.load("asset/icon.png")
pygame.display.set_icon(title_icon)
pygame.display.set_caption("Cards game")
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    
def get_font(size):
    return pygame.font.Font("asset/Grand9KPixel.ttf", size)
def win():
    a = True
    while a:
     win = get_font(40)
     win_text = win.render("Your Guess is Correct", True, BLACK)
     screen.blit(win_text, (200,200))
     pygame.display.flip()

     for event in pygame.event.get():
         if event.type == pygame.QUIT:
                pygame.quit()
                quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
             a = False
def lose():
    a = True
    while a:
        lose = get_font(40)
        lose_text = lose.render("Your Guess is Wrong", True, BLACK)
        screen.blit(lose_text, (200,200))
        pygame.display.flip()
        
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
         if event.type == pygame.MOUSEBUTTONDOWN:
             a = False
    
def get_bet_amount(screen, current_money):
    
    font = get_font(32)
    input_rect = pygame.Rect(250,200,300,50)
    color= BLACK
    text = ""
    bet = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        try:
                            bet = int(text)
                            if 0 < bet <= current_money:
                             return bet
                            else:
                                text = ""
                        except ValueError:
                            text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        screen.fill((59,92,29))
        txt_surface = font.render(text, True,color)
        width = max(270, txt_surface.get_width())
        input_rect.w = width
        screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
        pygame.draw.rect(screen, color, input_rect, 2)
        
        if current_money > 0:
            prompt_text = font.render(f"Enter your bet (1-{current_money}):", True, WHITE)
        else:
            prompt_text = font.render("You have no money to bet!", True, WHITE)
        screen.blit(prompt_text, (250, 150))
        
        pygame.display.flip()
        clock.tick(60)

def restart_or_exit():
    while True:
        mouse_position = pygame.mouse.get_pos()
        screen.fill(BLACK)
        
        you_lose_text = get_font(80).render("You Lose",True, WHITE)
        you_lose_text_rect = you_lose_text.get_rect(center=(380, 100))
        screen.blit(you_lose_text,you_lose_text_rect)
        
        restart = pygame.image.load("asset/Play.png")
        restart_button = Button(restart,position=(380,300),text_input="Play Again",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        menus = pygame.image.load("asset/Play.png")
        menu_button = Button(menus,position=(380,500),text_input="Main Menu",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        for button in [restart_button,menu_button]:
                button.changeColor(mouse_position)
                button.update(screen)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.checkForInput(mouse_position):
                        main()
                if menu_button.checkForInput(mouse_position):
                    import menu
                    menu.title_screen()
                    
            pygame.display.flip()
            clock.tick(60)

def restart_or_exit_1():
    while True:
        mouse_position = pygame.mouse.get_pos()
        screen.fill(WHITE)
        
        you_lose_text = get_font(80).render("You Win",True, BLACK)
        you_lose_text_rect = you_lose_text.get_rect(center=(380, 100))
        screen.blit(you_lose_text,you_lose_text_rect)
        
        restart = pygame.image.load("asset/Play.png")
        restart_button = Button(restart,position=(380,300),text_input="Play Again",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        menus = pygame.image.load("asset/Play.png")
        menu_button = Button(menus,position=(380,500),text_input="Main Menu",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        for button in [restart_button,menu_button]:
                button.changeColor(mouse_position)
                button.update(screen)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.checkForInput(mouse_position):
                        main()
                if menu_button.checkForInput(mouse_position):
                    import menu
                    menu.title_screen()
                    
            pygame.display.flip()
            clock.tick(60)
def main():
    
    pygame.display.set_caption('Higher or Lower')

    game = Laro()
    game.start_game()

    #Music
    pygame.mixer.init()
    pygame.mixer.music.load("asset/Game_background.mp3")
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(-1)   

    bet_amount = 0
    while True:
        
        # background image
        Background = pygame.image.load("asset/game_background.png")
        screen.blit(Background,(0,0))

        #mouse position
        mouse_position = pygame.mouse.get_pos()

        higher = pygame.image.load("asset/Play.png")
        Higher_button = Button(higher,position=(600,500),text_input="Higher",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        lower = pygame.image.load("asset/Play.png")
        lower_button = Button(lower,position=(200,500),text_input="Lower",font=get_font(30),base_color=BLACK,hovering_color=WHITE)
        
        chips = pygame.image.load("asset/chips.png").convert_alpha()
        chips_button = ImageButton(30,250,chips,1)
        chips_button.draw(screen)

        for button in [Higher_button,lower_button]:
            button.changeColor(mouse_position)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Higher_button.checkForInput(mouse_position):
                    if bet_amount > 0:
                        result = game.round_start("Higher")
                        if result:
                            win()
                            game.money += bet_amount
                        else:
                            lose()
                            game.money -= bet_amount
                        bet_amount = 0
                elif lower_button.checkForInput(mouse_position):
                    if bet_amount > 0:
                        result = game.round_start("Lower")
                        if result:
                            win()
                            game.money += bet_amount
                        else:
                            lose()
                            game.money -= bet_amount
                        bet_amount = 0
                elif chips_button.checkForInput(mouse_position):
                    if game.money > 0:
                        new_bet = get_bet_amount(screen,game.money)
                        if 0 < new_bet <= game.money:
                            bet_amount = new_bet
                if game.money == 0:
                    restart_or_exit()
                if game.money == 1000000:
                    restart_or_exit_1()
                
                    
                    
        #current card
        current_card = game.get_current_card()
        if current_card:
            card_image = game.load_card_image(current_card)
            if card_image:
                card_image = pygame.transform.scale(card_image,(75,115))
            screen.blit(card_image,(297,210))

        back = pygame.image.load("asset/Back1.png")
        back = pygame.transform.scale(back,(75,115)) 
        screen.blit(back,(427,210))

        bet_font = get_font(24)
        bet_text = bet_font.render(f"Current Bet: {bet_amount}", True, BLACK)
        screen.blit(bet_text, (10, 50))

        money_font = get_font(24)
        money_text = money_font.render(f"Money: {game.get_money()}", True, BLACK)
        screen.blit(money_text, (10, 10))
        
        clock.tick(60)
        pygame.display.flip()

