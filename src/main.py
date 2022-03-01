import pygame
from game import Game
from board import Board
from piece import *

if __name__ == "__main__":
    pygame.init()
    game = Game()
    board = Board()
    board.draw()
    game.run()