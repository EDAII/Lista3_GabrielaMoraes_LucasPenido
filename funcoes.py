import random
import string
from os import system
from datetime import date, time
from faker import Faker

fake = Faker()

class Decolagem:
    numeroVoo: str 
    dia: date
    hora: time
    pista: int 

def darBoasVindas():
    system("clear")
    print("Seja bem vindo, controlador de voo!")
    print("Esse é o painel informativo de decolagens")
    print("\n\nInformações importantes: ")
    print("- Esse programa gerencia somente as decolagens;")
    print("- O aeroporto possui 3 pistas para decolagem;")
    print("- Cada vôo possui os seguintes campos:")
    print(" 1. Número do Vôo")
    print(" 2. Data de partida")
    print(" 3. Horário")
    print(" 4. Número da pista")

def exibirMenu():
    print("========================== Menu Principal =====================================")
    print("\n1. Ver decolagens")
    print("0. Sair")

def recebeOpcaoMenuValida():
    opcao = str(input("\n\nDigite a opção que deseja executar: "))
    while (opcao < '0') or (opcao > '1'):
        print("Opção Inválida! Digite novamente")
        opcao = str(input("Digite a opção que deseja executar: "))
    return int(opcao)

def escolheNumeroDecolagens():
    numeroDecolagens = str(input("\n\nQuantas decolagens você deseja que o programa gerencie:  "))
    while (numeroDecolagens < '1'):
        print("Número inválido! Digite novamente um número maior que zero")
        numeroDecolagens = str(input("\n\nQuantas decolagens você deseja que o programa gerencie:  "))
    return int(numeroDecolagens)

def gerarDecolagens(listaDecolagens, numeroDecolagens):
    # listaDecolagens = []
    nPista = 1
    for i in range(0, numeroDecolagens):
        if(nPista > 3):
            nPista = 1

        decolagem = Decolagem()
        decolagem.numeroVoo = ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + ''.join(random.choice(string.digits) for _ in range(4))

        while any(d.numeroVoo == decolagem.numeroVoo for d in listaDecolagens):
            decolagem.numeroVoo = ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + ''.join(random.choice(string.digits) for _ in range(4))

        decolagem.dia = fake.date_between(start_date='today', end_date='+180d')        
        decolagem.hora = fake.time(pattern="%H:%M", end_datetime=None)
        decolagem.pista = nPista
        
        while any(d.dia == decolagem.dia and d.hora == decolagem.hora and d.pista == decolagem.pista for d in listaDecolagens):
            decolagem.dia = fake.date_between(start_date='today', end_date='+180d')        
            decolagem.hora = fake.time(pattern="%H:%M", end_datetime=None)
        
        # print(decolagem.numeroVoo, decolagem.dia, decolagem.hora, decolagem.pista)
        listaDecolagens.append(decolagem)
        nPista += 1

    return listaDecolagens

def imprimeListaVoos(tamanho, lista):
    print("======================== Lista de Decolagens ==========================\n\n")
    for i in range (0, tamanho):
        print("============= Voo ", i+1, "===============")
        print("Número do Vôo: " + lista[i].numeroVoo)
        print("Data de partida:",lista[i].dia)
        print("Horário: " + lista[i].hora)
        print("Número da pista:",lista[i].pista, "\n\n")

def exibirMenuOrdenacao():
    print("========================== Você deseja ordenar por qual critério ? =====================================")
    print("\n1. Número do Vôo")
    print("2. Dia")
    print("3. Horário")
    print("4. Pista")
    print("5. Dia e horário")
    print("6. Dia, horário e pista")
    print("0. Sair")

def recebeOpcaoMenuOrdenacaoValida():
    criterio = str(input("\n\nDigite o número correspondente ao critério que você deseja: "))
    while criterio.isnumeric() == False or (int(criterio) < 0) or (int(criterio) > 6):
        print("Opção Inválida! Digite novamente")
        criterio = str(input("Digite o número correspondente ao critério que você deseja: "))
    return int(criterio)
    
def gerenciaVoosAdicionais(listaDecolagens):
    alteracao = input("Algum vôo foi cancelado ou adicionado? (S para sim / N para não) ")
    alteracao = alteracao.lower()
    while(alteracao != "n") and (alteracao != "s"):
        print("Caracter inválido! Digite novamente")
        alteracao = input("Algum foi cancelado ou adicionado? (S para sim / N para não) ")
        alteracao = alteracao.lower()
    if(alteracao == 's'):
        print("O vôo foi: ")
        print("1. Cancelado")
        print("2. Adicionado")
        operacao = input("Digite o número: ")
        while operacao.isnumeric() == False or (int(operacao) < 1) or (int(operacao) > 2):
            print("Opção Inválida! Digite novamente")
            operacao = input("Digite o número: ")
        if(int(operacao) == 1):
            cdVoo = input("Digite o código do vôo que foi cancelado: ")
            posicao = buscaSequencial(listaDecolagens, cdVoo)
            if(posicao == -1):
                print("\nEsse vôo não foi encontrado. Tente novamente!")
                input("\n\nAperte QUALQUER tecla para continuar")
                imprimeListaVoos(len(listaDecolagens), listaDecolagens) 
            else:
                del(listaDecolagens[posicao])
                print("\nVôo deletado com sucesso!")
                input("\n\nAperte QUALQUER tecla para continuar")
                imprimeListaVoos(len(listaDecolagens), listaDecolagens)  
        else:
            novasDecolagens = input("Quantos vôos foram adicionados: ")
            while novasDecolagens.isnumeric() == False or (int(novasDecolagens) < 1):
                print("Número Inválido! Digite novamente")
                novasDecolagens = input("Quantos vôos foram adicionados: ")
            gerarDecolagens(listaDecolagens, int(novasDecolagens))
            imprimeListaVoos(len(listaDecolagens), listaDecolagens)

def buscaSequencial(listaDecolagens, valorBuscado):
    for i in range(0, len(listaDecolagens)):
        if(listaDecolagens[i].numeroVoo == valorBuscado):
            return int(i)
    return -1
    
