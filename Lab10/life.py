#
# life.py - Game of Life lab
#
# Name: Marc Sulsenti   
# Pledge: I pledge my honor that I have abided by the Stevens Honor System
#

import random
import sys

#random variable


def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    '''Returns a 2d array with "height" rows and wdith "cols" '''
    board = []
    for row in range(height):
        board += [createOneRow(width)]
    return board

def printBoard(A):
    '''This function prints the 2d list of lists without spaces'''
    for row in A:
        for col in row:
            sys.stdout.write((str(col)))
        sys.stdout.write('\n')

def diagonalize(width,height): 
    """ creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height ) 
     
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      
 
    return A

def innerCells(width,height):
    '''This function creates an array of all live cells except for a one cell wide
border of empty cells around the edge of the 2d array'''
    A = createBoard(width,height)
    for row in range(height):
        for col in range(width):
            if (col != 0 and col != width-1) and (row != 0 and row != height-1) :
                A[row][col] = 1
    return A

def randomCells(width,height):
    '''Returns an array of rnadomly assigned 1s and 0s except that the outer edge
of the erray is still completely empty (all 0s) ex. see inner cells'''
    A = createBoard(width,height)
    for row in range(height):
        for col in range(width):
            if (col != 0 and col != width-1) and (row != 0 and row != height-1) :
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    '''This function creates a deep copy of the inputted list
does not use impot copy'''
    copy = []
    for row in range(len(A)):
        newRow = []
        for col in range(len(A[row])):
            newRow = newRow  + [A[row][col]]
        copy = copy  + [newRow]
    return copy

def innerReverse(A):
    '''This function creates a reversed 2d array of the input array'''
    copied = copy(A)
    width = len(copied[0])
    height = len(copied)
    for row in range(h):
        for col in range(w):
            #establishes the boundry
            if  (row == 0 or row == h-1) or (col == 0 or col == w-1):
                copied[row][col] = 0
            #1s become 0s
            elif copied[row][col] == 1:
                copied[row][col] = 0
            #0s become 1s
            else:
                copied[row][col] = 1
    return copied #returns copied that is inner reversed, not to be confused with a copied array

def findNeighbors(A,r,c):
    '''This function finds the neighbors of a given cell at r,c (row,col)
    in the given 2d array A'''
    neighbors = 0
    for row in range(r-1, r+2):
        for col in range(c-1, c+2):
            if not(row == r and col == c) and A[row][col] == 1:
                neighbors += 1
    return neighbors

def next_life_generation(A): 
    """ makes a copy of A and then advanced one 
        generation of Conway's game of life within 
        the *inner cells* of that copy. 
        The outer edge always stays 0.

        utilzies findNeighbors function
        follows game of life rules
    """
    copyA = copy(A)
    width = len(copyA[0])
    height = len(copyA)
    for row in range(height):
        for col in range(width):
            if  (row == 0 or row == height-1) or (col == 0 or col == width-1):
                #establishes border
                copyA[row][col] = 0
            elif findNeighbors(A, row, col) < 2:
                #cell with fewer than two neighbors dies
                copyA[row][col] = 0
            elif findNeighbors(A, row, col) > 3:
                #Cell with more than 3 neighbors dies
                copyA[row][col] = 0
            elif findNeighbors(A, row, col) == 3 and copyA[row][col] == 0:
                #Cell with 3 neighbors exactly comes to life
                copyA[row][col] = 1
            else:
                copyA[row][col]=A[row][col]
    return copyA


    


