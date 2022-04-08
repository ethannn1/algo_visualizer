import pygame

pygame.init()

SCREEN = pygame.display.set_mode((600, 600))

class Menu:
    def __init__(self, text, x, y,width, height, color, font_size):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text_col = (0,0,0)
        self.font = pygame.font.SysFont(None, font_size)
        self.reverse = False
        
    def display(self):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, False, self.text_col)
        SCREEN.blit(text, (self.x+self.width//2, self.y+self.height//2))
        
    
    def run(self):
        if self.x<=pygame.mouse.get_pos()[0] and pygame.mouse.get_pos()[0]<=self.x+self.width\
        and self.y<=pygame.mouse.get_pos()[1] and pygame.mouse.get_pos()[1]<=self.y+self.height:
            print(1)
            self.reverse = True
        else:
            print(2)
            self.reverse = False
            
        if self.reverse:
            #self.color = (255-self.color[0], 255-self.color[1], 255-self.color[2])
            self.color = (0,0,0)
            self.text_col = (255,255,255)
        else:    
            #self.color = (255-self.color[0], 255-self.color[1], 255-self.color[2])
            self.color = (255,255,255 )
            self.text_col = (0,0,0)
        
        self.display()

test = Menu("test", 100,100,200,200,(255,0,0), 20)

while 1:
    test.run()
    pygame.display.flip()	