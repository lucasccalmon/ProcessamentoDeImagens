# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:41:02 2024

@author: 19123556714
"""

import numpy as np
import matplotlib.pyplot as plt

def hist(imagem, canal):
    histograma = np.zeros(256, dtype=np.uint)
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] += 1
    return histograma

def plotarGrafico(X, imagem, cor):
    plt.xlabel('Pixel')
    plt.ylabel('Quantidade')
    plt.title('Histograma da Imagem em Tons da cor do gráfico')
    plt.bar(X, imagem, color=cor)
    plt.show()
    