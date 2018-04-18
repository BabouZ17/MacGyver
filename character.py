#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Class that represents a character (which you can play or not).
The character (if it's the hero) can move on the map and collect
items.
"""

import pygame

from constants import IMAGE_FACTOR

class Character:
    """
    Create a character which has :
        - a name  (string)
        - a sub_name (string) (which is the name in the map)
        - an image path for the image use by pygame
        - a position (tuple), first element is vertical,
        second element is horizontal
        - is_hero (bool), tells that the character is the player
        or not
        - inventory (list of items objects) an inventory to store
        the items
    """

    def __init__(self, name, image_path, position, is_hero=False):
        """
        Constructor of the Character class
        """
        self.name = name
        self.sub_name = self.name[0:2]
        self.is_hero = is_hero
        self.position = (position[0], position[1])
        self.image = pygame.transform.scale(pygame.image.load(image_path), \
        (IMAGE_FACTOR, IMAGE_FACTOR))
        self.image.convert_alpha()
        self.inventory = []

    def __repr__(self):
        """
        Magic method to represent the character instance
        """
        return 'Character : {}, position: {}, {}'\
        .format(self.name, self.position[0], self.position[1])

    def vertical_move(self, value):
        """
        Change the vertical position of the Character
        """
        self.position = (self.position[0], self.position[1] + value)

    def horizontal_move(self, value):
        """
        Change the horizontal position of the Character
        """
        self.position = (self.position[0] + value, self.position[1])

    def collect_item(self, item):
        """
        Add an item on the character inventory
        """
        self.inventory.append(item)
