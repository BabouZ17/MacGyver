#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# This class represents the game frame and provides methods
# in order to manage the events in the game such as a move
# from the character, checking if the game is over or
# preparing the map.

"""
This class represents the game frame and deals
with all the logic which occurs during a game such
as the moves made by the player, checking if the
game is over or preparing the map.
"""

from json import load
from random import randint
from constants import MAP_FILE_PATH, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT, \
KEY_QUIT


class Frame:
    """
    Class representing the game frame and actions.
    This class deals with all the logic and events
    coming from the play actions.
    The attributes are:
        -   is_over (bool)
        -   is_won (bool)
        -   game_map(json file)
        -   characters (Characters instances list)
        -   items (Items instances list)
    """
    def __init__(self, characters, items):
        """
        Constructor of Main class
        """
        self.is_over = False
        self.is_won = False
        self.game_map = load(open(MAP_FILE_PATH))['map']
        self.characters = characters
        self.items = items

    def prepare_map(self):
        """
        Fill the map with items and characters in the list
        """
        items_ready = 0

        for character in self.characters:
            self.game_map[character.position[1]]\
            [int(character.position[0])] = character.sub_name

        while items_ready != len(self.items):
            for item in self.items:
                for row_index, row in enumerate(self.game_map):
                    for index, element in enumerate(row):
                        if element == "" and randint(0, 50) == 1 and \
                        item.position == (0, 0):
                            item.position = (index, row_index)
                            row[index] = item.sub_name
                            items_ready += 1

    def is_correct_position(self, character_position):
        """
        Check if the new character position is out of
        range.Check if the character move is possible
        or not and return a boolean.
        Also check if the character moves into an item
        and if so, collect the item.
        """
        if character_position[1] > len(self.game_map) - 1 or \
        character_position[0] > len(self.game_map) - 1 or \
        character_position[0] < 0 or character_position[1] < 0:
            return False

        for item in self.items:
            if self.game_map[character_position[1]][character_position[0]] \
            == item.sub_name:
                self.game_map[character_position[1]][character_position[0]] = ''

                # Update Item attribute
                item.is_collected = True

                # Update character inventory
                character = [character for character in self.characters \
                if character.is_hero]
                character[0].collect_item(item)
                return True

        for character in self.characters:
            if self.game_map[character_position[1]][character_position[0]] \
            == character.sub_name:
                self.game_map[character_position[1]][character_position[0]] = ''
                return True

        return bool(self.game_map[character_position[1]]\
        [character_position[0]] == '')


    def manage_moves(self, keys_pressed, character):
        """
        Make the Character move regarding to the keys pressed.
        """
        # Down
        if keys_pressed[KEY_UP] == 1:
            if self.is_correct_position((character.position[0], \
            character.position[1] - 1)):
                character.vertical_move(-1)
        # Up
        if keys_pressed[KEY_DOWN] == 1:
            if self.is_correct_position((character.position[0], \
            character.position[1] + 1)):
                character.vertical_move(1)
        # Left
        if keys_pressed[KEY_LEFT] == 1:
            if self.is_correct_position((character.position[0] - 1, \
            character.position[1])):
                character.horizontal_move(-1)
        # Right
        if keys_pressed[KEY_RIGHT] == 1:
            if self.is_correct_position((character.position[0] + 1, \
            character.position[1])):
                character.horizontal_move(1)

    def is_quited(self, event):
        """
        Check if the event type is a pygame.QUIT
        and return a boolean.
        Pygame pygame.QUIT value is 12
        """
        return bool(event.type == KEY_QUIT)

    def is_finished(self, p_pos, opp_pos):
        """
        Check either if the game is won or lost
        """
        if [item.is_collected for item in self.items].count(True) == \
        len(self.items) and p_pos == opp_pos:
            self.is_over = True
            self.is_won = True

        if [item.is_collected for item in self.items].count(True) != \
        len(self.items) and p_pos == opp_pos:
            self.is_over = True
