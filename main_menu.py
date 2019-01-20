import pygame
import time

def menu(screen):
    mainmenu = True
    playing = True
    while (mainmenu):
        dis_width = 800
        dis_height = 600
        # load and display the background image on the start screen
        background = pygame.transform.scale( \
            pygame.image.load("mb.jpg"),(dis_width,dis_height))
        rect = background.get_rect(center=(dis_width/2,dis_height/2))
        screen.blit(background,rect)  
        
        tweet_button = pygame.Rect(475,373,525-475,412-370)
        nuke_button = pygame.Rect(655,374,710-655,427-374)
        
        pygame.display.update()
        
        time = 0
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tweet_button.collidepoint(event.pos):
                        mainmenu = False;
                    elif nuke_button.collidepoint(event.pos):
                        while(time < 50):
                            time += 1
                            background = pygame.transform.scale( \
                                        pygame.image.load("nuke_trump.jpg"),(dis_width,dis_height))
                            rect1 = background.get_rect(center=(dis_width/2,dis_height/2)) 
                            screen.blit(background,rect)
                            pygame.display.update()
                        mainmenu = False
                        playing = False
                        
            if event.type == pygame.QUIT:
                mainmenu = False
                playing = False
                
    return(playing)