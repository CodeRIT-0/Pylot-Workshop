import pygame
import random
import time

n = 100


w,h = 600,400


padx = pady = 10

inc = (w - (2 * padx)) / n

x = padx


arr = [random.randint(1,h - (2 * pady)) for x in range(n)]


screen = pygame.display.set_mode((w, h))

for i in range(n):
    pygame.draw.rect(screen,(93,137,186),(x, pady, inc, arr[i]))

    x += inc

    
    # pygame.draw.rect(screen,(93, 137, 186), (x,h - (2 * pady) - arr[i],inc,arr[i]))

pygame.display.update()


run = True

while run:

    events  = pygame.event.get()

    for e in events:
      
        if e.type == pygame.QUIT:
          run = False
          break

pygame.quit()