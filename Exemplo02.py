# Jogo da velha em python

# Definir o tabuleiro como uma lista de 9 espaços vazios
tabuleiro = [" " for i in range(9)]

# Definir as possíveis combinações de vitória como uma lista de listas
vitorias = [[0, 1, 2], [3, 4, 5], [6, 7, 8], # linhas horizontais
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # linhas verticais
            [0, 4, 8], [2, 4, 6]] # diagonais

# Definir uma função para imprimir o tabuleiro na tela
def imprimir_tabuleiro():
    print(tabuleiro[0] + "|" + tabuleiro[1] + "|" + tabuleiro[2])
    print("-+-+-")
    print(tabuleiro[3] + "|" + tabuleiro[4] + "|" + tabuleiro[5])
    print("-+-+-")
    print(tabuleiro[6] + "|" + tabuleiro[7] + "|" + tabuleiro[8])
    print()

# Definir uma função para verificar se o tabuleiro está cheio
def tabuleiro_cheio():
    return " " not in tabuleiro

# Definir uma função para verificar se um jogador ganhou o jogo
def ganhou(jogador):
    # Para cada combinação de vitória
    for v in vitorias:
        # Se os três espaços correspondem ao símbolo do jogador
        if tabuleiro[v[0]] == tabuleiro[v[1]] == tabuleiro[v[2]] == jogador:
            # Retornar verdadeiro
            return True
    # Se nenhuma combinação de vitória foi encontrada, retornar falso
    return False

# Definir uma função para obter a jogada do jogador humano
def jogada_humano():
    # Pedir ao jogador para digitar um número de 1 a 9
    jogada = input("Digite um número de 1 a 9: ")
    # Enquanto a jogada não for válida
    while not jogada_valida(jogada):
        # Pedir novamente ao jogador para digitar um número de 1 a 9
        jogada = input("Digite um número de 1 a 9: ")
    # Retornar a jogada convertida em um índice de 0 a 8
    return int(jogada) - 1

# Definir uma função para verificar se uma jogada é válida
def jogada_valida(jogada):
    # Se a jogada não for um número de 1 a 9
    if not jogada.isdigit() or int(jogada) < 1 or int(jogada) > 9:
        # Retornar falso
        return False
    # Se o espaço correspondente no tabuleiro não estiver vazio
    if tabuleiro[int(jogada) - 1] != " ":
        # Retornar falso
        return False
    # Se nenhuma das condições anteriores for verdadeira, retornar verdadeiro
    return True

# Definir uma função para obter a jogada do jogador computador
def jogada_computador():
    # Importar o módulo random
    import random
    # Gerar uma lista de índices dos espaços vazios no tabuleiro
    espacos_vazios = [i for i in range(9) if tabuleiro[i] == " "]
    # Escolher um índice aleatório da lista de espaços vazios
    jogada = random.choice(espacos_vazios)
    # Retornar a jogada
    return jogada

# Definir uma função para alternar o jogador da vez
def trocar_jogador(jogador):
    # Se o jogador for "X"
    if jogador == "X":
        # Retornar "Y"
        return "Y"
    # Se o jogador for "Y"
    if jogador == "Y":
        # Retornar "X"
        return "X"

# Definir o jogador inicial como "X"
jogador = "X"

# Enquanto o jogo não terminar
while not tabuleiro_cheio() and not ganhou("X") and not ganhou("Y"):
    # Imprimir o tabuleiro na tela
    imprimir_tabuleiro()
    # Se o jogador for "X"
    if jogador == "X":
        # Obter a jogada do jogador humano
        jogada = jogada_humano()
    # Se o jogador for "Y"
    if jogador == "Y":
        # Obter a jogada do jogador computador
        jogada = jogada_computador()
    # Marcar o espaço correspondente no tabuleiro com o símbolo do jogador
    tabuleiro[jogada] = jogador
    # Alternar o jogador da vez
    jogador = trocar_jogador(jogador)

# Imprimir o tabuleiro final na tela
imprimir_tabuleiro()

# Se o jogador "X" ganhou o jogo
if ganhou("X"):
    # Imprimir uma mensagem de parabéns
    print("Parabéns pela roubada, você ganhou!")
# Se o jogador "Y" ganhou o jogo
if ganhou("Y"):
    # Imprimir uma mensagem de derrota
    print("Você perdeu otário!")
# Se o tabuleiro ficou cheio e ninguém ganhou o jogo
if tabuleiro_cheio() and not ganhou("X") and not ganhou("O"):
    # Imprimir uma mensagem de empate
    print("Deu Velha!")