# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
entrada = 'entrada.jfif'
import cv2
import numpy



imagem = cv2.imread(entrada)
#colunas
print('Largura da imagem em pixels:', end='')
print(imagem.shape[1])

#linhas
print('Altura da imagem em pixels:', end='')
print(imagem.shape[0])

#canais da imagem
print('qtde de canais:', end='')
print(imagem.shape[2])

(b,g,r) = imagem[0, 0]
print (b, g, r)
print(imagem.shape)
print(imagem.size)
print(imagem.ndim)


#trasnformando a imagem
canalBlue = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype= numpy.uint8)
canalGreen = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype= numpy.uint8)
canalRed = numpy.zeros((imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype= numpy.uint8)

canalBlue[:,:,0] = imagem[:,:,0]
canalGreen[:,:,1] = imagem[:,:,1]
canalRed[:,:,2] = imagem[:,:,2]

#mono cor
#cv2.imshow("Nome da janela", canalBlue)
#cv2.imshow("Nome da janela", canalGreen)
#cv2.imshow("Nome da janela", canalRed)

#tons de cinza
#cv2.imshow("Nome da janela", imagem[:,:,0])
#cv2.imshow("Nome da janela", imagem[:,:,1])
#cv2.imshow("Nome da janela", imagem[:,:,2])

#canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype= numpy.uint8)
#for linha in range (imagem.shape[0]):
     # for coluna in range (imagem.shape[1] ):
    #      canalCinza[linha, coluna] = int((int(imagem[linha, coluna, 0]) + int(imagem[linha,coluna, 1]) + int(imagem[linha, coluna, 2]))/ 3)

#transformando imagem colorida em tons de cinza
canalCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype= numpy.uint8)
for linha in range (imagem.shape[0]):
        for coluna in range (imagem.shape[1] ):
            canalCinza[linha, coluna] = (imagem[linha, coluna].sum()//3)

cv2.imshow("a", canalCinza)
cv2.waitKey(0) #espera pressionar tecla

#mostra a imagem
#cv2.imshow("Nome da janela", imagem)
#cv2.waitKey(0) #espera pressionar tecla

#Salvar imagem no disco
cv2.imwrite("saida.jpg", imagem)
