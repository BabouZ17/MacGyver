#! /user/bin/env python
# -*- coding: utf-8 -*-
# File which contains the constants for the game

"""
File containing all the constants used in the game
"""

# Frame Rate
FRAME_RATE = 20

# Fonts
FONT = 'comicsans'
FONT_SIZE = 30

# Messages
DEATH_MSG = 'Oh... You Lost ..., Try Again !'
SUCCESS_MSG = 'Congretulations ! You Won !'
GAME_NAME = 'MacGyver Python Game'

# Pygame pressed keys values
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_QUIT = 12

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Either 900*900 or 450*450 for the Window Size
GAME_WINDOW_SIZE = (900, 900)
SIZE_FACTOR = int(GAME_WINDOW_SIZE[0] * 2 / 30)
STEP_SIZE = SIZE_FACTOR
IMAGE_FACTOR = 60

# MAP FILE PATH
MAP_FILE_PATH = 'components/map.json'

# Images files
MAC_GYVER_IMG_PATH = 'components/mac_gyver.png'
MURDOC_IMG_PATH = 'components/murdoc.png'
START_IMG_PATH = 'components/start.png'
WALL_IMG_PATH = 'components/wall.png'
BACKGROUND_IMG_PATH = 'components/background.jpg'
NEEDLE_IMG_PATH = 'components/needle.png'
TUBE_IMG_PATH = 'components/tube.png'
ETHER_IMG_PATH = 'components/ether.png'
