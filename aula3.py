# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
entrada = 'entrada.jfif'
#entrada = 'arrozfeijao.png'
#entrada = 'fluminense.png'
import cv2
import numpy as np
import matplotlib.pyplot as plt
import histograma


imagem = cv2.imread(entrada)

print('tamanho da matriz:',imagem.shape)



#transformando imagem colorida em tons de cinza
canalCinza = histograma.CanalCinza(imagem)



print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))


#criando eixo x do histograma



cinza = histograma.hist(canalCinza, "cinza")

histograma.plotarGrafico(cinza, 'grey')

###################
##### Aula 3: Deixar apenas cor Branca e cor preta da imagem
corBranca, corPreta = histograma.BrancoPreto(canalCinza, 140)
cv2.imshow("Imagem em tons de cinza", canalCinza)
cv2.imshow("Imagem Branca", corBranca)
cv2.imshow("Imagem Preta", corPreta)
cv2.waitKey(0) #espera pressionar tecla

#######
#########Aula 3: pegar imagem onde o histograma tem vários vales
cor1 = histograma.CanalCinza(imagem)            
cor2 = histograma.CanalCinza(imagem)
cor3 = histograma.CanalCinza(imagem)

for i in range(cor1.shape[0]):
    for j in range(cor1.shape[1]):
        if  cor1[i][j] > 55:
           cor1[i][j] = 255



for i in range(cor2.shape[0]):
    for j in range(cor2.shape[1]):
        if  cor2[i][j] > 55 and cor2[i][j] < 145:
            cor2[i][j] = 255
            


for i in range(cor3.shape[0]):
    for j in range(cor3.shape[1]):
        if  cor3[i][j] < 145:
            cor3[i][j] = 255
            
            
cv2.imshow("Imagem no primeiro vale", cor1)   
cv2.imshow("Imagem no segundo vale", cor2)  
cv2.imshow("Imagem no terceiro vale", cor3)
cv2.waitKey(0) #espera pressionar tecla