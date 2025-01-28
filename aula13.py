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
#entrada = 'contorno.png'
entrada = 'olhos3.png'
#entrada = "output_image.png"
#entrada = "impressao1.jpg"
#entrada = 'fluminense.png'
import cv2
import numpy as np
import matplotlib.pyplot as plt
import histograma


imagem = cv2.imread(entrada)
print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))
#transformando imagem colorida em tons de cinza
canalCinza = histograma.CanalCinza(imagem)





np.random.seed(0)

BW = histograma.BWimg(canalCinza, 150)


#utilizando uma matriz 3x3 preenchida com 1
matrizest =  np.full((3, 3), 1)
#mascara em cruz suaviza mais
mascara = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]])

#escolher qual matriz-máscara utilzar

###################
##### Aula 13: Extração de Componentes Conectados
matrix = np.array([
    [0,  0,  0,  0,  0, 0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0, 0,  255, 255, 255,  0],
    [0,  0,  0,  0,  0, 0,  255, 255, 255,  0],
    [0,  0,  0,  0,  0, 255,  255, 0, 255,  0],
    [0,  0,  0,  0,  0, 255,  255,  255,  255,  0],
    [0, 0, 0, 255, 255, 255, 0, 0, 0, 0],  # Eixo horizontal
    [0,  0, 255, 255,  255, 0,  0,  0,  0,  0],
    [0,  255, 0, 0,  255, 0,  0,  0,  0,  0],
    [0,  0,  255,  255,  255, 0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0, 0,  0,  0,  0,  0]
])
#se usar a matriz:
matriz_uint8 = matrix.astype(np.uint8)
imagem = matriz_uint8
BW = histograma.BWimg(imagem, 150)
#definindo primeiro ponto na imagem
X = np.zeros_like(BW)
X[6, 3] = 255


while True:
    X_next = histograma.dilatacao(X, matrizest, 1)  # Dilatação
    #print("Matriz inicial:\n", X_next)

    X_next = np.where((X_next == 255) & (BW == 255), 255, 0).astype(np.uint8)  # Restrição ao buraco

    if np.array_equal(X, X_next):  # Se não mudou, paramos
        break
    
    X = X_next  # Atualizamos X para continuar expandindo
    # Exibir resultado final
    print("Matriz final preenchida:\n", X)


resultado = X.copy()

print("Matriz inicial:\n", imagem)
print("Matriz após dilatações:\n", X)
print("Matriz final preenchida:\n", resultado)

cv2.imshow("imagem original", imagem)
cv2.imshow("imagem após dilatações", X)
cv2.imshow("imagem final", resultado)
cv2.waitKey(0) 