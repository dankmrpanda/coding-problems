#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'play2248' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING boardValues as parameter.
#

def createGraph(board):
    boardEdges = {}
    for i in range(8):
        for j in range(5):
            loc = (i, j)
            boardEdges[loc] = []
            value1 = board[i][j]
            # check the 8 spaces
            if i != 0:
                # T
                value2 = board[i-1][j]
                if value1 == value2 or value1 * 2 == value2:
                    boardEdges[loc].append((i-1, j))
                # TL
                if j - 1 >= 0:
                    value2 = board[i-1][j-1]
                    if value1 == value2 or value1 * 2 == value2:
                        boardEdges[loc].append((i-1, j-1))
                # TR
                if j + 1 <= 4:
                    value2 = board[i-1][j+1]
                    if value1 == value2 or value1 * 2 == value2:
                        boardEdges[loc].append((i-1, j+1))
            # L
            if j - 1 >= 0:
                value2 = board[i][j-1]
                if value1 == value2 or value1 * 2 == value2:
                    boardEdges[loc].append((i, j-1))
            # R
            if j + 1 <= 4:
                value2 = board[i][j+1]
                if value1 == value2 or value1 * 2 == value2:
                    boardEdges[loc].append((i, j+1))
            if i != 7:
                # B
                value2 = board[i+1][j]
                if value1 == value2 or value1 * 2 == value2:
                    boardEdges[loc].append((i+1, j))
                # BL
                if j - 1 >= 0:
                    value2 = board[i+1][j-1]
                    if value1 == value2 or value1 * 2 == value2:
                        boardEdges[loc].append((i+1, j-1))
                # BR
                if j + 1 <= 4:
                    value2 = board[i+1][j+1]
                    if value1 == value2 or value1 * 2 == value2:
                        boardEdges[loc].append((i+1, j+1))
                
    return boardEdges


def generatePaths(board, graph, currentVertex, visited):
    # for paths
    visitedList = [[]]
    def findNodes(board, graph, currentVertex, visited):
        # make sure the first 2 numbers are the same
        if len(visited) == 1:
            a, b = currentVertex
            c, d = visited[0]
            if board[a][b] != board[c][d]:
                return []
        # mark node as visited
        visited.append(currentVertex)
        for vertex in graph[currentVertex]:
            # recursively find nodes :(
            if vertex not in visited:
                findNodes(board, graph, vertex, visited.copy())
        # we are done visiting this node
        visitedList.append(visited)
        return visitedList
    return [i for i in findNodes(board, graph, currentVertex, visited)[1:] if len(i) > 1]


def round(boardValues):
    # Create board.
    boardValues = boardValues.split(" ")
    board = []
    for i in range(8):
        row = []
        for j in range(5):
            row.append(int(boardValues[i*5+j]))
        board.append(row)

    # Create graph to help with longest path.
    boardEdges = createGraph(board)

    # for _, key in enumerate(boardEdges):
    #     print(key, boardEdges[key])

    # Find all paths. Also find highest power of 2 cuz why not.
    highestPowerOf2 = 1
    allPaths = []
    for i in range(8):
        for j in range(5):
            if board[i][j] > highestPowerOf2:
                highestPowerOf2 = board[i][j]
            for path in generatePaths(board, boardEdges, (i,j), []):
                allPaths.append(path)

    # Find path to be used (longest, and sorted first in alphabetical order).
    maxPathLength = max(len(path) for path in allPaths)
    allPaths = [path for path in allPaths if len(path) == maxPathLength]
    chosenPath = sorted([str(path) for path in allPaths])[0]
    chosenPath = eval(chosenPath)

    # Remove tiles in path. Also get their sum.
    s = 0
    for coordinate in chosenPath:
        a, b = coordinate
        s += board[a][b]
        board[a][b] = None

    # Replace that one last tile with the power of 2.
    replacement = 2
    while replacement < s:
        replacement *= 2
    board[a][b] = replacement
    
    # Remove lower power of 2s, if applicable.
    # First find the new range of possible powers.
    if replacement > highestPowerOf2:
        highestPowerOf2 = replacement
    if highestPowerOf2 < 2 ** 8:
        highestPowerOf2 = 2 ** 8
    eligiblePowers = []
    for i in range(8):
        eligiblePowers.append(int(highestPowerOf2))
        highestPowerOf2 /= 2
    # Now, iterate through the graph and eliminate.
    for i in range(8):
        for j in range(5):
            if board[i][j] not in eligiblePowers:
                board[i][j] = None

    # for row in board:
    #     print(row)
    # print()

    # Move tiles down.
    # for each number starting from the BL to TR:
    for i in range(6, -1, -1):
        for j in range(5):
            # if it is a number, check if there is a none below it
            if board[i][j] is not None:
                for k in range(7, i, -1):
                    # if it does, fill it
                    if board[k][j] == None:
                        board[k][j] = board[i][j]
                        board[i][j] = None
                        break

    # Fill empty tiles in row-major order.
    num = 0
    for i in range(8):
        for j in range(5):
            if board[i][j] == None:
                board[i][j] = eligiblePowers[num]
                num = (num+1) % 8
    
    # for row in board:
    #     print(row)
    # print()
    
    ans = ""
    for row in board:
        for num in row:
            ans += str(num) + " "

    return ans.strip() 

def play2248(boardValues):
    # Repeat 3 rounds.
    for i in range(3):
        boardValues = round(boardValues)
    return boardValues    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # boardValues = input()

    boardValues = "4 128 4 128 32 16 16 4 256 16 32 4 16 64 4 8 64 64 256 8 16 2 2 256 4 32 128 2 64 8 256 32 128 16 2 8 32 32 4 32"
    
    result = play2248(boardValues)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
