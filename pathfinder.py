import pygame
import math
from queue import PriorityQueue 

Width = 800
WIN = pygame.display.set_mode((Width, Width))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Node:
    def _init_(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_position(self):
        #Indexing things using row columns, starting with the row as x and col as Y
        return self.row, self.col

    def is_closed(self):
        #Tells us it is a square that we have already looked at
        return self.color == RED




