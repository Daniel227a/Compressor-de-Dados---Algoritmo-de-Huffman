from Funcoes import *
from Selection_Sort import *
from No import *
from copy import copy

def soma_menor(vet):#cria um novo no apartir da soma de dois nos
    while len(vet) > 1:
        # print("A")
        temp = []

        temp = Nos(None, vet[0].valor + vet[1].valor, None)
        # print(temp.valor)
        if (vet[0].valor > vet[1].valor):
            vet[0].pai = (temp)

            temp.direita = (vet[0])
            vet[1].pai = (temp)
            temp.esquerda = (vet[1])

        if (vet[0].valor < vet[1].valor):
            vet[0].pai = (temp)
            temp.esquerda = (vet[0])
            vet[1].pai = (temp)
            temp.direita = (vet[1])

        if (vet[0].valor == vet[1].valor):
            vet[0].pai = (temp)
            temp.esquerda = (vet[0])

            vet[1].pai = (temp)
            temp.direita = (vet[1])

        vet.pop(0)
        vet.pop(0)

        adiciona_no(vet, temp)

def gera_binario4(raiz, byte):
    if (raiz != None):

             if (raiz.pai != None):

                    raiz.binario = copy(raiz.pai.binario)
                    raiz.binario.append(byte)

             if (raiz.direita != None):

                 gera_binario4(raiz=raiz.direita, byte=1)

             if (raiz.esquerda != None):

                 gera_binario4(raiz=raiz.esquerda, byte=0)

def em_ordem(raiz, letra):
    if raiz != None:
        # Visita filho da esquerda.
        em_ordem(raiz=raiz.esquerda, letra=None)
        print(raiz.chave, raiz.valor)
        em_ordem(raiz=raiz.direita, letra=None)

        # Visita nodo corrente.

        # Visita filho da direita.









