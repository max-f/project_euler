#!/usr/bin/env python

import time


class Grid:
    def __init__(self, gridsize):
        self.gridsize = gridsize
        self.matrix= [([0] * gridsize) for x in range(gridsize)]
        # Fill all spots where only one move is possible (down/right)
        for i in range(gridsize):
            self.matrix[i][gridsize - 1] = 1
            self.matrix[gridsize - 1][i] = 1

    def fill(self):
        for i in reversed(range(0, self.gridsize - 1)):
            for j in reversed(range(0, self.gridsize - 1)):
                self.matrix[i][j] = self.matrix[i + 1][j] + self.matrix[i][j + 1]

    def __str__(self):
        s = ''
        for row in self.matrix:
            s = ''.join([s, str(row), '\n'])
        return s


def main():
    """
    Dynamic programming
    """
    gridsize = 21  # For a 20x20 grid, since the borders are important
    g = Grid(gridsize)
    print(g)
    g.fill()
    print(g)
    print('In total {0} possibilities for a {1}x{1} '
          'grid'.format(g.matrix[0][0], gridsize - 1))

if __name__ == '__main__':
    start = time.time()
    main()
    print('Total runtime: %f seconds' % (time.time() - start))
