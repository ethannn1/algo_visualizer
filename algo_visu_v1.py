import pygame
import random
import time

screen = pygame.display.set_mode((600, 600))


def display_list(array: list, mini: int, cursor: int, a_sorted: int):
    arr = array.copy()
    for i in range(len(liste)):
        if i == mini:
            pygame.draw.rect(screen, (240, 10, 10), (i*12, 600-arr[i]*10, 10, arr[i]*10))
        elif i == cursor:
            pygame.draw.rect(screen, (10, 240, 10), (i*12, 600-arr[i]*10, 10, arr[i]*10))
        elif i < a_sorted:
            pygame.draw.rect(screen, (100, 10, 240), (i * 12, 600 - arr[i] * 10, 10, arr[i] * 10))
        else:
            pygame.draw.rect(screen, (255, 255, 255), (i*12, 600-arr[i]*10, 10, arr[i]*10))
    pygame.display.flip()
    screen.fill((0, 0, 0))
    time.sleep(0.01)


def selection_sort(array: list):
    arr = array.copy()
    for i in range(len(arr)-1):
        mini = arr[i]
        mini_i = i
        for j in range(i, len(arr)):
            if arr[j] < mini:
                mini = arr[j]
                mini_i = j
            display_list(arr, mini_i, j, i)
        arr[i], arr[mini_i] = mini, arr[i]
    return arr


def insertion_sort(array: list):
    arr = array.copy()
    for i in range(1, len(arr)):
        j = i
        while arr[j-1] > arr[j] and j>0:
            display_list(arr, j-1, j, i)
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        display_list(arr, j - 1, j, i)
    return arr


if __name__ == "__main__":
    liste = list(range(1, 51))
    random.shuffle(liste)

    insertion_sort(liste)
    selection_sort(liste)
