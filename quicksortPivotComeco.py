def quickSortPivotNoComecoNumVoo(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if listaDecolagens[i].numeroVoo < listaDecolagens[pivot].numeroVoo:
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoNumVoo(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoNumVoo(listaDecolagens, flag, fim);

def quickSortPivotNoComecoDia(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if listaDecolagens[i].dia < listaDecolagens[pivot].dia:
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoDia(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoDia(listaDecolagens, flag, fim);

def quickSortPivotNoComecoHora(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if str(listaDecolagens[i].hora) < str(listaDecolagens[pivot].hora):
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoHora(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoHora(listaDecolagens, flag, fim);

def quickSortPivotNoComecoPista(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if listaDecolagens[i].pista < listaDecolagens[pivot].pista:
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoPista(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoPista(listaDecolagens, flag, fim);

def quickSortPivotNoComecoDiaHora(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if listaDecolagens[i].dia < listaDecolagens[pivot].dia or \
            listaDecolagens[i].dia == listaDecolagens[pivot].dia and str(listaDecolagens[i].hora) < str(listaDecolagens[pivot].hora):
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoDiaHora(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoDiaHora(listaDecolagens, flag, fim);

def quickSortPivotNoComecoDiaHoraPista(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if listaDecolagens[i].dia < listaDecolagens[pivot].dia or \
            listaDecolagens[i].dia == listaDecolagens[pivot].dia and str(listaDecolagens[i].hora) < str(listaDecolagens[pivot].hora) or \
            listaDecolagens[i].dia == listaDecolagens[pivot].dia and str(listaDecolagens[i].hora) == str(listaDecolagens[pivot].hora) and listaDecolagens[i].pista < listaDecolagens[pivot].pista:
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoDiaHoraPista(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoDiaHoraPista(listaDecolagens, flag, fim);

def quickSortPivotNoComecoPistaDiaHora(listaDecolagens, comeco, fim):
    if comeco < fim:
        pivot = comeco
        flag = comeco+1
        for i in range(comeco+1, fim+1):
            if listaDecolagens[i].pista < listaDecolagens[pivot].pista or \
            listaDecolagens[i].pista == listaDecolagens[pivot].pista and listaDecolagens[i].dia < listaDecolagens[pivot].dia or \
            listaDecolagens[i].pista == listaDecolagens[pivot].pista and listaDecolagens[i].dia == listaDecolagens[pivot].dia and str(listaDecolagens[i].hora) == str(listaDecolagens[pivot].hora):
                if i != flag:
                    listaDecolagens[flag], listaDecolagens[i] = listaDecolagens[i], listaDecolagens[flag]

                flag+=1

        listaDecolagens[comeco], listaDecolagens[flag-1] = listaDecolagens[flag-1], listaDecolagens[pivot];

        quickSortPivotNoComecoPistaDiaHora(listaDecolagens, comeco, flag-2);
        quickSortPivotNoComecoPistaDiaHora(listaDecolagens, flag, fim);
