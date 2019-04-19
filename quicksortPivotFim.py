def quickSortPivotNoFimNumVoo(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].numeroVoo <= listaDecolagens[pivot].numeroVoo:
                flag += 1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]



        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag+1];

        quickSortPivotNoFimNumVoo(listaDecolagens, comeco, flag);
        quickSortPivotNoFimNumVoo(listaDecolagens, flag+2, fim);

def quickSortPivotNoFimDia(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].dia <= listaDecolagens[pivot].dia:
                flag += 1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]



        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag+1];

        quickSortPivotNoFimDia(listaDecolagens, comeco, flag);
        quickSortPivotNoFimDia(listaDecolagens, flag+2, fim);

def quickSortPivotNoFimHora(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].hora <= listaDecolagens[pivot].hora:
                flag += 1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]



        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag+1];

        quickSortPivotNoFimHora(listaDecolagens, comeco, flag);
        quickSortPivotNoFimHora(listaDecolagens, flag+2, fim);

def quickSortPivotNoFimPista(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = fim
        flag = comeco-1
        for i in range(comeco, fim):
            if listaDecolagens[i].pista <= listaDecolagens[pivot].pista:
                flag += 1
                listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]



        listaDecolagens[flag+1], listaDecolagens[fim] = listaDecolagens[fim], listaDecolagens[flag+1];

        quickSortPivotNoFimPista(listaDecolagens, comeco, flag);
        quickSortPivotNoFimPista(listaDecolagens, flag+2, fim);
