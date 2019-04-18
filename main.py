import os
# import time
from funcoes import *

def main():
    darBoasVindas()
    input("\n\nAperte QUALQUER tecla para continuar")
    system("clear")
    while True:
        system("clear")
        exibirMenu()
        opcao = recebeOpcaoMenuValida()
        if opcao == 1: 
            numeroDecolagens = escolheNumeroDecolagens()
            listaDecolagens = gerarDecolagens(numeroDecolagens)
            imprimeListaVoos(numeroDecolagens, listaDecolagens)
            while True:
                exibirMenuOrdenacao()
                criterioOrdenacao = recebeOpcaoMenuOrdenacaoValida()
                if criterioOrdenacao == 1:
                    print("Ordenar por numero do voo")
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 2:
                    print("Ordenar por dia")
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 3:
                    print("Ordenar por horario")
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 4:
                    print("Ordenar por pista")
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 5:
                    print("Ordenar por dia e horario")
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 6:
                    print("Ordenar por dia, horario e pista")
                    gerenciaVoosAdicionais(listaDecolagens)
                else:
                    break
            
        else:
            system("clear")
            print("Encerrando programa")
            break


main()