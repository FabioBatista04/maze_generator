#!/usr/bin/env python3
"""
Módulo com funções de visualização do labirinto
"""

import os
from walls import Walls

def show_maze_values(maze, n):
    """Função para mostrar os valores e depurar a matriz"""
    # Para fins de teste apenas
    for i in range(n):
        for j in range(n):
            print(f" {maze[i][j]:2d} ", end="")
        print()

def show_maze(maze, n):
    """Preenchimento gráfico da matriz superior, laterais e inferior"""
    for i in range(n):
        # ##### TOP #####
        for j in range(n):
            # Topo (primeira linha apenas)
            if i == 0:
                if (maze[i][j] & Walls.TOP) == Walls.TOP:
                    print("+----", end="")
                else:
                    print("+    ", end="")
                if j == (n - 1):
                    print("+", end="")
            
            # Topo (segunda linha em diante)
            if i > 0:
                if ((maze[i-1][j] & Walls.BOTTOM) == Walls.BOTTOM or 
                    (maze[i][j] & Walls.TOP) == Walls.TOP):
                    print("+----", end="")
                else:
                    print("+    ", end="")
                if j == (n - 1):
                    print("+", end="")
        print()
        # FIM TOP

        # #### Ambos os lados ####
        for j in range(n):
            L = ' '
            R = ' '

            # ESQUERDA e DIREITA para a primeira coluna apenas
            if j == 0:
                if (maze[i][j] & Walls.LEFT) == Walls.LEFT:
                    L = '|'
                if (maze[i][j] & Walls.RIGHT) == Walls.RIGHT:
                    R = '|'
                print(f"{L}    {R}", end="")

            # ESQUERDA e DIREITA para a última coluna apenas
            L = ' '
            R = ' '
            if j == (n - 1):
                if (maze[i][j] & Walls.LEFT) == Walls.LEFT:
                    L = '|'
                if (maze[i][j] & Walls.RIGHT) == Walls.RIGHT:
                    R = '|'
                if (maze[i][j-1] & Walls.RIGHT) == Walls.RIGHT:
                    L = ' '
                print(f"{L}   {R}", end="")

            # ESQUERDA e DIREITA para as colunas intermediárias apenas
            L = ' '
            R = ' '
            if j > 0 and j < (n - 1):
                # Verificar as paredes entre duas colunas intermediárias
                if ((maze[i][j] & Walls.RIGHT) == Walls.RIGHT or 
                    (maze[i][j+1] & Walls.LEFT) == Walls.LEFT):
                    L = '|'
                print(f"    {L}", end="")
        print()
        # Fim ambos os lados

        # #### INFERIOR - última linha apenas ####
        if i == (n - 1):
            for j in range(n):
                if (maze[i][j] & Walls.BOTTOM) == Walls.BOTTOM:
                    print("+----", end="")
                else:
                    print("+    ", end="")
                if j == (n - 1):
                    print("+", end="")
            print()

def show_maze_details(maze, visited, curr_cell_line, curr_cell_column, n):
    """Mostra o labirinto com detalhes de célula atual e não visitadas"""
    # Limpar tela
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for i in range(n):
        # ##### TOP #####
        for j in range(n):
            # Topo (primeira linha apenas)
            if i == 0:
                if (maze[i][j] & Walls.TOP) == Walls.TOP:
                    print("+---", end="")
                else:
                    print("+   ", end="")
                if j == (n - 1):
                    print("+", end="")
            
            # Topo (segunda linha em diante)
            if i > 0:
                if ((maze[i-1][j] & Walls.BOTTOM) == Walls.BOTTOM or 
                    (maze[i][j] & Walls.TOP) == Walls.TOP):
                    print("+---", end="")
                else:
                    print("+   ", end="")
                if j == (n - 1):
                    print("+", end="")
        print()
        # FIM TOP

        # #### Ambos os lados ####
        for j in range(n):
            L = ' '
            R = ' '


            # Conteúdo da célula
            C = ' '
            if not visited[i][j]:
                C = '*'
            if i == curr_cell_line and j == curr_cell_column:
                C = 'C'

            # ESQUERDA e DIREITA para a primeira coluna apenas
            if j == 0:
                if (maze[i][j] & Walls.LEFT) == Walls.LEFT:
                    L = '|'
                if (maze[i][j] & Walls.RIGHT) == Walls.RIGHT:
                    R = '|'
                print(f"{L} {C} {R}", end="")

            # ESQUERDA e DIREITA para a última coluna apenas
            L = ' '
            R = ' '
            if j == (n - 1):
                if (maze[i][j] & Walls.LEFT) == Walls.LEFT:
                    L = '|'
                if (maze[i][j] & Walls.RIGHT) == Walls.RIGHT:
                    R = '|'
                if (maze[i][j-1] & Walls.RIGHT) == Walls.RIGHT:
                    L = ' '
                print(f"{L} {C} {R}", end="")

            # ESQUERDA e DIREITA para as colunas intermediárias apenas
            L = ' '
            R = ' '
            if j > 0 and j < (n - 1):
                # Verificar as paredes entre duas colunas intermediárias
                if ((maze[i][j] & Walls.RIGHT) == Walls.RIGHT or 
                    (maze[i][j+1] & Walls.LEFT) == Walls.LEFT):
                    L = '|'
                print(f" {C} {L}", end="")
        print()
        # Fim ambos os lados

        # #### INFERIOR - última linha apenas ####
        if i == (n - 1):
            for j in range(n):
                if (maze[i][j] & Walls.BOTTOM) == Walls.BOTTOM:
                    print("+---", end="")
                else:
                    print("+   ", end="")
                if j == (n - 1):
                    print("+", end="")
            print()