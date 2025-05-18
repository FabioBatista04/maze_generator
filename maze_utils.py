#!/usr/bin/env python3
"""
Módulo com funções utilitárias para o gerador de labirinto
"""

import random
from walls import Walls

def reset_maze(maze, visited, cell_value, n):
    """Função para fazer a limpeza da matriz"""
    for i in range(n):
        for j in range(n):
            maze[i][j] = cell_value
            visited[i][j] = False

def pickup_random_cell(n):
    """Retorna uma célula aleatória do labirinto"""
    return random.randint(0, n-1), random.randint(0, n-1)

def open_wall(maze, line, column, wall, n):
    """Abre uma parede, fazendo o mesmo para suas paredes vizinhas"""
    if (wall & Walls.TOP) == Walls.TOP:
        if line > 0:
            maze[line - 1][column] -= Walls.BOTTOM
            if maze[line - 1][column] < 0:
                maze[line - 1][column] = 0
    
    if (wall & Walls.BOTTOM) == Walls.BOTTOM:
        if line < (n - 1):
            maze[line + 1][column] -= Walls.TOP
            if maze[line + 1][column] < 0:
                maze[line + 1][column] = 0
    
    if (wall & Walls.LEFT) == Walls.LEFT:
        if column > 0:
            maze[line][column - 1] -= Walls.RIGHT
            if maze[line][column - 1] < 0:
                maze[line][column - 1] = 0
    
    if (wall & Walls.RIGHT) == Walls.RIGHT:
        if column < (n - 1):
            maze[line][column + 1] -= Walls.LEFT
            if maze[line][column + 1] < 0:
                maze[line][column + 1] = 0
    
    maze[line][column] -= wall
    if maze[line][column] < 0:
        maze[line][column] = 0

def close_isolated_cells(maze, n):
    """Fecha completamente células que não têm passagem ou que têm menos de duas passagens"""
    # Cria uma matriz copia para armazenar as células a serem fechadas
    cells_to_close = [[False for _ in range(n)] for _ in range(n)]
    
    # Loop 1: Identificar células que precisam ser fechadas
    for i in range(n):
        for j in range(n):
            # Contar o número de passagens abertas da célula
            passages_count = 0
            
            # Verifica parede superior
            if i > 0 and (maze[i][j] & Walls.TOP) == 0:
                passages_count += 1
                
            # Verifica parede inferior
            if i < n-1 and (maze[i][j] & Walls.BOTTOM) == 0:
                passages_count += 1
                
            # Verifica parede esquerda
            if j > 0 and (maze[i][j] & Walls.LEFT) == 0:
                passages_count += 1
                
            # Verifica parede direita
            if j < n-1 and (maze[i][j] & Walls.RIGHT) == 0:
                passages_count += 1
            
            # Marca para fechar se tiver menos de duas passagens
            cells_to_close[i][j] = passages_count < 2
    
    # Loop 2: Fechar as células marcadas
    for i in range(n):
        for j in range(n):
            if cells_to_close[i][j]:
                # Fecha todas as paredes dessa célula
                maze[i][j] = Walls.ALL
                
                # Fecha as paredes correspondentes das células vizinhas
                if i > 0:  # Célula acima
                    maze[i-1][j] |= Walls.BOTTOM
                if i < n-1:  # Célula abaixo
                    maze[i+1][j] |= Walls.TOP
                if j > 0:  # Célula à esquerda
                    maze[i][j-1] |= Walls.RIGHT
                if j < n-1:  # Célula à direita
                    maze[i][j+1] |= Walls.LEFT