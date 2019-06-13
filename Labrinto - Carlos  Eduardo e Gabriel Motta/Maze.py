import pygame
import random

class MazeGenerator:
    BRANCH_FACTOR = 5

    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.unvisited = dict(self.maze.tiles)
        self.current = None

    def make_start(self):
        start = self.maze.tiles[(0, random.randint(0, self.maze.grid_size))]
        start.startend = True
        self.remove_outer_wall(start)
        return start

    def make_maze(self):
        while self.unvisited:
            self.current.filled = False
            self.current.active = True
            if (self.current.x, self.current.y) in self.unvisited.keys():
                del self.unvisited[(self.current.x, self.current.y)]
            if not self.unvisited:
                break

            if self.path:
                self.current.active = False
                self.current = self.path.pop()
            else:
                self.current.active = False
                self.current = random.choice(self.unvisited.values())

    def step(self):
        if not self.maze.start:
            self.maze.start = self.make_start()
            self.current = self.maze.start
            self.current.filled = False
            self.current.active = True

        if self.unvisited:
            if (self.current.x, self.current.y) in self.unvisited.keys():
                del self.unvisited[(self.current.x, self.current.y)]
            if not self.unvisited:
                self.current.active = False
                self.maze.end = self.make_end()
                return

            adjacent = self.get_adjacent_unvisited(self.current)
            if adjacent:
                self.path.append(self.current)
                next = random.choice(adjacent)
                next.path_length = self.current.path_length + 1
                self.maze.get_wall(self.current, next).filled = False
                self.current.active = False
                self.current = next
            elif self.path:
                self.current.active = False
                self.current = self.path.pop()
            else:
                self.current.active = False
                self.current = random.choice(self.unvisited.values())

            self.current.filled = False
            self.current.active = True

    def get_adjacent_unvisited(self, tile, check_branching=True):
        coords = [(tile.x+1, tile.y), (tile.x, tile.y+1), (tile.x-1, tile.y),
                  (tile.x, tile.y-1)]
        adj = [self.maze.tiles.get(c) for c in coords if c
               in self.unvisited.keys()]

        if check_branching:
            adj_branching = list(adj)
            for adj_tile in adj:
                tile_adj = self.get_adjacent_unvisited(adj_tile,
                                                       check_branching=False)
                if len(tile_adj) > 2:
                    adj_branching += [adj_tile] * self.BRANCH_FACTOR

            adj = adj_branching

        return adj

    def make_end(self):
        max_path = -1
        end = None
        for tile in self.maze.get_edge_tiles():
            if tile.path_length > max_path:
                max_path = tile.path_length
                end = tile
        end.startend = True
        self.remove_outer_wall(end)
        return end

    def remove_outer_wall(self, tile):
        outer_wall = self.maze.get_outer_walls(tile)[0]
        if outer_wall:
            outer_wall.filled = False
            outer_wall.startend = True


class Kruskal:


    def __init__(self, maze):
        self.maze = maze
        self.open_list = []
        self.closed_list = []
        self.path = []
        self.path_walls = []
        self.start = None
        self.end = None
        self.done = False

    def retrace(self, current):
        self.path = [current]
        while current.parent:
            self.path_walls.append(self.maze.get_wall(current.tile,
                                                      current.parent.tile))
            current = current.parent
            self.path.append(current)

        self.path.reverse()

    def step(self, current):
        if not current:
            self.start = Node(self.maze.start)
            self.end = Node(self.maze.end)
            current = self.start
            self.open_list.append(current)

        if self.open_list:
            current = min(self.open_list, key=lambda elem: elem.h)
            if current == self.end:
                self.done = True
                return self.retrace(current)
            self.open_list.remove(current)
            self.closed_list.append(current)

            for tile in self.maze.get_accessible_tiles(current.tile):
                node = Node(tile)
                if node not in self.closed_list:
                    if node not in self.open_list:
                        self.open_list.append(node)
                        node.parent = current
                        node.distance = node.parent.distance + 1
                        node.h = node.distance + \
                            self.heuristic(tile, self.end.tile)
                    else:
                        dist = current.distance + 1
                        if dist < node.distance:
                            node.parent = current
                            node.distance = dist
                            node.h = dist + self.heuristic(tile, self.end.tile)

                    node.parent = current
            return current
        else:
            self.done = True

    @staticmethod
    def heuristic(t1, t2):
        return abs(t1.x - t2.x) + abs(t1.y - t2.y)


class Node:
    def __init__(self, tile):
        self.tile = tile
        self.distance = 0
        self.h = 0
        self.parent = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.tile.x == other.tile.x and self.tile.y == other.tile.y:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Maze:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.tiles = self.make_tiles()
        self.walls = self.make_walls()
        self.start = None
        self.end = None

    def make_tiles(self):
        return {(i, j): Tile(i, j) for i in range(self.grid_size)
                for j in range(self.grid_size)}

    def make_walls(self):
        hor = {(i, j, "h"): Wall(i, j) for i in range(self.grid_size)
               for j in range(self.grid_size + 1)}
        ver = {(i, j, "v"): Wall(i, j) for i in range(self.grid_size + 1)
               for j in range(self.grid_size)}

        hor.update(ver)
        return hor

    def get_wall(self, t1, t2):
        dx = t1.x - t2.x
        dy = t1.y - t2.y
        if dy == 0:
            if dx == 1:
                return self.walls[(t1.x, t1.y, "v")]
            if dx == -1:
                return self.walls[(t2.x, t2.y, "v")]
        if dx == 0:
            if dy == 1:
                return self.walls[(t1.x, t1.y, "h")]
            if dy == -1:
                return self.walls[(t2.x, t2.y, "h")]

    def get_accessible_tiles(self, tile):
        coords = [(tile.x+1, tile.y), (tile.x, tile.y+1), (tile.x-1, tile.y),
                  (tile.x, tile.y-1)]
        adjacent = [self.tiles.get(c)
                    for c in coords if c in self.tiles.keys()]
        return [t for t in adjacent if not self.get_wall(tile, t).filled]

    def get_edge_tiles(self):
        edge_tiles = [self.tiles[(0, i)] for i in range(self.grid_size)]
        edge_tiles += [self.tiles[(i, 0)] for i in range(self.grid_size)]
        edge_tiles += [self.tiles[(i, self.grid_size-1)]
                       for i in range(self.grid_size)]
        edge_tiles += [self.tiles[(self.grid_size-1, i)]
                       for i in range(self.grid_size)]
        return edge_tiles

    def get_outer_walls(self, tile):
        outer_walls = []
        if tile.x == 0:
            outer_walls.append(self.walls[(tile.x, tile.y, 'v')])
        if tile.x == self.grid_size - 1:
            outer_walls.append(self.walls[(tile.x + 1, tile.y, 'v')])
        if tile.y == 0:
            outer_walls.append(self.walls[(tile.x, tile.y, 'h')])
        if tile.y == self.grid_size - 1:
            outer_walls.append(self.walls[(tile.x, tile.y + 1, 'h')])

        return outer_walls

    def finished(self):
        if self.start and self.end:
            return True
        return False


class Tile:
    def __str__(self):
        return "Tile: {0}, {1}".format(self.x, self.y)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filled = True
        self.active = False
        self.startend = False
        self.path_length = 0
        self.in_path = False


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.filled = True
        self.startend = False
        self.in_path = False


class Labyrinth:
    FPS = 30
    BACKGROUND = (55, 55, 155)
    WALLS = (0, 0, 0)
    ACTIVE_TILE = (255, 255, 255)
    START_END = (200, 170, 250)
    COLOR_PATH = (55, 255, 155)
    WALL_SIZE = 4
    OFFSET = 4

    def __init__(self, screen_size=820, generate_speed=1,
                 solve_speed=1, size=90):
        self.screen_size = screen_size
        self.name = ("Labirinto "+str(size)+" x "+ str(size))
        self.maze = Maze(size)
        self.maze_size, self.tile_size = self.set_dimensions()
        self.gen = MazeGenerator(self.maze)
        self.generate_speed = generate_speed
        self.solve_speed = solve_speed
        self.solver = Kruskal(self.maze)

    def set_dimensions(self):
        maze_size = self.screen_size - 2*self.OFFSET
        tile_size = (maze_size / self.maze.grid_size)
        return maze_size, tile_size

    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((self.screen_size,
                                          self.screen_size))
        pygame.display.set_caption(self.name)

        clock = pygame.time.Clock()
        running = True
        make_maze = False
        solve_maze = False
        current = None

        while running:
            if current:
                current.tile.active = False
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    make_maze = not make_maze
                    if self.maze.finished():
                        solve_maze = not solve_maze
                if event.type == pygame.QUIT:
                    running = False

            if make_maze and not self.maze.finished():
                for _ in range(self.generate_speed):
                    self.gen.step()

            if solve_maze and not self.solver.done:
                for _ in range(self.solve_speed):
                    current = self.solver.step(current)
                if current:
                    current.tile.active = True
                if self.solver.done:
                    for node in self.solver.path:
                        node.tile.in_path = True
                    for wall in self.solver.path_walls:
                        wall.in_path = True

            screen.fill(self.BACKGROUND)
            self.draw_maze(screen)
            pygame.display.flip()
            clock.tick(self.FPS)

        pygame.quit()

    def draw_maze(self, screen):
        self.draw_walls(screen)
        self.draw_tiles(screen)

    def draw_walls(self, screen):
        x = self.OFFSET
        y = self.OFFSET

        for j in range(self.maze.grid_size + 1):
            for i in range(self.maze.grid_size + 1):
                # Draw dot
                pygame.draw.rect(screen, self.WALLS, (x, y,
                                                           self.WALL_SIZE,
                                                           self.WALL_SIZE))

                wall_length = self.tile_size - self.WALL_SIZE

                # Draw horizontal walls
                if i < self.maze.grid_size:
                    hor = self.maze.walls[(i, j, 'h')]
                    if hor.startend:
                        color = self.START_END
                    elif hor.in_path:
                        color = self.COLOR_PATH
                    else:
                        color = self.WALLS if hor.filled else self.BACKGROUND
                    pygame.draw.rect(screen, color,
                                     (x + self.WALL_SIZE, y,
                                      wall_length, self.WALL_SIZE))

                # Draw vertical walls
                if j < self.maze.grid_size:
                    pass
                    ver = self.maze.walls[(i, j, 'v')]
                    if ver.startend:
                        color = self.START_END
                    elif ver.in_path:
                        color = self.COLOR_PATH
                    else:
                        color = self.WALLS if ver.filled else self.BACKGROUND
                    pygame.draw.rect(screen, color,
                                     (x, y + self.WALL_SIZE,
                                      self.WALL_SIZE, wall_length))

                x += self.tile_size

            x = self.OFFSET
            y += self.tile_size

    def draw_tiles(self, screen):
        x = self.OFFSET + self.WALL_SIZE
        y = self.OFFSET + self.WALL_SIZE
        rect_size = self.tile_size - self.WALL_SIZE

        for j in range(self.maze.grid_size):
            for i in range(self.maze.grid_size):
                tile = self.maze.tiles[(i, j)]

                if tile.active:
                    color = self.ACTIVE_TILE
                elif tile.startend:
                    color = self.START_END
                elif tile.in_path:
                    color = self.COLOR_PATH
                else:
                    color = self.WALLS if tile.filled else self.BACKGROUND
                pygame.draw.rect(screen, color,
                                 (x, y,
                                  rect_size, rect_size))

                x += self.tile_size
            x = self.OFFSET + self.WALL_SIZE
            y += self.tile_size


if __name__ == "__main__":
    size = int(input("Digite a quantidade de Linhas Colunas que voc quer: "))
    Labyrinth = Labyrinth(screen_size=900, size = size)
    Labyrinth.run()
