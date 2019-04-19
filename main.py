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
                    shellSortNumeroVoo(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 2:
                    print("================= Ordenação por data de partida =================================")
                    inicio = timeit.default_timer()
                    shellSortDia(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 3:
                    print("================= Ordenação por horário de partida =================================")
                    inicio = timeit.default_timer()
                    shellSortHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 4:
                    print("================= Ordenação por pista =================================")
                    inicio = timeit.default_timer()
                    shellSortPista(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 5:
                    print("================= Ordenação por dia e horário =================================")
                    inicio = timeit.default_timer()
                    shellSortDiaHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 6:
                    print("================= Ordenação por dia, horário e pista =================================")
                    inicio = timeit.default_timer()
                    shellSortDiaHorarioPista(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    print("Tempo de execução: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    
                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                    
                elif criterioOrdenacao == 7:
                    print("================= Ordenação por pista, dia e horário =================================")
                    inicio = timeit.default_timer()
                    shellSortPistaDiaHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
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