import pygame 
import os 
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800,800 
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BulletHell")

WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)
GREY = (128,128,128)

FPS = 60 
VEL = 5

def drawWindow(): 
    window.fill(GREY) 





def main(): 
    clock = pygame.time.Clock() 
    run = True 
    while run: 
        clock.tick(FPS) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
                pygame.quit() 

        drawWindow()
        pygame.display.update() 

if __name__ == "__main__": 
    main() 