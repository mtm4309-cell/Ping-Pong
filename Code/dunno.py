import pygame, sys, random 
import button

pygame.mixer.init()

game_bg = "UI/pixbg.jpg"
pause_bg = "UI/bg3.jpg"

boop = pygame.mixer.Sound("UI/boop.wav")
punch = pygame.mixer.Sound("UI/punch.mp3")
victor = pygame.mixer.Sound("UI/Victory.wav")
lose = pygame.mixer.Sound("UI/Lose.mp3")


def ball_animation():
    global ball_speed_x, ball_speed_y, opp_score, player_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score +=1
        ball_start()
    if ball.right >= WIDTH:
        opp_score +=1
        ball_start()
    if ball.colliderect(player) or ball.colliderect(opponent):
        boop.play()
        ball_speed_x *= -1
        ball_speed_x + 4
        ball_speed_y + 4 
        (ball_speed_y) *= random.choice((1,-1)) 
def ball_start():
    global ball_speed_x, ball_speed_y 
    punch.play()
    pygame.time.delay(500)
    ball.center = (WIDTH/2, HEIGHT/2)
    ball_speed_y *= random.choice((1,-1)) 
    ball_speed_x *= random.choice((1,-1)) 


def player_animation():
    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT


def opponent_animation():
    if opponent.top < ball.y:
        opponent.y += opponent_speed + 15
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed + 15
    
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT

pygame.init()
clock = pygame.time.Clock()

HEIGHT = 600
WIDTH = 1200

fonti = pygame.font.Font("UI/PokemonGB.ttf", 40)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING-PONG")

ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30,30)
opponent= pygame.Rect(10, HEIGHT/2 - 70 ,10,140)
player = pygame.Rect(WIDTH-20, HEIGHT/2 -70,10,140)

bg_color = pygame.Color("black")
light_grey = (200, 200, 200)

player_score = 0
opp_score = 0

ball_multiplier = random.randint(15,20)

ball_speed_x = ball_multiplier * random.choice((1,-1)) 
ball_speed_y = ball_multiplier * random.choice((1,-1)) 

if opp_score + 1 or player_score + 1:
    ball_speed_x + random.randint(6,10)
    ball_speed_y + random.randint(6,10)


player_speed = 0
opponent_speed = random.randint(15,18)

font = pygame.font.Font("UI/PokemonGB.ttf", 21)
draws = True
game_pause = False
gstart = True
while True:
    
    if gstart== True:
        pygame.display.set_caption("MAIN MENU")
        WIN.fill("antiquewhite4")
        text = fonti.render("PING PONG", False, ("white"))
        WIN.blit(text, (450, 50))
        draws = False
        
        start_img = pygame.image.load("UI/start_btn.png").convert_alpha()
        start_button = button.Button(480,200, start_img, 1)

        quit_img = pygame.image.load("UI/exit_btn.png").convert_alpha()
        quit_button = button.Button(500,400, quit_img, 1)    

        if start_button.draw(WIN):
            pygame.mixer.music.pause()
            draws = True
            gstart = False

        elif quit_button.draw(WIN):
            break
   
        pygame.display.flip()



    if game_pause == True:
        draws = False
        gstart = False
        pygame.display.set_caption("PAUSE")

        pause_BG = pygame.transform.scale(pygame.image.load(pause_bg), (WIDTH,HEIGHT))
        WIN.blit(pause_BG, (0,0))

        resume_img = pygame.image.load("UI/resume.png").convert_alpha()
        resume_button = button.Button(500,200, resume_img, 1)
        quit_img = pygame.image.load("UI/button_quit.png").convert_alpha()
        back_btn = button.Button(530,400, quit_img, 1)
        pygame.mixer.music.pause()

        if resume_button.draw(WIN):
            draws = True
            game_pause = False
            
        elif back_btn.draw(WIN):
            draws = False
            game_pause = False
            gstart = True
        pygame.display.flip() 



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_pause = True

            if event.key == pygame.K_DOWN:
                player_speed +=13
            if event.key == pygame.K_UP:
                player_speed -=13
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -=13
            if event.key == pygame.K_UP:
                player_speed +=13
        
    if draws:
        pygame.display.set_caption("PING-PONG")

        if opp_score == 5:
            lose.play()
            pygame.mixer.music.pause()
            WIN.fill("black")
            win_text= font.render("YOU LOSE!", False,(0,0,255)) 
            WIN.blit(win_text,(480,300))
            pygame.display.flip()
            pygame.time.delay(4000)
            gstart = True
            opp_score = 0 
            player_score = 0
            pygame.display.flip()
        
        if player_score == 5:
            victor.play()
            pygame.mixer.music.pause()
            WIN.fill("black")
            win_text = font.render("YOU WIN!", False,( 0, 255,0))
            WIN.blit(win_text,(480, 300))
            pygame.display.flip()
            pygame.time.delay(4500)
            gstart = True
            player_score = 0
            opp_score = 0
            pygame.display.flip()
       
        ball_animation()
        player_animation()
        opponent_animation()
            

        BG = pygame.transform.scale(pygame.image.load(game_bg), (WIDTH,HEIGHT))
        WIN.blit(BG, (0,0))


        pygame.draw.rect(WIN,light_grey,player)
        pygame.draw.rect(WIN, light_grey, opponent)
        pygame.draw.ellipse(WIN, light_grey, ball)
        pygame.draw.aaline(WIN, light_grey, (WIDTH/2,0), (WIDTH/2,HEIGHT))
        
        player_text = font.render(f" Player : {player_score}", True, light_grey)
        WIN.blit(player_text,(950,10))

        opp_text = font.render(f"Opponent : {opp_score}", False, light_grey)
        WIN.blit(opp_text,(10,10))
        pygame.display.flip()
        clock.tick(60)


