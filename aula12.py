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
##### Aula 12: extração de fronteiras - detecção de contornos
#erosao = histograma.erosao(BW, matrizest, 1)
#deteccao = BW - erosao

#cv2.imshow("imagem original", imagem)
#cv2.imshow("imagem BW", BW)
#cv2.imshow("imagem após primeira erosao", erosao)
#cv2.imshow("imagem após deteccao", deteccao)
#cv2.waitKey(0) 

###################
##### Preenchimento de buracos 
matrix = np.array([
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 255, 255, 0, 0, 0],
    [0, 255, 0, 0, 255, 0, 0],
    [0, 255, 0, 0, 255, 0, 0],
    [0, 0, 255, 0, 255, 0, 0],
    [0, 0, 255, 0, 255, 0, 0],
    [0, 255, 0, 0, 0, 255, 0],
    [0, 255, 0, 0, 0, 255, 0],
    [0, 255, 255, 255, 255, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
])
#se usar a matriz:
#matriz_uint8 = matrix.astype(np.uint8)
#imagem = matriz_uint8
#BW = histograma.BWimg(imagem, 150)
#definindo primeiro ponto na imagem
def find_zero_with_255_neighbors(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(1, rows):  # Começamos de 1 para evitar acessar índices negativos
        for j in range(1, cols):
            if (
                matrix[i][j] == 0 and     # O ponto deve ser 0
                matrix[i-1][j] == 255 and # Acima deve ser 255
                matrix[i][j-1] == 255     # À esquerda deve ser 255
            ):
                return (i, j)  # Retorna a posição (linha, coluna)
    
    return None  # Se não encontrar, retorna None

position = find_zero_with_255_neighbors(BW)
print("Posição encontrada:", position)


complementoA = histograma.inverterBW(BW)

X = np.zeros_like(BW)
X[position] = 255


while True:
    X_next = histograma.dilatacao(X, mascara, 1)  # Dilatação
    #print("Matriz inicial:\n", X_next)

    X_next = np.where((X_next == 255) & (complementoA == 255), 255, 0).astype(np.uint8)  # Restrição ao buraco

    if np.array_equal(X, X_next):  # Se não mudou, paramos
        break
    
    X = X_next  # Atualizamos X para continuar expandindo
    # Exibir resultado final
   # print("Matriz final preenchida:\n", X)


resultado = X.copy()
resultado = X + BW
print("Matriz inicial:\n", imagem)
print("Matriz após dilatações:\n", X)
print("Matriz final preenchida:\n", resultado)

cv2.imshow("imagem original", imagem)
cv2.imshow("imagem após dilatações", X)
cv2.imshow("imagem final", resultado)
cv2.waitKey(0) 