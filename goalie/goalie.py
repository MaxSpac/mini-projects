import pygame
import random
import sys

# Initialization
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Goalie-Game")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Styles
# Schriftarten
name_font = pygame.font.SysFont(None, 36)
button_font = pygame.font.SysFont(None, 48)

# Keeper-name selection
keeper_name = ""
input_active = False
input_text = "Write something"
selecting_name = True

# Goal settings
goal_height = 50
goal_y = 500

# Keeper settings
keeper_width = 120
keeper_height = 20
keeper_y = goal_y

# Ball settings
ball_radius = 15
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = 0
ball_speed = 5

# Game variables
score = 0
running = True
game_over = False
game_over_angle = 0 # Rotation angle
animation_step = 0 # Step counter
loser_text_visible = False # Controls "You Looser!" display 

# Selecting name
while selecting_name:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            # Button für Manuel Neuer
            if 200 < mouse_pos[0] < 600 and 200 < mouse_pos[1] < 250:
                keeper_name = "Manuel N."
                selecting_name = False
            # Button für Rainer Winkler
            elif 200 < mouse_pos[0] < 600 and 300 < mouse_pos[1] < 350:
                keeper_name = "Rainer W."
                selecting_name = False
            # Eingabefeld aktivieren
            elif 200 < mouse_pos[0] < 600 and 400 < mouse_pos[1] < 450:
                input_text = ""
                input_active = True
                
        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN and input_text:
                keeper_name = input_text[:8]  # Begrenze auf 9 Buchstaben
                selecting_name = False
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            elif len(input_text) < 8 and event.unicode.isprintable():
                input_text += event.unicode

    # Zeichne Auswahlbildschirm
    screen.fill(BLACK)
    title = name_font.render("Choose your keeper's name:", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

    # Button Manuel Neuer
    neuer_text = button_font.render("Manuel N.", True, WHITE)
    pygame.draw.rect(screen, GREEN, (200, 200, 400, 50))
    screen.blit(neuer_text, (400 - neuer_text.get_width() // 2, 210))

    # Button Rainer Winkler
    winkler_text = button_font.render("Rainer W.", True, WHITE)
    pygame.draw.rect(screen, GREEN, (200, 300, 400, 50))
    screen.blit(winkler_text, (400 - winkler_text.get_width() // 2, 310))

    # Eingabefeld
    input_box = pygame.Rect(200, 400, 400, 50)
    pygame.draw.rect(screen, WHITE if input_active else GREEN, input_box)
    input_surface = name_font.render(input_text, True, BLACK)
    screen.blit(input_surface, (input_box.x + 5, input_box.y + 10))

    pygame.display.flip()
    clock.tick(60)



# Actual Game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            game_over = False
            score = 0
            ball_y = 0
            ball_speed = 5
            animation_step = 0
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False  # Beendet das Spiel

    
    # Mouse position goalie
    keeper_x = pygame.mouse.get_pos()[0] - keeper_width // 2 # Center of keeper at mouse
    
    # Move ball
    if not game_over:
        ball_y += ball_speed

    # Check for collision (rectangular collision)
    collision_buffer = ball_speed // 5 # Buffer growths with ball speed
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    keeper_rect = pygame.Rect(keeper_x, keeper_y - collision_buffer, keeper_width, keeper_height)
    if ball_rect.colliderect(keeper_rect):
        score +=1
        ball_x = random.randint(ball_radius, WIDTH - ball_radius)
        ball_y = 0 # Set back
        ball_speed += 0.25

    # Ball in goal?
    elif ball_y + ball_radius > goal_y:
        game_over = True

    if game_over and ball_y + ball_radius < goal_y + goal_height:
        ball_y += ball_speed
        # Stops at lower barrier of goal
        if ball_y + ball_radius > goal_y + goal_height:
            ball_y = goal_y + goal_height - ball_radius  # Ball stays in the goal until new game is started

    # Draw screen
    screen.fill(BLACK)
    
    # Draw goal
    pygame.draw.rect(screen, WHITE, (0, goal_y, WIDTH, goal_height))
                                     
    # Draw ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw keeper
    pygame.draw.rect(screen, GREEN, (keeper_x, keeper_y, keeper_width, keeper_height))
    keeper_name_surface = name_font.render(keeper_name, True, BLACK)
    keeper_name_rect = keeper_name_surface.get_rect(center=(keeper_x + keeper_width // 2, keeper_y + keeper_height // 2))
    screen.blit(keeper_name_surface, keeper_name_rect)

    # Show score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over animation
    if game_over:
        # Step 1: Fast Rotation
        if animation_step < 60:  # 1 Sekunde bei 60 FPS
            game_over_angle += 15  # Schnelle Rotation (15 Grad pro Frame)
            font = pygame.font.SysFont(None, 55)
            game_over_text = font.render("Game Over!", True, RED)
            rotated_text = pygame.transform.rotate(game_over_text, game_over_angle)
            text_rect = rotated_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(rotated_text, text_rect)
            animation_step += 1

        # Step 2: Big Game Over
        elif animation_step < 180: 
            font = pygame.font.SysFont(None, 100)  
            game_over_text = font.render("Game Over!", True, RED)
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over_text, text_rect)
            animation_step += 1

         # Step 3: "You Loser!" 
        else:
        
            font = pygame.font.SysFont(None, 100)
            game_over_text = font.render("Game Over!", True, RED)
            text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(game_over_text, text_rect)
            animation_step += 1

            if not loser_text_visible:
                loser_text_visible = True
            loser_font = pygame.font.SysFont(None, 80)
            loser_text = loser_font.render("You Loser!", True, WHITE)
            loser_rect = loser_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            screen.blit(loser_text, loser_rect)
            
            # Restart-Text
            restart_font = pygame.font.SysFont(None, 40)
            restart_text = restart_font.render("Try again? Press R. Only real quitters quit now (Q)!", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT - 25))   
            screen.blit(restart_text, restart_rect)
        
    # Refresh page
    pygame.display.flip()
    clock.tick(60)

# Finish game
pygame.quit()