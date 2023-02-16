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

#Load font
font = pygame.font.Font("trebuc.ttf", 36)

#Define text
text = "It's been 5 years since the incident."
text_image = font.render(text, True, (255, 255, 255))
text_position = (0, 450)

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
    screen.blit(text_image, text_position)
    pygame.display.update()

#Quit pygame
pygame.quit()
