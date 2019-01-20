import pygame, os, colors, char
import main_menu

def main():
    
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    player1 = char.Char(WIDTH, HEIGHT)
    all_players = pygame.sprite.Group()
    all_players.add(player1)


    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tweet Jump")
    background1 = background2 = pygame.image.load("full-background_scaled.png")
    clock = pygame.time.Clock()
    move1 = 0
    move2 = 1200
    running = True
    
    main_menu.menu(screen)
    
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        
        # Process exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()
        screen.fill(colors.black)
        move1 -= 1
        move2 -= 1
        screen.blit(background1, (move1,0))
        screen.blit(background2, (move2,0))
        all_players.update(WIDTH, HEIGHT)
        all_players.draw(screen)
        if move2 == -1200:
            move2 = 1200
        if move1 == -1200:
            move1 = 1200
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()