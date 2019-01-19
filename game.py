import pygame, os, colors

def main():
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    pygame.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # background = pygame.image.load("Background.png")
    clock = pygame.time.Clock()

    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)
        
        # Process exit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    main()
        screen.fill(colors.black)

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()