
import tweepy
import threading
import time
import random
import main_menu
import pygame, os, colors, char, genText
import pygame.freetype


class TweetStream(threading.Thread):
    consumer_key = 'G3LVy1Ib9hiJiUULAOzS3rQou'
    consumer_secret = 'RQPvKxZcSmqLvizGIEJZWnDCWqZwfsfucvflNdRerJEkxQfWzw'
    access_token = '895545968027770880-RO1tkNqqdG0wibcPJOtKmAozKMdDvfa'
    access_token_secret = 'AkQRCqpobzYWeHys8YgPIcgfKfPYIjXjZryiYuRD6nDdI'

    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        self.api = tweepy.API(auth)
        self.current_tweets = []
        self.prev_tweets = []
        self.tags = []
        self.limit = 10
        self.cache_limit = 50

        self.cached_tweets = []
        self.cached_index = 0
    def run(self):
        while True:
            time.sleep(5)
            self.get_current_new_tweets(self.tags)

    def get_current_new_tweets(self, tags):
        # print("getting text")
        if self.cached_index >= 50 or len(self.cached_tweets) < 1:
            # print("new tweetsn\n\n")
            new_cached = []
            for tag in tags:
                search = tweepy.Cursor(self.api.search, q="what", result_type="mixed", lang="en", show_user=False).items(self.cache_limit)
                print("getting tweets")
                new_cached.extend([info.text for info in list(search)])

            self.cached_tweets = new_cached
            self.current_tweets = new_cached[:self.limit]
            self.cached_index = 10
        else:
            # print("old tweets\n\n\n")
            self.current_tweets = self.cached_tweets[self.cached_index: self.cached_index + 10]
            self.cached_index += 10
        random.shuffle(self.current_tweets)



def main():
    WIDTH = 800
    HEIGHT = 600
    FPS = 60

    player1 = char.Char(WIDTH, HEIGHT)
    all_players = pygame.sprite.Group()
    all_players.add(player1)


    pygame.init()
    pygame.freetype.init()
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tweet Jump")
    background1 = background2 = pygame.image.load("full-background_scaled.png")

    SCROLL_SPEED = 1
    player1 = char.Char(WIDTH, HEIGHT)
    all_players = pygame.sprite.Group()
    all_players.add(player1)
    text = genText.Text("Welcome to Tweet Jump. Jump on the tweets", 0, 250, colors.black, 40)
    all_text = pygame.sprite.Group()
    all_text.add(text)


    clock = pygame.time.Clock()
    move1 = 0
    move2 = 1200
    running = True

    # twitter fetching thread
    tweet_stream = TweetStream()
    tweet_stream.tags = ['trump', '@realDonaldTrump']
    tweet_stream.cache_limit = 20
    tweet_stream.start()

    
    main_menu.menu(screen)
    text_timer = time.time()
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
        
        tweets = tweet_stream.current_tweets
        if len(all_text) <= 3: #time.time() - text_timer > 5:
            for txt in tweets[:5]:
                rendered_text = genText.Text(txt, screen.get_width(), random.randint(0, screen.get_height() - 213), colors.black, 40)
                def add_text():
                    all_text.add(rendered_text)
                threading.Timer(random.randint(1,10), add_text).start()
            text_timer = time.time()
        
        #print(tweets)
        screen.fill(colors.black)
        move1 -= SCROLL_SPEED
        move2 -= SCROLL_SPEED
        screen.blit(background1, (move1,0))
        screen.blit(background2, (move2,0))
        all_players.update(WIDTH, HEIGHT, player1, all_text)
        all_text.update(SCROLL_SPEED, all_text)

        for i, text in enumerate(all_text):
            if text.rect.x  + text.rect.width < 0:
                all_text.remove(text)

        all_players.draw(screen)
        all_text.draw(screen)
        if player1.rect.bottom >= HEIGHT-211:
            main()
        if move2 == -1200:
            move2 = 1200
        if move1 == -1200:
            move1 = 1200
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
