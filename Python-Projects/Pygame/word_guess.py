import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 700
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (200, 200, 0)
GRAY = (160, 160, 160)
BACKGROUND_COLOR = (100, 100, 100)

# Load Sounds
win_sound = pygame.mixer.Sound("D:\Python-Practice\Pygame\winning_sound.mp3")
# Load Words & Themes
words = {"Animals": ["tiger", "zebra", "horse", "sheep", "eagle"],
         "Fruits": ["apple", "mango", "grape", "peach", "melon"]}

theme = random.choice(list(words.keys()))
word = random.choice(words[theme]).upper()

# Game Variables
attempts = 6
guess_length = len(word)
guesses = ["" for _ in range(attempts)]
colors = [[WHITE for _ in range(guess_length)] for _ in range(attempts)]
current_guess = ""
current_row = 0

# Pygame Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Word Guessing Game")
font = pygame.font.Font(None, 50)
keyboard_font = pygame.font.Font(None, 40)
clock = pygame.time.Clock()

# Keyboard Layout
keys = "QWERTYUIOPASDFGHJKLZXCVBNM"
keyboard = {letter: [(50 + (i % 10) * 50, 500 + (i // 10) * 50), GRAY] for i, letter in enumerate(keys)}

# Virtual Keyboard Rectangles
key_rects = {letter: pygame.Rect(pos[0], pos[1], 40, 40) for letter, (pos, _) in keyboard.items()}

def draw_board():
    screen.fill(BACKGROUND_COLOR)
    theme_text = font.render(f"Theme: {theme}", True, BLACK)
    screen.blit(theme_text, (20, 20))
    
    for row in range(attempts):
        for col in range(guess_length):
            x, y = 50 + col * 60, 100 + row * 60
            pygame.draw.rect(screen, colors[row][col], (x, y, 50, 50))
            pygame.draw.rect(screen, BLACK, (x, y, 50, 50), 2)
            if col < len(guesses[row]):
                letter = font.render(guesses[row][col], True, BLACK)
                screen.blit(letter, (x + 15, y + 10))
    
    # Display current typing guess
    for col, letter in enumerate(current_guess):
        x, y = 50 + col * 60, 100 + current_row * 60
        text = font.render(letter, True, BLACK)
        screen.blit(text, (x + 15, y + 10))
    
    for letter, (pos, color) in keyboard.items():
        pygame.draw.rect(screen, color, (*pos, 40, 40))
        text = keyboard_font.render(letter, True, BLACK)
        screen.blit(text, (pos[0] + 10, pos[1] + 5))

def check_guess():
    global current_row, current_guess
    if len(current_guess) != guess_length:
        return
    
    guesses[current_row] = current_guess
    
    word_count = {letter: word.count(letter) for letter in set(word)}
    
    # First pass to mark correct positions
    for i, letter in enumerate(current_guess):
        if letter == word[i]:
            colors[current_row][i] = GREEN
            keyboard[letter][1] = GREEN
            word_count[letter] -= 1
    
    # Second pass to mark misplaced letters
    for i, letter in enumerate(current_guess):
        if letter in word and word_count[letter] > 0 and colors[current_row][i] != GREEN:
            colors[current_row][i] = YELLOW
            keyboard[letter][1] = YELLOW
            word_count[letter] -= 1
    
    if current_guess == word:
        pygame.display.set_caption("You Won!")
        win_sound.play()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()
    
    current_row += 1
    current_guess = ""
    if current_row == attempts:
        pygame.display.set_caption(f"Game Over! Word: {word}")
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

def main():
    global current_guess
    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        draw_board()
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if len(current_guess) == guess_length:
                        check_guess()
                elif event.key == pygame.K_BACKSPACE:
                    current_guess = current_guess[:-1]
                elif event.unicode.upper() in keys and len(current_guess) < guess_length:
                    current_guess += event.unicode.upper()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for letter, rect in key_rects.items():
                    if rect.collidepoint(mouse_pos) and len(current_guess) < guess_length:
                        current_guess += letter
                        break
        
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()
