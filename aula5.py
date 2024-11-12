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

#




###################
##### Aula 5: Normalizar histograma

cinzaorig, cinzanorm, cinzaacu = histograma.histogramaplus(canalCinza)
niveis, imagemno = histograma.normalizados(cinzaacu, canalCinza)

#histograma da imagem original
histograma.plotarGrafico(cinzaorig, 'grey')
#histograma da imagem normalizada
histograma.plotarGrafico(cinzanorm, 'grey')
#histograma da imagem acumulada
histograma.plotarGrafico(cinzaacu, 'grey')

#histograma da imagem mapeada
normalhist = histograma.hist(imagemno, 'ksadlfkal')
histograma.plotarGrafico(normalhist, 'grey')


cv2.imshow("imagem original", canalCinza)
cv2.imshow("imagem mapeada", imagemno)

#cv2.imshow("imagem expandida", img_expandida) #bom para usar com a imagem de neve
cv2.waitKey(0) 