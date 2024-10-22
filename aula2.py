# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
entrada = 'entrada.jfif'
#entrada = 'fluminense.png'
import cv2
import numpy as np
import matplotlib.pyplot as plt
import histograma


imagem = cv2.imread(entrada)

print('tamanho da matriz:',imagem.shape)



#transformando imagem colorida em tons de cinza
canalCinza = np.zeros((imagem.shape[0], imagem.shape[1]), dtype= np.uint8)
for linha in range (imagem.shape[0]):
        for coluna in range (imagem.shape[1] ):
            canalCinza[linha, coluna] = (imagem[linha, coluna].sum()//3)

cv2.imshow("a", canalCinza)
cv2.waitKey(0) #espera pressionar tecla

#
#
#------------------------------------------------
#Criar histograma (aula 2)

#MESMA COISA DA BIBLIOTECA!!!!!!!
#for linha in canalCinza:
#    for valor in linha:
#        hist[valor] +=1
        
#count = 0
#for i in range(256):
#    count+=hist[i]
#print(hist)
print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))


#criando eixo x do histograma
pixel = [0] * 256
for i in range(256):
    pixel[i] = i


azul = histograma.hist(imagem[:,:,0], "Blue") #canalBlue
verde = histograma.hist(imagem[:,:,1], "Verde") #canalVerde
vermelho = histograma.hist(imagem[:,:,2], "Red") #canalRed
cinza = histograma.hist(canalCinza, "cinza")

count = 0
for i in range(256):
    count+=cinza[i]
print('Contagem do array da função hist():', count)

histograma.plotarGrafico(pixel, cinza, 'grey')
histograma.plotarGrafico(pixel, azul, 'blue')
histograma.plotarGrafico(pixel, verde, 'green')
histograma.plotarGrafico(pixel, vermelho,'red' )