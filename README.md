# SMART MAZE Generator

Um gerador de labirintos inteligente que utiliza o algoritmo Aldous-Broder para criar labirintos perfeitos (sem loops e com um único caminho entre quaisquer dois pontos). Este projeto foi desenvolvido por RetroModernProfessor (Professor Filipo).
Essa versão é uma atualização do projeto original, feita em python, com modularização, inclusão de parametros para dimencionamento da matriz e parametros de debug

## Sobre o Projeto

O SMART MAZE é uma aplicação em Python que gera labirintos personalizáveis em tamanho. O programa utiliza o algoritmo Aldous-Broder que garante labirintos perfeitos onde cada célula é acessível a partir de qualquer outra célula por exatamente um caminho único.

Características principais:
- Geração de labirinto com tamanho configurável
- Visualização da construção do labirinto em tempo real
- Representação gráfica do labirinto utilizando caracteres ASCII
- Opções para controlar a velocidade de visualização do processo de geração
- Modularização e inclusão de parâmetros para dimensionamento da matriz e parâmetros de debug

## Dependências

O projeto utiliza apenas bibliotecas padrão do Python:
- `random`: Para seleção aleatória de células
- `os`: Para limpeza de tela
- `time`: Para controle de tempo entre cada etapa da visualização
- `argparse`: Para processamento de argumentos da linha de comando

## Como Executar

### Pré-requisitos
- Python 3.x instalado no sistema

### No Linux

1. Abra um terminal
2. Navegue até a pasta do projeto:
   ```
   cd /caminho/para/maze_generator
   ```
3. Dê permissão de execução ao script (se necessário):
   ```
   chmod +x maze_generator.py
   ```
4. Execute o programa:
   ```
   ./maze_generator.py
   ```

   Ou:
   ```
   python3 maze_generator.py
   ```

### No Windows

1. Abra o Prompt de Comando ou PowerShell
2. Navegue até a pasta do projeto:
   ```
   cd C:\caminho\para\maze_generator
   ```
3. Execute o programa:
   ```
   python maze_generator.py
   ```

### Opções de Linha de Comando

O script suporta as seguintes opções:

- `-s`, `--size`: Define o tamanho da matriz do labirinto (padrão: 5)
  ```
  python maze_generator.py --size 10
  ```

- `-np`, `--no-progress`: Desativa a exibição do progresso durante a geração
  ```
  python maze_generator.py --no-progress
  ```

- `-d`, `--delay`: Define o tempo de espera entre cada passo da geração em segundos (padrão: 0.05s)
  ```
  python maze_generator.py --delay 0.1
  ```

Você pode combinar estas opções:
```
python maze_generator.py --size 15 --delay 0.02
```

## Exemplos de Uso

Para gerar um labirinto padrão 5x5:
```
python maze_generator.py
```

Para gerar um labirinto grande (20x20) sem mostrar o progresso:
```
python maze_generator.py --size 20 --no-progress
```

Para gerar um labirinto 10x10 com visualização lenta do processo:
```
python maze_generator.py --size 10 --delay 0.5
```
