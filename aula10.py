# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
#entrada = 'entrada.jfif'
#entrada = 'taj.jfif'
#entrada = 'pisaa.jfif'
#entrada = 'roma.jfif'
#entrada = 'arrozfeijao.png'
#entrada = 'bolas2.png'
#entrada = 'j2.png'
entrada = "p.png"
#entrada = "impressao1.jpg"
#entrada = 'fluminense.png'
import cv2
import numpy as np
import matplotlib.pyplot as plt
import histograma


imagem = cv2.imread(entrada)


#transformando imagem colorida em tons de cinza
canalCinza = histograma.CanalCinza(imagem)



print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))





###################
##### Aula 10: fazer abertura da imagem
np.random.seed(0)

histo = histograma.hist(canalCinza, 'a')
histograma.plotarGrafico(histo, 'grey')
BW = histograma.BWimg(canalCinza, 150)


#utilizando uma matriz 3x3 preenchida com 1
matrizest =  np.full((3, 3), 1)
#mascara em cruz suaviza mais
mascara = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]])
#escolher qual matriz-máscara utilzar
def abertura(imagem, mascara, repeticoes):
    erodida = histograma.erosao(imagem, mascara, repeticoes)
    aberta = histograma.dilatacao(erodida, mascara, repeticoes)
    return aberta

def fechamento(imagem, mascara, repeticoes):
    dilatada = histograma.dilatacao(imagem, mascara, repeticoes)
    fechada = histograma.erosao(dilatada, mascara, repeticoes)
    return fechada
#dilatada = abertura(BW, matrizest , 1)
#erodida = histograma.erosao(BW, matrizest, 1)
#print('tamanho da img orig: ', BW.shape)
#print('tamanho da img erod: ', erodida.shape)

#resultado= histograma.dilatacao(erodida, matrizest, 1)
#print('tamanho da img dilat: ', dilatada.shape)

#dilatada = histograma.dilatacao(BW, matrizest, 1)
#resultado = histograma.erosao(dilatada, matrizest, 1)
 
aberta = abertura(BW, matrizest , 1)
resultado = fechamento(aberta, matrizest, 1)
 
cv2.imshow("imagem em preto e branco", BW)
#cv2.imshow("imagem erodida", erodida)
#cv2.imshow("imagem dilatada", dilatada)
cv2.imshow("imagem apos abertura", aberta)
cv2.imshow("imagem apos operacao", resultado)
cv2.waitKey(0) 
