# alunos:
# Rodrigo Bento de Macedo
# Marcelo da Silva de Oliveira
# Critica feita pelo grupo de estudos Brabos!

# sorteio da palavra
import random


def sortear_palavra():
    arquivo = open("lista_palavras.txt")
    linhas = arquivo.readlines()
    palavra = ''
    while len(palavra) < 4 or len(palavra) > 10:
        sorteio = random.randint(0, len(linhas)) + 1
        palavra = linhas[sorteio]
    palavra = palavra.upper()
    arquivo.close()
    return palavra


# mensagem final
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f"A palavra era {palavra_secreta}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


# desenho da forca
forca = '''
__
    |'''
vazio = '''

'''
cabeca = '''
  (@@)
'''
corpo = '''
  (@@) 
   ||
'''
brc_dir = '''
  (@@)
  /||
'''
brc_esq = '''
  (@@)
  /||\\
'''
pern_dir = '''
  (@@)
  /||\\
  /
'''

palavra = sortear_palavra().strip()
chances = [vazio, cabeca, corpo, brc_dir, brc_esq, pern_dir]

erros = 0
letras_acertadas = ''
letras_erradas = ''
acertos = 0
print(palavra)
while acertos != len(palavra) and erros != 6:
    mensagem = ''
    for letra in palavra:
        if letra in letras_acertadas:
            mensagem = mensagem + letra + ' '
        else:
            mensagem = mensagem + '_ '
    print(mensagem)
    print(forca + chances[erros])
    print(f'Voce tem {+erros} erros!')
    letra = str(input('Digite a letra do seu palpite: ')).upper()
    if len(letra) > 1:
        print('Digite apenas uma letra, sem espaços ou acentoo por palpite!')
    else:
        if letra in palavra:
            qtde = 0
            print('Parabéns você acertou a letra!!!')
            letras_acertadas += letra

            for c in range(len(palavra)):
                if palavra[c] == letra:
                    acertos = acertos + 1

            if acertos == len(palavra):
                print(imprime_mensagem_vencedor())
        else:
            print('Você errou a letra!')
            letras_erradas = letras_erradas + letra
            erros = erros + 1
            if erros == 6:
                print(imprime_mensagem_perdedor(palavra))
