from zipfile import ZipFile
import io
from typing import Sized
from No import *
from Selection_Sort import *
from struct import *
import pickle
import csv
import os, pickle, timeit
import re

tipo_txt = 0
f = (open("zip.dv2", "w+b"))


def menu():
    print()
    print("\t------------------Darth Vader Zip----------------------")
    print()
    x = str(input("\tDigite nome do arquivo que deseja coprimir \n \texemplo:Compressor_2.txt\n\t"))



    return x

def conta_letras(x):
    print()
    print("\t------------------Darth Vader Zip----------------------")
    print()
    # x=str(input("\tDigite nome do arquivo que deseja coprimir \n \texemplo:Compressor_2.txt\n\t"))
    letra_cada_texto = []  # armazena a quantidade de letras de cada texto

    if (x == 'Compressor_2.txt'):
        global tipo_txt
        tipo_txt = 1
    texto_1 = io.open(x, mode="r", encoding="utf-8")

    texto_2 = io.open('Compressor_2.txt', mode="r", encoding="utf-8")
    texto_3 = io.open('Compressor_3.txt', mode="r", encoding="utf-8")
    texto_4 = io.open('Compressor_4.txt', mode="r", encoding="utf-8")
    texto_5 = io.open('Compressor_5.txt', mode="r", encoding="utf-8")

    cont_letras = ""
    for i in texto_1:
        if (i == "\n"):
            cont_letras += '*'
        else:
            cont_letras += i

    letra_cada_texto.append((cont_letras))

    cont_letras = ""
    for i in texto_2:
        cont_letras += i
    letra_cada_texto.append((cont_letras))

    cont_letras = ""
    for i in texto_3:
        cont_letras += i
    letra_cada_texto.append((cont_letras))

    cont_letras = ""
    for i in texto_4:
        cont_letras += i
    letra_cada_texto.append((cont_letras))

    cont_letras = ""
    for i in texto_5:
        cont_letras += i
    letra_cada_texto.append((cont_letras))

    return (letra_cada_texto)  # retorna um vetor com todos os carracters em cada texto


def frequencia(vet: list):
    temp = ""
    dicionario = {}
    lista_de_frequencias = []
    temp = {}
    cont = 0
    for i in vet[0:1]:
        for letra in i:
            if (letra in dicionario):
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

    temp = dicionario.copy()
    lista_de_frequencias.append(temp)
    dicionario.clear()
    for i in vet[1:2]:
        for letra in i:
            if (letra in dicionario):
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

    temp = dicionario.copy()
    lista_de_frequencias.append(temp)
    dicionario.clear()
    for i in vet[2:3]:

        for letra in i:
            if (letra in dicionario):
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

    temp = dicionario.copy()
    lista_de_frequencias.append(temp)
    dicionario.clear()
    for i in vet[3:4]:
        for letra in i:
            if (letra in dicionario):
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

    temp = dicionario.copy()
    lista_de_frequencias.append(temp)
    dicionario.clear()
    for i in vet[4:5]:
        for letra in i:
            if (letra in dicionario):
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

    temp = dicionario.copy()
    lista_de_frequencias.append(temp)
    dicionario.clear()
    return lista_de_frequencias  # retorna todas as ferquencias


def frequencia_para_no(vet, texto: int):  # vetor de frequencia e o numero do texto
    x = vet[texto]
    vetor_de_Nos = []
    temp = []
    for chave, valor in x.items():
        temp.append(Nos(chave, valor, None))
    return temp


def arquivo_com_frequencias(vet):
    frequencia = open("Frequencia.dv1", "w")
    for i in vet:
        tenp_str = (str(i.chave))
        tenp_str2 = (str(i.valor))
        frequencia.write(tenp_str + tenp_str2 + '\n')
    frequencia.close()


def adiciona_no(vet: list, temp: Nos):
    cont = -1
    for i in range(len(vet)):
        if (temp.valor <= vet[i].valor):
            cont += 1
            vet.insert(i, temp)
            break
    if cont == -1:
        vet.append(temp)


def chave_binario2(raiz, vet):#percore a arvore e adiciona em uma lista chave e seu binario
    if (raiz != None):
        chave_binario2(raiz=raiz.direita, vet=vet)
        if (raiz.chave != None):
            vet.append((raiz.chave, raiz.binario))
        chave_binario2(raiz=raiz.esquerda, vet=vet)


def enconta_binario(vet, texto_str, nova_chave_valor,dicionario):  # vet=vetor com binario de cada letra ,

    vet2 = []

    # (a,[b])chave er vetor de int
    for letra in texto_str:
        for i in vet:
            if (i[0] == letra):
                # print(letra)

                nova_chave_valor.append(i)
                #dicionario[i[0]]=str(vetor_int(i[1]))
                temp=str(vetor_int(i[1]))
                dicionario[temp]= i[0]
                x = (i[1])
                # print(i[1])
                for k in range(len(x)):
                    temp = (x[k])
                    vet2.append(temp)

    return vet2  # gera o vetor com todos os inteiros que correspondem a um byte


def fraciona_vet(vet):  # cont==len(vet)//8
    vet8 = []
    while (len(vet) != 0):
        vet8 = vet[:8]
        vet = vet[8:]

        # print(vet8)
        compressao2(vet8)

    f.close()
    print("\tcompressao terminada ")


def byte_int(temp3):
    y = int.from_bytes(temp3, byteorder='big', signed=True)
    return y


def compressao2(temp3):  # recebe um vetor com 8 inteiro
    # print(temp3)
    temp = 0
    c = 1
    cont = 7
    i = 0
    k = len(temp3)
    if (k < 8):
        cont = len(temp3) - 1

    while (cont != -1):
        c = (temp3[i])

        c = c << cont

        temp = (temp | c)
        i = i + 1
        cont = cont - 1
        if (cont == -1):
            x = temp.to_bytes((temp.bit_length() + 7) // 8, 'big')

            f.write(x)


def lendo_arquivo_frequencia():
    x = open("Frequencia.dv1", mode="r")
    temp = x.readlines()
    tupla = ()
    lista = []
    for i in temp:

        if (
                i.encode() != b'1\n' and i.encode() != b'2\n' and i.encode() != b'3\n' and i.encode() != b'4\n' and i.encode() != b'5\n'):#corige o erro do \n
            x = i[1:]
            tupla = (i[0], (x.strip('\n')))
            lista.append(tupla)
    return lista


def vetor_int(vet):
    i = len(vet)
    cont = 0
    temp = 0
    while (cont != i):
        temp = temp + vet[cont]

        temp = temp * 10
        cont = cont + 1
    return (temp // 10)


def converte_dicionario(vet,nome_texto):
    temp = []
    dicionario = {}
    for i in vet:
        # print(i[0],(i[1]))
        x = map(int, i[1])
        t = list(x)
        k = vetor_int(t)

        dicionario[i[0]] = k
    if (nome_texto!='Compressor_1.txt' ):
        z = dicionario.get('*')

        dicionario['*'] = z * 2

    temp.append(dicionario)
    return temp


def split_int(num):
    temp = []
    while num > 0:
        temp.append(num % 10)
        num //= 10
    return temp[::-1]


def decode(vet4, input,tamanho_texto):#a demora na descompressao e por conta que essa funçao tem complexidade bigO(n^3)
    output = ''
    curr_code = ''
    temp = ''

    for ele in input:#percorre string de binario
        curr_code += ele
        for j in range(len(vet4)):#percorre um vetor com caracter e binario exemplo['carcter':[1,0,1,1]]
                for i in vet4[j][1]:#trasforma o int em str
                     temp += str(i)
            # print(temp)
                if curr_code in temp and len(output)<tamanho_texto:# compara o binario do str binario com temp

                     if (vet4[j][0] != '*'):#tratando o \n
                            output += str(vet4[j][0])
                     else:
                             output += '\n'

                curr_code = ''
                temp = ''


    return output



def removePadding(input):
    pad_info = input[:8]
    input = input[8:]
    pad_info = int(pad_info, 2)
    input = input[:-1 * pad_info]

    return input

def decompres(vet4,dicio,tamanho_texto):
    output_path = 'descompressão.txt'
    with open('zip.dv2', 'rb') as file, open(output_path, 'w') as output:
        bit_string = ''
        byte = file.read(1)
        while byte:
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = file.read(1)
        bit_string = removePadding(bit_string)
        decoded_text = decode(vet4, bit_string,tamanho_texto)
        #decoded_text = decode2(vet4, bit_string,dicio)

        output.write(decoded_text)
    print('\n\tdescompressao terminada ')

    return output_path
