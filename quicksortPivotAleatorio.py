import random

def quickSortPivotAleatorioNumVoo(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = random.randint(comeco, fim)
        listaDecolagens[pivot], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[pivot]
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].numeroVoo < listaDecolagens[pivot].numeroVoo:

                flag+=1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag + 1];

        quickSortPivotAleatorioNumVoo(listaDecolagens, comeco, flag);
        quickSortPivotAleatorioNumVoo(listaDecolagens, flag+2, fim);

def quickSortPivotAleatorioDia(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = random.randint(comeco, fim)
        listaDecolagens[pivot], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[pivot]
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].dia < listaDecolagens[pivot].dia:

                flag+=1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag + 1];

        quickSortPivotAleatorioDia(listaDecolagens, comeco, flag);
        quickSortPivotAleatorioDia(listaDecolagens, flag+2, fim);

def quickSortPivotAleatorioHora(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = random.randint(comeco, fim)
        listaDecolagens[pivot], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[pivot]
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if str(listaDecolagens[i].hora) < str(listaDecolagens[pivot].hora):

                flag+=1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag + 1];

        quickSortPivotAleatorioHora(listaDecolagens, comeco, flag);
        quickSortPivotAleatorioHora(listaDecolagens, flag+2, fim);

def quickSortPivotAleatorioPista(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = random.randint(comeco, fim)
        listaDecolagens[pivot], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[pivot]
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].pista < listaDecolagens[pivot].pista:

                flag+=1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag + 1];

        quickSortPivotAleatorioPista(listaDecolagens, comeco, flag);
        quickSortPivotAleatorioPista(listaDecolagens, flag+2, fim);
