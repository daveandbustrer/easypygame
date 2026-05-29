import pygame as pyg
from .variables import isRunning


def init():
    isRunning = True
    return pyg.init()
