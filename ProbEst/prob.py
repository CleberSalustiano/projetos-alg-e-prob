#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  prob.py
#
#  Copyright 2021
#  Autores: Josué Ramos Souza , Cléber de Jesus Salustiano
#  Matricula: 20202BSI0292, 20202BSI0268
#  
# Este é um programa que a partir de uma váriavel contínua de uma base de dados
# Traça um Histograma, Calcula medidas de tendencia central, calcula medidas de dispersão
# Traça o box-plot
#########################################
import sys
import pandas as pd # Importando biblioteca para organização e Data frames
import matplotlib.pyplot as plt # Biblioteca de graficos
dados = pd.read_csv("./Notas2.csv") #Arquivo com as notas linha por linha
dados.head()

#Exibe Histograma
plt.style.use("classic")
dados.hist(column='notas', bins=11)
plt.axis([0, 10, 0.00, 600]) # Xmin, Xmax, Ymin, Ymax
plt.ylabel("Frequência:")
plt.title("Notas:",fontsize=14,fontweight='bold')
plt.grid(b=True,which='major')
plt.show()

dados.boxplot(column='notas')
#Exibe box-plot
plt.minorticks_on()
plt.grid(b=True,which="minor")
plt.show()
#Le arquivo
def readline(arq):
    lines = arq.readlines()
    array = []
    for line in lines:
        line = line.split(',')
        line[9] = line[9].replace('\n', '')
        i = 0
        for char in line:
            line[i] = int(char)
            i += 1
        array.append(line)
    return array


def numberNotes(array):
    freqNotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for elements in array:
        for element in elements: #se tiver um elemento no array [posição] conta +1
            freqNotes[element] += 1
    return freqNotes


def media(freqNotes):
    media = 0
    total = 0
    i = 0
    for freq in freqNotes:
        media += freq * i
        i += 1
        total += freq
    media = media / total
    return media, total


def mediana(freqNotes):
    medianaPosition = (len(array)*10)/2
    freqAcumulated = 0
    for freq in freqNotes:
        freqAcumulated += freq
        if(freqAcumulated >= medianaPosition):
            mediana = freqNotes.index(freq)
            break
    return mediana


def moda(freqNotes):
    moda = 0
    modaQnt = 0
    for freq in freqNotes:
        if freq > modaQnt:
            modaQnt = freq
            moda = freqNotes.index(freq)
    return moda


def dms(freqNotes, media, total):
    dms = 0
    dmsAccumulated = 0
    for freq in freqNotes:
        if ((freqNotes.index(freq) - media) < 0):
            dmsAccumulated += ((freqNotes.index(freq) - media) * (-1)) * freq
        else:
            dmsAccumulated += ((freqNotes.index(freq) - media)) * freq
    dms = dmsAccumulated / total
    return dms


def varianca(freqNotes, media, total):
    varAcumulated = 0
    for freq in freqNotes:
        varAcumulated += ((freqNotes.index(freq) - media)**2)*freq
    varianca = varAcumulated / total
    return varianca


def quartis(freqNotes, total):
    quartilOne = 0
    posQuartilOne = (25*total)/100
    quartilThree = 0
    posQuartilThree = (75*total)/100

    freqAccumulated = 0
    for freq in freqNotes:
        freqAccumulated += freq
        if posQuartilThree <= freqAccumulated:
            quartilThree = freqNotes.index(freq)
            break
        if posQuartilOne <= freqAccumulated:
            if quartilOne > 0:
                continue
            quartilOne = freqNotes.index(freq)

    return quartilOne, quartilThree


arq = open('Notas.csv', 'r')
array = readline(arq)
freqNotes = numberNotes(array)
media, totalData = media(freqNotes)
mediana = mediana(freqNotes)
moda = moda(freqNotes)
dms = dms(freqNotes, media, totalData)
varianca = varianca(freqNotes, media, totalData)
devPadrao = varianca**(1/2)
quartilOne, quartilThree = quartis(freqNotes, totalData)

file_path = './dados.txt'
sys.stdout = open(file_path, "w")
print('Dados para Histograma: ')
for freq in freqNotes:
    print(freqNotes.index(freq), ': ', freq)

print('\nMedidas Separatrizes')
print('Media: ', round(media, 2))
print('Mediana: ', mediana)
print('Moda: ', moda)

print('\nMedidas de Dispersão')
print('Desvio Médio Simples: ', round(dms, 2))
print('Variança', round(varianca, 2))
print('Desvio Padrão: ', round(devPadrao, 2))

print('\nDados para o Box-Plot: ')
print('Limite inferior: 0')
print('Quartil1: ', quartilOne)
print('Quartil2: ', mediana)
print('Quartil3: ', quartilThree)
print('Limite superior: ', len(freqNotes) - 1)
