import os
import sys
# import time
import timeit
from funcoes import *
from quicksortPivotFim import *
from quicksortPivotAleatorio import *
from quicksortPivotComeco import *

def main():
    sys.setrecursionlimit(1000000) #Permite realizar mais chamadas recursivas do que o normal
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
                    tempoShellSort = fim - inicio
                    print("Tempo de execução do Shell Sort: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortNumeroVoo(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    sorted(listaDecolagens, key=lambda decolagem: decolagem.numeroVoo)
                    fim = timeit.default_timer()
                    tempoTimSort = fim - inicio
                    print("Tim sort realizado! ")
                    # imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    print("Tempo de execução do Tim Sort: {:.6f}s".format (tempoTimSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimNumVoo(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoNumVoo(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioNumVoo(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    
                    f = open("historico.txt", "a")
                    f.write("Número do vôo\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "{:.6f}".format (tempoTimSort) + "\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 2:
                    print("================= Ordenação por data de partida =================================")
                    inicio = timeit.default_timer()
                    shellSortDia(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    tempoShellSort = fim - inicio
                    print("Tempo de execução: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortDia(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    sorted(listaDecolagens, key=lambda decolagem: decolagem.dia)
                    fim = timeit.default_timer()
                    tempoTimSort = fim - inicio
                    print("Tim sort realizado! ")
                    # imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    print("Tempo de execução do Tim Sort: {:.6f}s".format (tempoTimSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimDia(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoDia(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioDia(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    f = open("historico.txt", "a")
                    f.write("Data\t\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "{:.6f}".format (tempoTimSort) + "\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                elif criterioOrdenacao == 3:
                    print("================= Ordenação por horário de partida =================================")
                    inicio = timeit.default_timer()
                    shellSortHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    tempoShellSort = fim - inicio
                    print("Tempo de execução: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortHorario(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    sorted(listaDecolagens, key=lambda decolagem: decolagem.hora)
                    fim = timeit.default_timer()
                    tempoTimSort = fim - inicio
                    print("Tim sort realizado! ")
                    # imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    print("Tempo de execução do Tim Sort: {:.6f}s".format (tempoTimSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    f = open("historico.txt", "a")
                    f.write("Horário\t\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "{:.6f}".format (tempoTimSort) + "\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 4:
                    print("================= Ordenação por pista =================================")
                    inicio = timeit.default_timer()
                    shellSortPista(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    tempoShellSort = fim - inicio
                    print("Tempo de execução: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortPista(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    sorted(listaDecolagens, key=lambda decolagem: decolagem.pista)
                    fim = timeit.default_timer()
                    tempoTimSort = fim - inicio
                    print("Tim sort realizado! ")
                    # imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    print("Tempo de execução do Tim Sort: {:.6f}s".format (tempoTimSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    f = open("historico.txt", "a")
                    f.write("Pista\t\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "{:.6f}".format (tempoTimSort) + "\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 5:
                    print("================= Ordenação por dia e horário =================================")
                    inicio = timeit.default_timer()
                    shellSortDiaHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    tempoShellSort = fim - inicio
                    print("Tempo de execução: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortDiaHorario(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    f = open("historico.txt", "a")
                    f.write("Dia, Horário\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "--\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 6:
                    print("================= Ordenação por dia, horário e pista =================================")
                    inicio = timeit.default_timer()
                    shellSortDiaHorarioPista(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    tempoShellSort = fim - inicio
                    print("Tempo de execução: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortDiaHorarioPista(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimDiaHoraPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoDiaHoraPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioDiaHoraPista(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    f = open("historico.txt", "a")
                    f.write("Dia|Hora|Pista\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "--\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)

                elif criterioOrdenacao == 7:
                    print("================= Ordenação por pista, dia e horário =================================")
                    inicio = timeit.default_timer()
                    shellSortPistaDiaHorario(listaDecolagens, len(listaDecolagens))
                    fim = timeit.default_timer()
                    tempoShellSort = fim - inicio
                    print("Tempo de execução: {:.6f}s".format (tempoShellSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    dadosMerge = mergeSortPistaDiaHorario(listaDecolagens)
                    fim = timeit.default_timer()
                    tempoMergeSort = fim - inicio
                    print("Merge sort realizado! ")
                    # print("Quantidade de comparações: ", dadosMergeNumeroVoo[0])
                    # print("Quantidade de movimentos até formar o vetor ordenado: ", dadosMergeNumeroVoo[1])
                    print("Tempo de execução do Merge Sort: {:.6f}s".format (tempoMergeSort))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoFimPistaDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoFim = fim - inicio
                    print("Quick Sort realizado! ")
                    print("Tempo de execução do Quick Sort com Pivot no fim: {:.6f}s".format (tempoQuickSortPivoFim))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotNoComecoPistaDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoComeco = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot no comeco: {:.6f}s".format (tempoQuickSortPivoComeco))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    inicio = timeit.default_timer()
                    quickSortPivotAleatorioPistaDiaHora(listaDecolagens, 0, numeroDecolagens-1)
                    fim = timeit.default_timer()
                    tempoQuickSortPivoAleatorio = fim - inicio
                    print("Tempo de execução do Quick Sort com Pivot aleatorio: {:.6f}s".format (tempoQuickSortPivoAleatorio))
                    input("\n\nAperte QUALQUER tecla para continuar\n")

                    f = open("historico.txt", "a")
                    f.write("Pista|Dia|Hora\t" + str(len(listaDecolagens)) + "\t"+ \
                            "{:.6f}".format (tempoShellSort) + "\t" + \
                            "{:.6f}".format (tempoMergeSort) + "\t" + \
                            "--\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoComeco) +"\t\t\t"+ \
                            "{:.6f}".format (tempoQuickSortPivoFim) + "\t\t\t" + \
                            "{:.6f}".format (tempoQuickSortPivoAleatorio) + "\n")

                    imprimeListaVoos(len(listaDecolagens), listaDecolagens)
                    gerenciaVoosAdicionais(listaDecolagens)
                else:
                    f.close()
                    print("Histórico")
                    print("Critério\tTamanho\tTempo Shell\tTempo Merge\tTempo TimSort\tTempo Quick Sort Pivo no Começo\tTempo Quick Sort Pivo no Fim\tTempo Quick Sort Pivo Aleatorio")
                    f = open("historico.txt","r")
                    print(f.read())
                    input("\n\nAperte QUALQUER tecla para continuar\n")
                    f.close()
                    break

        else:
            system("clear")
            print("Encerrando programa")
            break


main()
