import random
import pygame
import time

class Pylot:
    def __init__(self,screen,width,height,n,padx,pady) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.n = n
        self.padx = padx
        self.pady = pady

        self.arr = Pylot.randomizer(self.n, (self.height - (2 * self.pady)))

        self.seen = set()


    @staticmethod
    def randomizer(n,lim):
        return [random.randint(1,lim) for x in range(n)]


    
    def update(self,screen,arr):
        screen.fill((0,0,0))
        # self.width, self.height = pygame.display.get_surface().get_size()
        x = self.padx

        inc = (self.width - (2 * self.padx)) / self.n

        for i in range(len(arr)):
            if i in self.seen: pygame.draw.rect(screen,(93, 137, 186), (x,self.height - (2 * self.pady) - arr[i],inc,arr[i]))
            else: pygame.draw.rect(screen,(240, 224, 137),(x,self.height - (2 * self.pady) - arr[i],inc,arr[i]))

            x += inc

            pygame.display.update()

            time.sleep(0.05)
    
    
    def bubbleSort(self):

        self.update(self.screen,self.arr)
        arr = self.arr
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            self.seen.add(n - 1 - i)
            self.update(self.screen,self.arr)

    



n = 30


w,h = 600,400


padx = pady = 10




screen = pygame.display.set_mode((w, h))


obj = Pylot(screen,w,h,n,padx,pady)


# obj.bubbleSort()



run = True

while run:

    events  = pygame.event.get()

    for e in events:
      
        if e.type == pygame.QUIT:
          run = False
          break

        elif e.type == pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_1]:
                screen.fill((0,0,0))
                obj.bubbleSort()

pygame.quit()