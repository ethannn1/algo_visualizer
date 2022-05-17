from consts import*


class Menu:
    def __init__(self, text, xy, dimensions, color, font_size, fonc):
        self.text = text
        self.x = xy[0]
        self.y = xy[1]
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.color = color
        self.text_col = (0, 0, 0)
        self.font = pygame.font.SysFont("arialblack", font_size)
        self.text_pos = (self.x + self.width//2 - font_size*2, self.y + self.height//2 - font_size)
        self.reverse = False
        self.clicked = False
        self.fonc = fonc

    def get_e(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicked = True
            else:
                self.clicked = False

    def display(self):
        pygame.draw.rect(SCREEN, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, False, self.text_col)
        SCREEN.blit(text, (self.text_pos[0], self.text_pos[1]))

    def run(self):
        if self.x <= pygame.mouse.get_pos()[0] <= self.x+self.width \
                and self.y <= pygame.mouse.get_pos()[1] <= self.y+self.height:
            self.reverse = True
            self.get_e()
            if self.clicked:
                self.clicked = False
                self.fonc()
        else:
            self.reverse = False
            
        if self.reverse:
            self.color = (0, 0, 0)
            self.text_col = (255, 255, 255)
        else:
            self.color = (255, 255, 255)
            self.text_col = (0, 0, 0)
        
        self.display()
