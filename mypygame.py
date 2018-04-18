#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Wrapper for pygame

"""
Class that wraps the pygame calls so it makes
easier to edit the game if the pygame library
receives changes in the future.
"""

import pygame

from constants import GAME_NAME, GAME_WINDOW_SIZE, BACKGROUND_IMG_PATH, \
FONT, FONT_SIZE, SIZE_FACTOR, WALL_IMG_PATH, TUBE_IMG_PATH, ETHER_IMG_PATH, \
START_IMG_PATH, NEEDLE_IMG_PATH, WHITE, SUCCESS_MSG, DEATH_MSG, RED, FRAME_RATE

class Mypygame():
    """
    Create a wrapper of for a pygame instance
    to modify if changes appear in the pygame
    library. We initialize pygame within the
    constructor.
    The attributes are:
        - screen (pygame screen)
        - background (pygame image)
        - font (pygame font)
        - clock (pygame clock)
    """

    def __init__(self):
        """
        Constructor of the pygame wrapper
        """
        pygame.init()
        pygame.display.set_caption(GAME_NAME)
        self.screen = pygame.display.set_mode(GAME_WINDOW_SIZE)
        self.background = pygame.transform.scale(\
        pygame.image.load(BACKGROUND_IMG_PATH), GAME_WINDOW_SIZE)
        self.font = pygame.font.SysFont(FONT, FONT_SIZE)
        self.clock = pygame.time.Clock()

    def click(self, value):
        """
        Update the Clock and limit the framerate
        """
        self.clock.tick(value)

    def add_image(self, image):
        """
        Add image to the pygame instance
        """
        return pygame.transform.scale(pygame.image.load(image), \
            (SIZE_FACTOR, SIZE_FACTOR))

    def image_blit(self, image, coordinates=(0, 0)):
        """
        A method to blit the image
        """
        return self.screen.blit(image, coordinates)

    def elements_blit(self, elements):
        """
        A method to blit all the elements in the a provided list
        and the background. Also tick the clock object.
        """
        self.image_blit(self.background, (0, 0))
        for element in elements:
            if isinstance(element, list):
                for row_index, row in enumerate(element):
                    for index, value in enumerate(row):
                        if value == 's':
                            self.screen.blit(self.add_image(START_IMG_PATH), \
                            (index * SIZE_FACTOR, row_index * SIZE_FACTOR))
                        if value == 'w':
                            self.screen.blit(self.add_image(WALL_IMG_PATH), \
                            (index * SIZE_FACTOR, row_index * SIZE_FACTOR))
                        elif value == 't':
                            self.screen.blit(self.add_image(TUBE_IMG_PATH), \
                            (index * SIZE_FACTOR, row_index * SIZE_FACTOR))
                        elif value == 'e':
                            self.screen.blit(self.add_image(ETHER_IMG_PATH), \
                            (index * SIZE_FACTOR, row_index * SIZE_FACTOR))
                        elif value == 'n':
                            self.screen.blit(self.add_image(NEEDLE_IMG_PATH), \
                            (index * SIZE_FACTOR, row_index * SIZE_FACTOR))
            if 'Character' in str(type(element)):
                self.image_blit(element.image, (element.position[0] * SIZE_FACTOR, \
                element.position[1] * SIZE_FACTOR))
            self.clock.tick(FRAME_RATE)

    def display_flip(self):
        """
        Flip the display
        """
        return pygame.display.flip()

    def get_events(self):
        """
        Listen to the events triggered by the player
        """
        return pygame.event.get()

    def pressed_keys(self):
        """
        Listen to pressed keys by the player
        """
        return pygame.key.get_pressed()

    def display_end_game(self, result):
        """
        Fill the screen and displays an end message depending on result
        (if you won or not).
        """
        # Win
        self.screen.fill(WHITE)
        if result:
            render = self.font.render(SUCCESS_MSG, False, (0, 0, 0))
            self.image_blit(render, ((GAME_WINDOW_SIZE[0] - 200) / 2,\
            GAME_WINDOW_SIZE[0] / 2))
        # Lose
        else:
            render = self.font.render(DEATH_MSG, False, RED)
            self.image_blit(render, ((GAME_WINDOW_SIZE[0] - 200) / 2,\
            GAME_WINDOW_SIZE[0] / 2))
        self.display_flip()
        pygame.time.delay(2000)
