import os
# import time
import timeit
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
            listaDecolagens = []
            listaDecolagens = gerarDecolagens(listaDecolagens, numeroDecolagens)
            imprimeListaVoos(numeroDecolagens, listaDecolagens)
            while True:
                exibirMenuOrdenacao()
                criterioOrdenacao = recebeOpcaoMenuOrdenacaoValida()
                if criterioOrdenacao == 1:
                    print("================= Ordenação por Número do Vôo =================================")
                    inicio = timeit.default_timer()
                    qtdSwaps = shellSortNumeroVoo(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Shell sort realizado! ")
                    print("Quantidade de swaps: ", qtdSwaps)
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 2:
                    print("================= Ordenação por data de partida =================================")
                    inicio = timeit.default_timer()
                    qtdSwaps = shellSortDia(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Shell sort realizado! ")
                    print("Quantidade de swaps: ", qtdSwaps)
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 3:
                    print("================= Ordenação por horário de partida =================================")
                    inicio = timeit.default_timer()
                    qtdSwaps = shellSortHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Shell sort realizado! ")
                    print("Quantidade de swaps: ", qtdSwaps)
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 4:
                    print("================= Ordenação por pista =================================")
                    inicio = timeit.default_timer()
                    qtdSwaps = shellSortPista(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Shell sort realizado! ")
                    print("Quantidade de swaps: ", qtdSwaps)
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 5:
                    print("================= Ordenação por dia e horário =================================")
                    inicio = timeit.default_timer()
                    qtdSwaps = shellSortDiaHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Shell sort realizado! ")
                    print("Quantidade de swaps: ", qtdSwaps)
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 6:
                    print("================= Ordenação por dia, horário e pista =================================")
                    inicio = timeit.default_timer()
                    qtdSwaps = shellSortDiaHorarioPista(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Shell sort realizado! ")
                    print("Quantidade de swaps: ", qtdSwaps)
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                else:
                    break
            
        else:
            system("clear")
            print("Encerrando programa")
            break


main()