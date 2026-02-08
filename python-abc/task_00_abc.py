#!/usr/bin/python3
"""
    Class file for ABC class.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """ Abstract class for Animal. """

    @abstractmethod
    def sound(self):
        """ Make a sound of the animal. """
        pass


class Dog(Animal):
    """ Sub class for a Dog Animal. """

    def sound(self):
        """ Make a sound of the dog. """
        return "Bark"


class Cat(Animal):
    """ Sub class for a Cat Animal. """

    def sound(self):
        """ Make a sound of the cat. """
        return "Meow"
