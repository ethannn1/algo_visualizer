from menu import*
from algo_visu_v1 import*

Running = True


def get_e():
    global Running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            quit()


menu1 = Menu("selection", (0, 0), (300, 300), (255, 0, 0), 30, selection_sort)
menu2 = Menu("insertion", (300, 0), (300, 300), (255, 0, 0), 30, insertion_sort)
menu3 = Menu("  bulle", (0, 300), (300, 300), (255, 0, 0), 30, bubble_sort)
menu4 = Menu("cocktail", (300, 300), (300, 300), (255, 0, 0), 30, cocktail_sort)

menus = [menu1, menu2, menu3, menu4]

while Running:
    for m in menus:
        m.run()
    get_e()
    pygame.display.flip()
