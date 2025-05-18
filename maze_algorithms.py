#!/usr/bin/env python3
"""
Módulo com algoritmos de geração de labirintos
"""

import time
import random
from walls import Walls
from maze_utils import reset_maze, pickup_random_cell, open_wall
from maze_display import show_maze_details, show_maze_values

def aldous_broder_maze(maze, n, show_progress=True, delay=0.05):
    """Implementa o algoritmo Aldous-Broder para geração de labirintos"""
    visited = [[False for _ in range(n)] for _ in range(n)]
    unvisited_cells = n * n
    
    # Inicializa o labirinto com todas as paredes
    reset_maze(maze, visited, Walls.TOP + Walls.BOTTOM + Walls.LEFT + Walls.RIGHT, n)
    
    # Escolhe uma célula inicial aleatória
    current_cell_line, current_cell_column = pickup_random_cell(n)
    visited[current_cell_line][current_cell_column] = True
    unvisited_cells -= 1
    
    cont = 0
    
    while unvisited_cells > 0:
        # Escolhe um vizinho aleatório da célula atual
        found = False
        while not found:
            # 0: UP, 1: DOWN, 2: LEFT, 3: RIGHT
            guess = random.randint(0, 3)
            
            if guess == 0:  # TOP
                if current_cell_line > 0:
                    neigh_cell_line = current_cell_line - 1
                    neigh_cell_column = current_cell_column
                    wall = Walls.TOP
                    found = True
            elif guess == 1:  # DOWN
                if current_cell_line < (n - 1):
                    neigh_cell_line = current_cell_line + 1
                    neigh_cell_column = current_cell_column
                    wall = Walls.BOTTOM
                    found = True
            elif guess == 2:  # LEFT
                if current_cell_column > 0:
                    neigh_cell_line = current_cell_line
                    neigh_cell_column = current_cell_column - 1
                    wall = Walls.LEFT
                    found = True
            elif guess == 3:  # RIGHT
                if current_cell_column < (n - 1):
                    neigh_cell_line = current_cell_line
                    neigh_cell_column = current_cell_column + 1
                    wall = Walls.RIGHT
                    found = True
        
        if not visited[neigh_cell_line][neigh_cell_column]:
            open_wall(maze, current_cell_line, current_cell_column, wall, n)
            visited[neigh_cell_line][neigh_cell_column] = True
            unvisited_cells -= 1
        
        # Depuração
        if show_progress:
            show_maze_details(maze, visited, current_cell_line, current_cell_column, n)
            show_maze_values(maze, n)
            cont += 1
            print(f"\ncont: {cont}")
            print(f"unvisited cells: {unvisited_cells}")
            print(f"wall: {wall}")
            print(f"neighCellLine:   {neigh_cell_line:2d} ::: \tcurrentCellLine:   {current_cell_line:2d}")
            print(f"neighCellColumn: {neigh_cell_column:2d} ::: \tcurrentCellColumn: {current_cell_column:2d}\n")
            time.sleep(delay)  # pausa configurável
        
        current_cell_line = neigh_cell_line
        current_cell_column = neigh_cell_column