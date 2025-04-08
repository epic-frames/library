import pygame as pg
from random import randint
import sys
import hashlib


pg.init()

pg.mixer.init()

screen_x = 800
screen_y = 600
screen = pg.display.set_mode((screen_x, screen_y))
pg.display.set_caption("Asteroid Avoider 3000 v1.3")
clock = pg.time.Clock()

fps = 30

font = pg.font.Font(None, 36)
main_font = pg.font.Font("font.ttf", 30)
start_font = pg.font.Font("font.ttf", 20)
big_font = pg.font.Font(None, 50)

title, _ = pg.display.get_caption()

if title.endswith("- Beta version"):
    allow_debug = True
else:
    allow_debug = False

debug_mode = False

# Load assets
asteroid_size = randint(75, 200)

asteroid_img = pg.image.load('Assets/asteroid.png')
asteroid_img_new = pg.transform.scale(asteroid_img, (asteroid_size, asteroid_size))
asteroid_mask = pg.mask.from_surface(asteroid_img_new)
asteroid_x = 0
asteroid_y = 100

slider_x = 600
slider_y = 85
slider_radius = 11

sloweroid = pg.image.load('Assets/sloweroid.png')
fasteroid = pg.image.load('Assets/fasteroid.png')

speed = 10  # Asteroid falling speed
difficulty = 1

change_size = False
chance = None
save_speed = None
allow = True

asteroid_bg = pg.image.load("Assets/asteroid_background.png")
asteroid_bg_new = pg.transform.scale(asteroid_bg, (screen_x, screen_y))

points = 0

text_x = 10
text_y = 10

music_volume = 50

player_img = pg.image.load('Assets/player.png')
player_img_new = pg.transform.scale(player_img, (120, 120))
player_mask = pg.mask.from_surface(player_img_new)
player_x = 540
player_y = 470
player_x_change = 0

start_text_x = -800
start_text_y = 200

name_text_x = -2000
name_text_y = 300

current_page = "start_animation"

gray = (150, 150, 150)
reset_afterwards = False

class Button:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

button1 = Button(350, 500, 100, 50)
button2 = Button(350, 250, 100, 50)
button3 = Button(245, 400, 100, 50)
button4 = Button(350, 500, 100, 50)
button5 = Button(365, 400, 200, 50)
button6 = Button(325, 475, 150, 50)
button7 = Button(325, 160, 150, 50)
button8 = Button(350, 400, 100, 50)

def generate_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

def verify_hash(data, hash_to_verify):
    return generate_hash(data) == hash_to_verify


def save_score(score):
    score_str = str(round(score))
    score_hash = generate_hash(score_str)
    with open("score.txt", "w") as file:
        file.write(f"{score_str}\n{score_hash}")

def load_score():
    try:
        with open("score.txt", "r") as file:
            lines = file.readlines()
            score_str = lines[0].strip()
            saved_hash = lines[1].strip()
            
            if verify_hash(score_str, saved_hash):
                return int(score_str)
            else:
                save_score(0)
                return 0
    except FileNotFoundError:
        print("No saved score found.")
        return 0

def asteroid(x, y):
    global asteroid_img_new, asteroid_size, change_size, asteroid_mask
    if change_size:
        roll_dice()
        asteroid_size = randint(75, 200)
        if chance in sloweroid_difficulty:
            asteroid_img_new = pg.transform.scale(asteroid_img, (400, 400))
        else:
            asteroid_img_new = pg.transform.scale(asteroid_img, (asteroid_size, asteroid_size))
        change_size = False
        asteroid_mask = pg.mask.from_surface(asteroid_img_new)
    screen.blit(asteroid_img_new, (x, y))

def player(x, y):
    screen.blit(player_img_new, (x, y))

def roll_dice():
    global speed, save_speed, chance, allow, points, asteroid_img_new, asteroid_img, asteroid_mask, sloweroid_difficulty, fasteroid_difficulty, reset_afterwards
    points += 0.25 * speed
    if reset_afterwards:
        asteroid_img = pg.image.load('Assets/asteroid.png')
        asteroid_img_new = pg.transform.scale(asteroid_img, (400, 400))
        asteroid_mask = pg.mask.from_surface(asteroid_img_new)
        if save_speed != None:
            speed = save_speed
        else:
            speed = 10

        reset_afterwards = False
    if allow:
        if difficulty == 1:
            chance = randint(1, 10)
            sloweroid_difficulty = [1]
            fasteroid_difficulty = [10]
        elif difficulty == 2:
            chance = randint(1, 10)
            sloweroid_difficulty = [1]
            fasteroid_difficulty = [1, 2]
        elif difficulty == 3:
            chance = randint(1, 20)
            sloweroid_difficulty = [1]
            fasteroid_difficulty = [1, 2, 3, 4, 5]
        elif difficulty == 4:
            chance = randint(1, 10)
            sloweroid_difficulty = []
            fasteroid_difficulty = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if chance in sloweroid_difficulty:
        asteroid_img = sloweroid
        asteroid_img_new = pg.transform.scale(asteroid_img, (400, 400))
        asteroid_mask = pg.mask.from_surface(asteroid_img_new)

        save_speed = speed
        speed /= 4

        reset_afterwards = True
    elif chance in fasteroid_difficulty:
        asteroid_img = fasteroid
        asteroid_img_new = pg.transform.scale(asteroid_img, (asteroid_size, asteroid_size))
        asteroid_mask = pg.mask.from_surface(asteroid_img_new)
        save_speed = speed
        speed = save_speed + 25

        reset_afterwards = True
    else:
        if save_speed != None:
            speed = save_speed
            save_speed = None
            reset_afterwards = False

def handle_events():
    global running, player_x_change, allow, chance, speed, debug_mode
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_x_change = -10
            if event.key == pg.K_RIGHT:
                player_x_change = 10
            if event.key == pg.K_q and debug_mode:
                speed += 5
            if event.key == pg.K_ESCAPE:
                return "start_page"
            if event.key == pg.K_1:
                if debug_mode == False and allow_debug:
                    debug_mode = True
                else:
                    debug_mode = False
        if event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_RIGHT):
                player_x_change = 0

def text(text_x, text_y):
    points_surface = font.render(f"Points: {round(points)}", True, (255, 255, 255))
    screen.blit(points_surface, (text_x, text_y))

def reset_asteroid():
    global change_size, asteroid_x, asteroid_y
    if asteroid_y > screen_y:
        asteroid_y = -120
        asteroid_x = randint(0, screen_x - asteroid_size)
        change_size = True

def button(screen, x, y, width, height, color, text):
    pg.draw.rect(screen, color, (x, y, width, height))
    text_rect = text.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text, text_rect)

def reset_game():
    global asteroid_x, asteroid_y, points, speed, player_x, player_x_change, change_size, chance, save_speed, allow
    asteroid_x = 0
    asteroid_y = 100
    speed = 10
    points = 0
    player_x = 540
    player_x_change = 0
    change_size = False
    chance = None
    save_speed = None
    allow = True



def start_animation():
    global start_text_x, start_text_y, name_text_x, name_text_y
    start_time = pg.time.get_ticks()
    duration = 4500
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_m:
                    return "start_page"

        screen.fill((0, 0, 0))

        studio_text = font.render(f"Epic Frame Studio presents...", True, (255, 255, 255))
        screen.blit(studio_text, (start_text_x, start_text_y))

        distance = 100 - start_text_x

        if start_text_x <= 100:
            start_text_x += max(1, (distance / (100 - (-800))) * 80)

        title_text = main_font.render(f"Asteroid Avoider 3000", True, (255, 255, 255))
        screen.blit(title_text, (name_text_x, name_text_y))

        distance_name = 200 - name_text_x

        if name_text_x <= 120:
            name_text_x += max(1, (distance_name / (200 - (-2000))) * 80)

        if pg.time.get_ticks() - start_time > duration:
            return "start_page"

        pg.display.update()
        clock.tick(30)


def start_page():
    global difficulty
    if not pg.mixer.music.get_busy():
        pg.mixer.music.load("Music/menu_music.mp3")
        pg.mixer.music.play(loops=-1, start=2.0)
        pg.mixer.music.set_volume(music_volume / 100)
    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if button2.x <= mouse_x <= button2.x + button2.width and button2.y <= mouse_y <= button2.y + button2.height:
                    reset_game()
                    return "main_page"
                if button3.x <= mouse_x <= button3.x + button3.width and button3.y <= mouse_y <= button3.y + button3.height:
                    return "credit_page"  
                if button6.x <= mouse_x <= button6.x + button6.width and button6.y <= mouse_y <= button6.y + button6.height:
                    return "settings_page"                
                if button5.x <= mouse_x <= button5.x + button5.width and button5.y <= mouse_y <= button5.y + button5.height:
                    if difficulty == 1:
                        difficulty = 2
                    elif difficulty == 2:
                        difficulty = 3
                    elif difficulty == 3:
                        difficulty = 4
                    elif difficulty == 4:
                        difficulty = 1
    
        screen.blit(asteroid_bg_new, (0, 0))

        game_name_text_surface = main_font.render(f"Asteroid Avoider 3000", True, (255, 255, 255))
        screen.blit(game_name_text_surface, (90, 70))

        start_text = font.render(f"Start", True, (0, 0, 0))
        button(screen, button2.x, button2.y, button2.width, button2.height, (194, 194, 194), start_text)

        credits_text = font.render(f"Credits", True, (0, 0, 0))
        button(screen, button3.x, button3.y, button3.width, button3.height, (194, 194, 194), credits_text)
        
        settings_text = font.render(f"Settings", True, (0, 0, 0))
        button(screen, button6.x, button6.y, button6.width, button6.height, (194, 194, 194), settings_text)

        if difficulty != 4:
            difficulty_text = font.render(f"Difficulty: " + str(difficulty), True, (0, 0, 0))
        else:
            difficulty_text = font.render(f"Difficulty: Hard", True, (0, 0, 0))
        
        button(screen, button5.x, button5.y, button5.width, button5.height, (194, 194, 194), difficulty_text)


        pg.display.update()

def settings_page():
    global back_text, slider_x, slider_y, slider_radius, music_volume, dragging
    reset_game()
    dragging = False
    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_9:
                    return "start_page"
            if event.type == pg.MOUSEBUTTONDOWN:
                if button4.x <= mouse_x <= button4.x + button4.width and button4.y <= mouse_y <= button4.y + button4.height:
                    return "start_page"
                if button7.x <= mouse_x <= button7.x + button7.width and button7.y <= mouse_y <= button7.y + button7.height:
                    return "key_tutorial_page"
                if 350 + slider_radius + 2 <= mouse_x <= 650 - slider_radius - 2 and 70 <= mouse_y <= 100:
                    dragging = True
            if event.type == pg.MOUSEBUTTONUP:
                dragging = False
        
        if dragging:
            if 350 + slider_radius + 2 <= mouse_x <= 650 - slider_radius - 2 and 70 <= mouse_y <= 100:
                slider_x = mouse_x
                music_volume = int((((slider_x - (350 + slider_radius + 2)) / (300 - 2 * slider_radius - 4)) * 100) + 50) - 50
                pg.mixer.music.set_volume(music_volume / 100)
        
        screen.fill(gray)

        music_text = big_font.render("Music Volume:", True, (0, 0, 0))
        screen.blit(music_text, (90, 70))

        pg.draw.rect(screen, (0, 0, 0), (350, 70, 300, 30))
        pg.draw.circle(screen, (255, 255, 255), (slider_x, slider_y), slider_radius)

        volume_text_surface = font.render(str(music_volume), True, (0, 0, 0))
        screen.blit(volume_text_surface, (680, 75))

        key_tutorial_text_surface = big_font.render(f"Key Tutorial:", True, (0, 0, 0))
        screen.blit(key_tutorial_text_surface, (90, 170))

        back_text = font.render(f"Back", True, (0, 0, 0))
        button(screen, button4.x, button4.y, button4.width, button4.height, (194, 194, 194), back_text)

        key_tutorial_text = font.render(f"Key Tutorial", True, (0, 0, 0))
        button(screen, button7.x, button7.y, button7.width, button7.height, (194, 194, 194), key_tutorial_text)


        pg.display.update()

def key_tutorial_page():
    global back_text
    reset_game()
    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_9:
                    return "start_page"
            if event.type == pg.MOUSEBUTTONDOWN:
                if button4.x <= mouse_x <= button4.x + button4.width and button4.y <= mouse_y <= button4.y + button4.height:
                    return "settings_page"
                if button7.x <= mouse_x <= button7.x + button7.width and button7.y <= mouse_y <= button7.y + button7.height:
                    return "key_tutorial_page"

        screen.fill(gray)

        right_text_surface = font.render(f"Press Right arrow to move the character right", True, (0, 0, 0))
        screen.blit(right_text_surface, (90, 100))

        left_text_surface = font.render(f"Press Left arrow to move the character left", True, (0, 0, 0))
        screen.blit(left_text_surface, (90, 140))

        escape_text_surface = font.render(f"Press Escape to exit the game", True, (0, 0, 0))
        screen.blit(escape_text_surface, (90, 180))

        red_button_text_surface = font.render(f"Click the red button to quit", True, (0, 0, 0))
        screen.blit(red_button_text_surface, (90, 220))

        back_text = font.render(f"Back", True, (0, 0, 0))
        button(screen, button4.x, button4.y, button4.width, button4.height, (194, 194, 194), back_text)


        pg.display.update()

def credit_page():
    global back_text
    reset_game()
    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_9:
                    return "start_page"
            if event.type == pg.MOUSEBUTTONDOWN:
                if button8.x <= mouse_x <= button8.x + button8.width and button8.y <= mouse_y <= button8.y + button8.height:
                    return "start_page"

        screen.fill(gray)

        andrey_text_surface = main_font.render(f"Game coder: Andrey", True, (0, 0, 0))
        screen.blit(andrey_text_surface, (90, 70))

        carter_text_surface = main_font.render(f"Art designer: Carter", True, (0, 0, 0))
        screen.blit(carter_text_surface, (90, 170))

        back_text = font.render(f"Back", True, (0, 0, 0))
        button(screen, button8.x, button8.y, button8.width, button8.height, (194, 194, 194), back_text)

        pg.display.update()

def main_page():
    global offset_x, offset_y, asteroid_y, player_x, speed, current_page
    pg.mixer.music.stop()
    while True:
        screen.fill((150, 150, 150))


    
        if handle_events() == "start_page":
            return "start_page"

        # Offset
        offset_x = asteroid_x - player_x
        offset_y = asteroid_y - player_y

        # Debug info
        if debug_mode:
            print(f"Player Position: ({player_x}, {player_y})")
            print(f"Asteroid Position: ({asteroid_x}, {asteroid_y})")
            print(f"Offset: ({offset_x}, {offset_y})")

            asteroid_rect = pg.Rect(asteroid_x, asteroid_y, asteroid_mask.get_size()[0], asteroid_mask.get_size()[1])
            player_rect = pg.Rect(player_x, player_y, player_mask.get_size()[0], player_mask.get_size()[1])

            pg.draw.rect(screen, (255, 0, 0), asteroid_rect, 2)
            pg.draw.rect(screen, (0, 255, 0), player_rect, 2)

        if player_mask.overlap(asteroid_mask, (offset_x, offset_y)):
            return "end_page"


        asteroid_y += speed
        player_x += player_x_change
        
        # Bounds
        if player_x < 0:
            player_x = 0
        if player_x > screen_x - 120:
            player_x = screen_x - 120

        reset_asteroid()

        # Draw objects
        asteroid(asteroid_x, asteroid_y)
        player(player_x, player_y)
        text(text_x, text_y)

        high_score = load_score()

        high_score_surface = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_surface, (10, 40))

        pg.display.update()

        speed += 0.005 * difficulty
        clock.tick(fps)

def end_page():
    global points, high_score
    high_score = load_score()
    if points > high_score:
        save_score(points)
        high_score = load_score()
    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_9:
                    return "start_page"
            if event.type == pg.MOUSEBUTTONDOWN:
                if button1.x <= mouse_x <= button1.x + button1.width and button1.y <= mouse_y <= button1.y + button1.height:
                    high_score = load_score()
                    return "start_page"
    

        screen.fill((240, 10, 33))

        end_text_surface = font.render(f"You died! Be better!", True, (0, 0, 0))
        screen.blit(end_text_surface, (screen_x // 2 - end_text_surface.get_width() // 2, 100))

        points_surface = big_font.render(f"Points: {round(points)}", True, (0, 0, 0))
        screen.blit(points_surface, (screen_x // 2 - points_surface.get_width() // 2, 200))

        high_score_surface = font.render(f"High Score: {high_score}", True, (0, 0, 0))
        screen.blit(high_score_surface, (screen_x // 2 - high_score_surface.get_width() // 2, screen_y // 2))

        button_text = font.render(f"Restart", True, (0, 0, 0))
        button(screen, button1.x, button1.y, button1.width, button1.height, (255, 255, 255), button_text)

        pg.display.update()

def main():
    global current_page
    while True:  
        if current_page == "start_animation":
            current_page = start_animation()
        if current_page == "start_page":
            current_page = start_page()
        if current_page == "main_page":
            current_page = main_page()
        if current_page == "end_page":
            current_page = end_page()
        if current_page == "credit_page":
            current_page = credit_page()
        if current_page == "settings_page":
            current_page = settings_page()
        if current_page == "key_tutorial_page":
            current_page = key_tutorial_page()


if __name__ == "__main__":
    main()

pg.quit()