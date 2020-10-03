from Spots import *
import queue
import timeit


def bfs_compute(draw, grid, start, end):
    """ Computing the bfs """
    visited = []
    came_from = {}
    the_queue = queue.Queue()
    visited.append(start)
    the_queue.put(start)

    # algorithm: https://en.wikipedia.org/wiki/Breadth-first_search#Pseudocode
    start_time = timeit.default_timer()
    while not the_queue.empty():

        current = the_queue.get()

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            end_time = timeit.default_timer()
            print('Time: ', end_time - start_time)
            return True

        for neighbors in current.neighbors:
            if neighbors not in visited:
                visited.append(neighbors)
                came_from[neighbors] = current
                the_queue.put(neighbors)
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

                    bfs_compute(
                        lambda: draw(
                            win, grid, ROWS, width
                        ),
                        grid, start, end
                    )


main(WIN, WIDTH)
