import random
import time
from consts import*


def get_events():
    global SPEED
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                SPEED *= 1.1
            if event.key == pygame.K_RIGHT:
                SPEED /= 1.1
            if event.key == pygame.K_SPACE:
                stopped = True
                while stopped:
                    display_info(True)
                    for e in pygame.event.get():
                        if e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_SPACE:
                                stopped = False


def random_array():
    array = list(range(1, 51))
    random.shuffle(array)
    return array


def display_info(paused: bool):
    global SPEED, FONT
    pygame.draw.rect(SCREEN, (0, 0, 0), (0, 0, 600, 40))
    spd = round(1/SPEED)
    speed_render = FONT.render(str(spd)+"%", False, (255, 255, 255))
    SCREEN.blit(speed_render, (0, 0))
    if not paused:
        for i in range(2):
            pygame.draw.rect(SCREEN, (255, 255, 255), (567+i*20, 3, 10, 30))
    else:
        pygame.draw.polygon(SCREEN, (255, 255, 255), [(570, 3), (570, 33), (597, 18)])
    pygame.display.flip()


def display_list(array: list, mini: int, cursor: int, a_sorted: int, a_sorted_end: int, unsorted=None):
    global SPEED
    arr = array.copy()
    for i in range(len(arr)):
        if i == mini:
            pygame.draw.rect(SCREEN, (240, 10, 10), (i*12, 600-arr[i]*10, 10, arr[i]*10))
        elif i == cursor:
            pygame.draw.rect(SCREEN, (10, 240, 10), (i*12, 600-arr[i]*10, 10, arr[i]*10))
        elif i < a_sorted:
            pygame.draw.rect(SCREEN, (100, 10, 240), (i * 12, 600 - arr[i] * 10, 10, arr[i] * 10))
        elif i >= a_sorted_end:
            pygame.draw.rect(SCREEN, (100, 10, 240), (i * 12, 600 - arr[i] * 10, 10, arr[i] * 10))
        else:
            pygame.draw.rect(SCREEN, (255, 255, 255), (i*12, 600-arr[i]*10, 10, arr[i]*10))
        if unsorted is not None:
            if unsorted[0] < i < unsorted[1]:
                pygame.draw.rect(SCREEN, (255, 255, 255), (i * 12, 600 - arr[i] * 10, 10, arr[i] * 10))
    display_info(False)
    pygame.display.flip()
    get_events()
    SCREEN.fill((0, 0, 0))
    time.sleep(SPEED)


def selection_sort(array: list = random_array()):
    global SPEED
    arr = array.copy()
    for i in range(len(arr)-1):
        mini = arr[i]
        mini_i = i
        for j in range(i, len(arr)):
            if arr[j] < mini:
                mini = arr[j]
                mini_i = j
            display_list(arr, mini_i, j, i, len(arr))
        arr[i], arr[mini_i] = mini, arr[i]
    SPEED = 0.01
    display_list(arr, -1, -1, -1, 0)
    return arr


def insertion_sort(array: list = random_array()):
    global SPEED
    arr = array.copy()
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j > 0:
            display_list(arr, j-1, j, i, len(arr))
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        display_list(arr, j - 1, j, i, len(arr))
    SPEED = 0.01
    display_list(arr, -1, -1, -1, 0)
    return arr


def bubble_sort(array: list = random_array()):
    global SPEED
    arr = array.copy()
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            display_list(arr, j, j+1, -1, len(arr)-i)
    SPEED = 0.01
    display_list(arr, -1, -1, -1, 0)
    return arr


def cocktail_sort(array: list = random_array()):
    global SPEED
    SPEED = 0.1
    arr = array.copy()
    swapped = True
    start = 0
    end = len(arr) - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        display_list(arr, -1, -1, -1, 0, (start-1, end))
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start += 1
        display_list(arr, -1, -1, -1, 0, (start-1, end))
    display_list(arr, -1, -1, -1, 0)
    SPEED = 0.01
    return arr
