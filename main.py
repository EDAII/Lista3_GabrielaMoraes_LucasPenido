import os
# import time
import timeit
from funcoes import *
from quicksortPivotFim import *
from quicksortPivotAleatorio import *
from quicksortPivotComeco import *

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
                    print("Tempo de execução do Shell Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortNumeroVoo(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimNumVoo(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoNumVoo(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioNumVoo(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortDia(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimDia(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoDia(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioDia(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortHorario(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortPista(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortDiaHorario(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortDiaHorarioPista(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimDiaHoraPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoDiaHoraPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioDiaHoraPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortPistaDiaHorario(listaDecolagens)
                    fim = timeit.default_timer()
                    print("Merge sort realizado! ")
                    print("Quantidade de comparações: ", dadosMerge[0])
                    print("Quantidade de swaps: ", dadosMerge[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (fim-inicio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimPistaDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoPistaDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (fim-inicio))

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioPistaDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (fim-inicio))
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
