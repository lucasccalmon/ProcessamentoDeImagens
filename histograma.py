# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:41:02 2024

@author: 19123556714
"""

import numpy as np
import matplotlib.pyplot as plt

def CanalCinza(imagem):
    canalCinza = np.zeros((imagem.shape[0], imagem.shape[1]), dtype= np.uint8)
    for linha in range (imagem.shape[0]):
            for coluna in range (imagem.shape[1] ):
                canalCinza[linha, coluna] = (imagem[linha, coluna].sum()//3)
    return canalCinza

def hist(imagem, canal):
    histograma = np.zeros(256, dtype=np.uint)
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] += 1
    return histograma

def plotarGrafico(imagem, cor):
    X = [0] * 256
    for i in range(256):
        X[i] = i
    plt.xlabel('Pixel')
    plt.ylabel('Quantidade')
    plt.title('Histograma da Imagem em Tons da cor do gráfico')
    plt.bar(X, imagem, color=cor)
    plt.show()
    
def BrancoPreto(imagemCinza, corte):
    corBranca = imagemCinza.copy()
    corPreta = imagemCinza.copy()
    for i in range(corBranca.shape[0]):
        for j in range(corBranca.shape[1]):
            if  corBranca[i][j] < corte:
               corBranca[i][j] = 255
               
    for i in range(corPreta.shape[0]):
        for j in range(corPreta.shape[1]):
            if  corPreta[i][j] > corte:
                corPreta[i][j] = 255
                
    return corBranca, corPreta

