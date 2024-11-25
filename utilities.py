#create a class buttons

import pygame



class Button():
    pygame.init()
    def __init__(self, image, position, text_input, font, base_color, hovering_color,size=None,bg_color=None):
        self.image = image
        self.x_position = position[0]
        self.y_position = position[1]
        self.text_input = text_input
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.bg_color = bg_color
        
        self.text = self.font.render(self.text_input, True, self.base_color)
        
        if self.image is None:
            self.image = self.text
        
        self.rect = self.image.get_rect(center=(self.x_position, self.y_position))
        self.text_rect = self.text.get_rect(center=(self.x_position, self.y_position))
        
    #ginagawa ang button and text at dinidisplay sa surface
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        
    #hinahanap kung saan nakalagay yung mouse
    def checkForInput(self, position):
        
         if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
         return False
    
    #palitan ng color sa button and text
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            

