#!/usr/bin/python
#! coding: utf-8
#
# created by Umbriel
# 2017-09-04
#
# This module generate a maze represented by an n x m matrix
#

import numpy as np
import maze_visualization as mv

def maze_generator(n, m):
    '''
    input: 
        n: the number of rows of the maze
        m: the number of columns of the maze
    output: an np matrix that represent the connectivity
    '''
    # initialize the maze
    maze = np.ones([n+2, m+2]) 
    maze[:, m+1] = 2
    maze[:, 0] = 2
    maze[0, :] = 2
    maze[n+1, :] = 2
    maze[1][1] = 0
    maze[n][m] = 0

    # step 1: generate the path

if __name__ == '__main__':
    print 'hello'