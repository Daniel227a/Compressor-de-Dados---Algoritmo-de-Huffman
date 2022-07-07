from Funcoes import *
from Huffman import *
import copy
import io
from io import BytesIO
import  ctypes
import pickle
#mport decode

descopr_comt=0
nome_texto=menu()
textos = conta_letras(nome_texto)#vetor com todas as letras  de todos os textos texto1==textos[0]

lista_de_frequencias = frequencia(textos)#todas as frequencias lista de dicionario com chave e valor
lista_de_nos = frequencia_para_no(lista_de_frequencias, 0)#gera os nos para um texto

sort(lista_de_nos)  # ordena Llista de nos

lista_de_nos2 = lista_de_nos.copy()#cria copia da lista de nos
arquivo_com_frequencias(lista_de_nos2)#gera o dv1
soma_menor(lista_de_nos)  # huffmann

teste = lista_de_nos[0]  # texto1
teste2 = lista_de_nos[0]

gera_binario4(teste, None)#gera valor de 0 ou 1 para ramos da arvore
dicio1={}
vet3 = []

arquivo_com_frequencias(lista_de_nos2)#dv1 =com frequencia
chave_binario2(teste, vet3)#retorna chave== letra e seu repectivo valor em "binario"
nova=[]
lista_de_pseudo_byte=enconta_binario(vet3, textos[0],nova,dicio1)#retorna todos os inteiros correspondentes ao valor binario de cada letra

fraciona_vet(lista_de_pseudo_byte)#gera sub vetores de 8 inteiros e chama a funçao compressao para gerar o byte e colocar no arquivo

##############################################
while descopr_comt == 0:
    print("\tpara  descomprimir o arquivo digite 1 ")
    print("\tpara sair digite 2")
    descopr_comt = int(input())
    if (descopr_comt == 2):
        exit()
    if (descopr_comt == 1):
        print("\taquarde a descompressao 'a paciencia é uma virtude'Clarice Lispector ")

    else:

        descopr_comt = 0

lista_fr_arquivo=lendo_arquivo_frequencia()
vg=converte_dicionario(lista_fr_arquivo,nome_texto)
lista_de_nos2 = frequencia_para_no(vg, 0)
soma_menor(lista_de_nos2)# huffmann
teste2 = lista_de_nos2[0]
gera_binario4(teste2, None)
vet4=[]
dicio={}
chave_binario2(teste2, vet4)
lista_de_pseudo_byte=enconta_binario(vet3, textos[0],nova,dicio)#nova e cada letra e seu binario correspondente

texto_descoprimido=decompres(nova,dicio,len(textos[0]))#len(textos[0]) para nao descomprimir byts com lixo

k=open(texto_descoprimido,'r')
print("\to arquivo de descompressao  "+texto_descoprimido+"  foi criado ")
print()
print("\tmostrando texto    ")
print()
for i in k:
   print('\t'+i,end='')


print()
