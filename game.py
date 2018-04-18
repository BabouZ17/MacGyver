#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# MacGyver game using a maze
# The main character : MacGyver is supposed to go through the maze and
# defeat his opponent Murdoc. Also, to succeed in the level, the Mac
# Gyver character has to collect all the items in the level before
# reaching the murdoc character, otherwise Mac will die which ends
# the game.

"""
Python file from where the game is called thanks to
the main function. We call all the instances needed
before running the main loop listening to all the
events happening in the game.
"""

from constants import MURDOC_IMG_PATH, MAC_GYVER_IMG_PATH, NEEDLE_IMG_PATH, \
TUBE_IMG_PATH, ETHER_IMG_PATH
from frame import Frame
from character import Character
from item import Item
from mypygame import Mypygame

def main():
    """
    Function called to start the game instance
    """

    pygame_wp = Mypygame()

    murdoc = Character('murdoc', MURDOC_IMG_PATH, (14, 14))
    mac = Character('mac', MAC_GYVER_IMG_PATH, (1, 0), True)

    needle = Item('needle', NEEDLE_IMG_PATH)
    tube = Item('tube', TUBE_IMG_PATH)
    ether = Item('ether', ETHER_IMG_PATH)

    game_frame = Frame(items=[needle, tube, ether], characters=[mac, murdoc])
    game_frame.prepare_map()

    # Main Loop
    while not game_frame.is_over and not game_frame.is_won:
        for event in pygame_wp.get_events():
            if game_frame.is_quited(event):
                game_frame.is_over = True

        pressed_keys = pygame_wp.pressed_keys()
        game_frame.manage_moves(pressed_keys, mac)

        # Update the background
        pygame_wp.elements_blit([game_frame.game_map, murdoc, mac])

        # Update the screen
        pygame_wp.display_flip()

        # Check if the game is over
        game_frame.is_finished(mac.position, murdoc.position)

        # Display end screen
        if game_frame.is_over:
            pygame_wp.display_end_game(game_frame.is_won)

if __name__ == '__main__':
    main()
