""" The Spots File """

import pygame

WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)


class Spot:
    """ The nodes/boxes """

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """ Get the current position """
        return self.row, self.col

    def is_closed(self):
        """ Check if node is closed or not """
        return self.color == RED

    def is_open(self):
        """ Check if node is open of not """
        return self.color == GREEN

    def is_barrier(self):
        """ Check is node is a barrier """
        return self.color == BLACK

    def reset(self):
        """ Reset the status of the node """
        self.color = WHITE

    def make_start(self):
        """ Make the node the start node """
        self.color = ORANGE

    def make_end(self):
        """ Make the node the start node """
        self.color = TURQUOISE

    def make_closed(self):
        """ Make the node close """
        self.color = RED

    def make_open(self):
        """ Make the node open """
        self.color = GREEN

    def make_barrier(self):
        """ Make the node barrier """
        self.color = BLACK

    def make_path(self):
        """ Make the node a path """
        self.color = PURPLE

    def draw(self, win):
        """ Draw a box/node """
        pygame.draw.rect(
            win,
            self.color,
            (self.x, self.y, self.width, self.width)
        )

    def update_neighbors(self, grid):
        """ Add the blocks/nodes that are potential neighbours together """

        self.neighbors = []
        if self.row < self.total_rows - \
                1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - \
                1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])


def make_grid(rows, width):
    """ Making the grid """
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    """ Drawing the grid """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(
            win,
            GREY,
            (0, i * gap),
            (width, i * gap)
        )
        for j in range(rows):
            pygame.draw.line(
                win,
                GREY,
                (j * gap, 0),
                (j * gap, width)
            )


def draw(win, grid, rows, width):
    """ Updating the canvas after changing colors """
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    """ Get the clicked position """
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def reconstruct_path(came_from, current, draw):
    """ Reconstruct the path between start and the end node """
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()
