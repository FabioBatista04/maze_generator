#!/usr/bin/env python3
"""
S M A R T   M A Z E
Versão 2 - Permite a seleção do tamanho da matriz para o labirinto.
Implementando o algoritmo de labirinto Aldous-Broder.
by the RetroModernProfessor (Professor Filipo) - filipomor.com
Versão Python
"""

import random
import argparse

# Importações dos módulos criados
from walls import Walls
from maze_utils import close_isolated_cells
from maze_display import show_maze, show_maze_values
from maze_algorithms import aldous_broder_maze

def parse_arguments():
    """Configura os argumentos de linha de comando"""
    parser = argparse.ArgumentParser(description='Gerador de Labirintos Smart Maze 2.0')
    parser.add_argument('-s', '--size', type=int, default=5, 
                        help='Tamanho da matriz do labirinto (padrão: 5)')
    parser.add_argument('-np', '--no-progress', action='store_true',
                        help='Desativa a exibição do progresso durante a geração')
    parser.add_argument('-d', '--delay', type=float, default=0.05,
                        help='Tempo de espera entre cada passo da geração (padrão: 0.05s)')
    return parser.parse_args()

def main():
    # Parse argumentos da linha de comando
    args = parse_arguments()
    
    # Tamanho da matriz do labirinto (valor padrão ou definido pelo usuário)
    n = args.size
    show_progress = not args.no_progress
    delay = args.delay
    
    print(f"Gerando labirinto de {n}x{n}...")
    
    # Inicializa a matriz do labirinto
    maze = [[0 for _ in range(n)] for _ in range(n)]
    
    # Configura a semente aleatória
    random.seed()
    
    # Gera o labirinto usando o algoritmo Aldous-Broder
    aldous_broder_maze(maze, n, show_progress, delay)
    
    # Fecha células isoladas sem passagem
    close_isolated_cells(maze, n)
    
    # Mostra o resultado final
    print("\nLabirinto Finalizado:")
    show_maze_values(maze, n)
    print("\nRepresentação gráfica do labirinto:")
    show_maze(maze, n)

if __name__ == "__main__":
    main()