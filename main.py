# CONTROLS: WASD, RSHIFT TO SWITCH VISION



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
playerWidth, playerHeight = 20, 20

WHITEPLAYERIMAGE = pygame.image.load(os.path.join('Assets', 'white.jpeg'))
WHITEPLAYER = pygame.transform.rotate(pygame.transform.scale(WHITEPLAYERIMAGE, (playerWidth, playerHeight)),0)
BLACKPLAYERIMAGE = pygame.image.load(os.path.join('Assets', 'black.jpeg'))
BLACKPLAYER = pygame.transform.rotate(pygame.transform.scale(BLACKPLAYERIMAGE, (playerWidth, playerHeight)),0)

def drawWindow(player, state): 
    window.fill(state) 
    if state == BLACK: 
        window.blit(WHITEPLAYER, (player.x, player.y))
    else: 
        window.blit(BLACKPLAYER, (player.x,player.y))

    pygame.display.update() 

def playerMovement (keys_pressed, player):
    if keys_pressed[pygame.K_a] and player.x - VEL > 0: # LEFT 
        player.x -= VEL 
    if keys_pressed[pygame.K_d] and player.x + VEL + player.width < WIDTH: #RIGHT 
        player.x += VEL 
    if keys_pressed[pygame.K_w] and player.y - VEL > 0: #UP 
        player.y -= VEL 
    if keys_pressed[pygame.K_s] and player.y + VEL + player.height < HEIGHT: #DOWN, checks if they are touching border 
        player.y += VEL 
    

def switchState(state): 
    if state == BLACK: 
        return WHITE 
    else: 
        return BLACK 



def main(): 
    whiteProjectiles = [] 
    blackProjectiles = []
    state = BLACK 

    playerRect = pygame.Rect(400, 400, playerWidth, playerHeight)
    clock = pygame.time.Clock() 
    run = True 
    while run: 
        clock.tick(FPS) 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False 
                pygame.quit() 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_RSHIFT: 
                    state = switchState(state)
                


        keys_pressed = pygame.key.get_pressed() 
        playerMovement (keys_pressed, playerRect)

        drawWindow(playerRect, state)
        pygame.display.update() 

if __name__ == "__main__": 
    main() 