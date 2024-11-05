# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
#entrada = 'entrada.jfif'
entrada = 'alpes.jpg'
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
##### Aula 4: Adicionar função de curvas de tom a imagem (cr + l)
#contraste = histograma.curvaTom(canalCinza, 1, 0)
#gera imagem negativa
#contraste2 = histograma.curvaTomNeg(imagem, 1, 0)
#cv2.imshow("imagem original", imagem)
#cv2.imshow("imagem com tons", contraste)
#cv2.imshow("imagem com tons negativa", contraste2)


#gera histograma da imagem com curva de tom
#cont = histograma.hist(contraste, "contrastada1")
#histograma.plotarGrafico(cont, 'blue')
#cont = histograma.hist(contraste2, "negativa")
#histograma.plotarGrafico(cont, 'blue')

#Expande uma imagem com pouco contraste
img_expandida = histograma.expansaohist(canalCinza, 110, 215)
exp = histograma.hist(img_expandida, "imagem expandida")
histograma.plotarGrafico(exp, 'red')
cv2.imshow("imagem original", canalCinza)
cv2.imshow("imagem expandida", img_expandida) #bom para usar com a imagem de neve
cv2.waitKey(0) 