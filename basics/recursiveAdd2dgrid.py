import numpy as np


def add_recurive(grid, x=0, y=0):

    if x >= len(grid) or y >= len(grid[0]):
        return 0

    curr = grid[x][y]
    grid2 = np.array(grid)
    grid2[x, y] = "-1"
    print(grid2)
    curr += add_recurive(grid, x, y+1)
    if y+1 == len(grid[0]):
        curr += add_recurive(grid, x+1, 0)
    return curr


if __name__ == '__main__':
    grid_shape = (4, 4)
    grid = np.random.randint(0, 5, size=grid_shape)
    print(grid)
    ans = add_recurive(grid.tolist())
    print(ans)
