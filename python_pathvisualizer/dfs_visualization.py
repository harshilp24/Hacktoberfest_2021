from Spots import *
import timeit
# import pygame

pygame.display.set_caption("DFS Visualizer")


def dfs_compute(draw, grid, start, end):
    """ Computing the DFS """
    visited = []
    the_stack = []
    the_stack.append(start)
    came_from = {}
    visited.append(start)

    start_time = timeit.default_timer()
    while len(the_stack) != 0:
        current = the_stack.pop()

        if current == end:
            stop_time = timeit.default_timer()
            end.make_end()
            reconstruct_path(came_from, end, draw)
            print('Time: ', stop_time - start_time)
            return True

        for neighbors in current.neighbors:
            if neighbors not in visited:
                visited.append(neighbors)
                came_from[neighbors] = current
                the_stack.append(neighbors)
                neighbors.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def main(win, width):
    """ The main function """
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and spot != end:
                    start = spot
                    start.make_start()
                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot not in (start, end):
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    dfs_compute(lambda: draw(
                        win, grid, ROWS, width
                    ),
                        grid, start, end)


main(WIN, WIDTH)
