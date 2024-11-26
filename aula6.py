# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
entrada = 'entrada.jfif'
#entrada = 'alpes.jpg'
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





###################
##### Aula 6: histograma ficticio
np.random.seed(0)



#gerando histograma da parabola
tamanho = 256

# Gerando os valores para a primeira metade (1000 a 0)
primeira_metade = np.linspace(1000, 0, tamanho // 2)

# Gerando os valores para a segunda metade (0 a 1000)
segunda_metade = np.linspace(0, 1000, tamanho // 2)

# Combinando as duas metades
array_final = np.concatenate([primeira_metade, segunda_metade])
histograma.plotarGrafico(array_final, 'grey')



#hist normalizado
total = np.sum(array_final)
histNorm = array_final / total
histograma.plotarGrafico(histNorm, 'blue')

#hist acum
histograma_acumulado = np.zeros(256)
acumulado = 0.0
for i in range(256):
    acumulado += histNorm[i]
    histograma_acumulado[i] = acumulado
    
histograma.plotarGrafico(histograma_acumulado, 'red')








#COISAS DA IMAGEM - AULA PASSADA
cinzaorig, cinzanorm, cinzaacu = histograma.histogramaplus(canalCinza)
#histograma da imagem original
histograma.plotarGrafico(cinzaorig, 'grey')
#histograma da imagem normalizada
#histograma.plotarGrafico(cinzanorm, 'grey')
#histograma da imagem acumulada
#histograma.plotarGrafico(cinzaacu, 'grey')



#histograma da imagem mapeada
mapa1, imagemmap = histograma.normalizados(cinzaacu, canalCinza)
normalhist = histograma.hist(imagemmap, 'ksadlfkal')
histograma.plotarGrafico(normalhist, 'grey')



####################Mapeando imagem no histograma parabolo
mapeamento = np.zeros_like(mapa1, dtype=np.uint8)

#histograma feito na aula de hoje
mapa2 = np.round(histograma_acumulado * 255).astype(np.uint8)
#mapa1 é o histograma feito a partir da imagem, já teve a conta acima aplicada


#normal hist mapeado para histograma_acumulado, dps processo da imagem com o resultado
#errado tambem
mapeamento = np.array([mapa2[np.abs(mapa2-val).argmin()] for val in mapa1])

#erro
#    while i < 256 and j < 256:
 #       # Mapeia o valor de intensidade de mapa1 para mapa2
  #      if mapa1_normalizado[i] < mapa2_normalizado[j]:
   #         i += 1
    #    else:
     #       mapeamento[i] = j
      #      j += 1


histograma.plotarGrafico(mapeamento, 'pink')

imagem_normalizada = mapeamento[canalCinza]
testee = histograma.hist(imagem_normalizada, 'ksadlfkal')
histograma.plotarGrafico(testee, 'red')








#a, b = histograma.normalizados(mapeamento, canalCinza)
#testee = histograma.hist(b, 'ksadlfkal')
#histograma.plotarGrafico(testee, 'red')




cv2.imshow("imagem original", canalCinza)
cv2.imshow("imagem equalizada", imagemmap)
cv2.imshow("imagem especificada", imagem_normalizada)

#cv2.imshow("imagem expandida", img_expandida) #bom para usar com a imagem de neve
cv2.waitKey(0) 