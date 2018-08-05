#!/usr/bin/python
#! coding: utf-8
#
# created by Umbriel
# 2017-09-04
#
# This module generate a maze represented by an n x n matrix
#

from functools import reduce
import numpy as np


class node(object):
    """
    Defines the nodes in the maze. Adjacent nodes can be connected by
    edges to form the wall of the maze.

    The connection is represented by [UP, DOWN, LEFT, RIGHT]
    """

    def __init__(self):
        self.connection = [1, 1, 1, 1]  # all connected initially

    def __str__(self):
        return '%' + reduce(lambda x, y: str(x) + str(y), self.connection)


class maze(object):
    """
    A maze is formed by nodes
    """

    def __init__(self, n_squares=10):
        """
        Prepare the initial state of the maze
        """
        # initialize the maze nodes
        self.maze = []
        self.n_nodes = (n_squares + 1) * (n_squares + 1)
        for _ in range(self.n_nodes):
            self.maze.append(node())
        self.maze = np.reshape(self.maze, (n_squares+1, n_squares+1))
        # Initialize the maze squares, which is basically the dual-lattice of
        # the nodes.
        # Each square is also represented by dim-4 array indicating its
        # connectivity to [UP, DOWN, LEFT, RIGHT] squares
        self.squares = []
        for _ in range(n_squares**2):
            self.squares.append(node())
        self.squares = np.reshape(self.squares, (n_squares, n_squares))


    def _update_squares():
        """
        update the squares based on the information of the nodes
        """
        pass

    def _find_route():
        """
        solve the maze
        """
        pass

    def generate_maze():
        """
        generate the maze
        """
        pass




if __name__ == '__main__':
    ma = maze(3)
    print(ma.maze)
