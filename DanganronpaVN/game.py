#Import the required libraries
import pygame

#Initialize pygame
pygame.init()

#Set screen size
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)

#Set title
pygame.display.set_caption("Danganronpa V4")

#Load background image
background_image = pygame.image.load("background.png")

#Load character images
kyoko_image = pygame.image.load("kyoko1.png")
byakuya_image = pygame.image.load("byakuya1.png")

#Define character positions
kyoko_position = (0, -500)
byakuya_position = (300, -250)

#Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Update screen
    screen.blit(background_image, (-75, 25))
    screen.blit(kyoko_image, kyoko_position)
    screen.blit(byakuya_image, byakuya_position)
    pygame.display.update()

#Quit pygame
pygame.quit()
