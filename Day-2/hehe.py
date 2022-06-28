import pygame

pygame.init()

width = 900
height = 700

color = (0, 0, 0)

screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# IMAGE LOADING
hehe = pygame.image.load("Day-2/image/hehe.jpg")
nothehe = pygame.image.load("Day-2/image/nothehe.jpeg")


smallhehe = pygame.transform.scale(hehe, (500, 500))

font = pygame.font.SysFont('arial', 32)
text = font.render("HEHE CAT", True, (255, 255, 255))
textRect = text.get_rect(center=(width//2, height//2))
screen.blit(text, textRect)

pygame.display.update()

running = True


while running:
    events = pygame.event.get()

    for e in events:
        if e.type == pygame.QUIT:
            print("exit")
            running = False
        elif e.type == pygame.KEYDOWN:
            screen.fill(color)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1] or keys[pygame.K_2]:
                if keys[pygame.K_1]:
                    screen.blit(smallhehe, (0, 0))

                elif keys[pygame.K_2]:
                    screen.blit(nothehe, (0, 0))

                pygame.display.update()
