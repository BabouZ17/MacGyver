#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# An item represents an object on the map that a character can collect

"""
Class that represents an item that a character can collect during the
game to finish it.
"""

import pygame

from constants import IMAGE_FACTOR

class Item:
    """
    Item that a character can collect.
    Theses objects are randomely displayed
    on the map at the beginning of the game.
    The attributes are:
        -   name (string)
        -   sub_name (string)
        -   image (pygame image)
        -   is_collected (bool)
        -   position (tuple)
    """

    def __init__(self, name, image_path, position=(0, 0)):
        """
        Constructor of the Item class
        """
        self.name = name
        self.sub_name = self.name[0:1]
        self.image = pygame.transform.scale(pygame.image.load(image_path), \
        (IMAGE_FACTOR, IMAGE_FACTOR))
        self.image.convert_alpha()
        self.is_collected = False
        self.position = (position[0], position[1])

    def __repr__(self):
        """
        Magic method to represent the Item Class
        """
        return 'Item : {}, collected yet: {} and location is : {}'\
        .format(self.name, self.is_collected, self.position)
