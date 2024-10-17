import pygame
import random as rand
import string
import sys
import os
from startScreen import *
from globals import *
from leaderboard import get_leaderboard
import pygame.gfxdraw

# Game end screen function
def game_end(screen, clock, background_color, player_name):

    celeb_text = pygame.font.Font(os.path.join(auxDirectory, 'MR ROBOT.ttf'), 140)
    large_text = pygame.font.Font('freesansbold.ttf', 45)
    small_text = pygame.font.Font('freesansbold.ttf', 20)

    while True:

        # To smoothly shine winning message
        delay = 0

        screen.fill(background_color)

        # Set flashing colors
        color_x = rand.randint(0, 4)
        color_y = rand.randint(0, 1)

        # Get inputs
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            # Press R to reset game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return 1
            # Press M to go to menu
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                return 2
            # Press esc or Q to quit
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Print which player won
        if delay == 0:
            # Fix: Change string.upper(player_name) to player_name.upper()
            disp_text(screen, "{0} WINS".format(player_name.upper()), (width / 2, height / 2 - 150),
                      celeb_text, colors[color_x][color_y])

        # Drawing buttons for reset, menu, and exit.
        # Reset button
        if abs(mouse_pos[0] - 200) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[0][0], (200, 470), "Reset", large_text, (255, 255, 255),
                          (width / 2 - 400, height / 2 + 170))
            if mouse_press[0] == 1:
                return 1
        else:
            button_circle(screen, colors[0][0], (200, 470), "Reset", small_text, (255, 255, 255),
                          (width / 2 - 400, height / 2 + 170))

        # Menu button
        if abs(mouse_pos[0] - 600) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[4][1], (600, 470), "Menu", large_text, (255, 255, 255),
                          (width / 2, height / 2 + 170))
            if mouse_press[0] == 1:
                return 2
        else:
            button_circle(screen, colors[4][1], (600, 470), "Menu", small_text, (255, 255, 255),
                          (width / 2, height / 2 + 170))

        # Quit button
        if abs(mouse_pos[0] - 1000) < buttonRadius and abs(mouse_pos[1] - 470) < buttonRadius:
            button_circle(screen, colors[1][1], (1000, 470), "Quit", large_text, (255, 255, 255),
                          (width / 2 + 400, height / 2 + 170))
            if mouse_press[0] == 1:
                pygame.quit()
                return 3
        else:
            button_circle(screen, colors[1][0], (1000, 470), "Quit", small_text, (255, 255, 255),
                          (width / 2 + 400, height / 2 + 170))

        # Draw the leaderboard
        draw_leaderboard(screen, small_text)

        pygame.display.update()
        clock.tick(10)

# Add this function to draw the leaderboard
def draw_leaderboard(screen, font):
    leaderboard = get_leaderboard()
    title = font.render("LEADERBOARD", True, const.WHITE)
    screen.blit(title, (width / 2 - title.get_width() / 2, 100))

    for i, entry in enumerate(leaderboard):
        text = font.render(f"{i+1}. {entry['name']}: {entry['score']}", True, const.WHITE)
        screen.blit(text, (width / 2 - text.get_width() / 2, 150 + i * 30))
