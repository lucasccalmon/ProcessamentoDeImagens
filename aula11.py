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
#entrada = "output_image.png"
#entrada = "impressao1.jpg"
#entrada = 'fluminense.png'
import cv2
import numpy as np
import matplotlib.pyplot as plt
import histograma


#gerando imagem
matriz = np.zeros((200, 200), dtype=int)

# Adicionar três quadrados 3x3 em posições distintas
matriz[10:13, 10:13] = 255  # Quadrado 1
matriz[50:53, 70:73] = 255  # Quadrado 2
matriz[150:153, 120:123] = 255  # Quadrado 3

# Adicionar um retângulo 15x25
matriz[20:35, 30:55] = 255

# Adicionar um retângulo 10x5
matriz[100:110, 50:55] = 255

# Adicionar um retângulo 25x40
matriz[120:145, 160:200] = 255

matriz_uint8 = matriz.astype(np.uint8)
imagem = matriz_uint8
#imagem = cv2.imread(entrada)




print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))





###################
##### Aula 11: hit-or-miss: encontrar padrões
np.random.seed(0)

BW = histograma.BWimg(imagem, 150)


#utilizando uma matriz 3x3 preenchida com 1
matrizest =  np.full((3, 3), 1)
#mascara em cruz suaviza mais
mascara = np.array([[0, 0, 0, 0],
                    [0, 255, 0, 0],
                    [0, 0, 0, 0]])

#escolher qual matriz-máscara utilzar
primeiraerosao = histograma.erosao(BW, matrizest, 1)
complementoA = histograma.inverterBW(BW)
#estruturante que englobe matrizest
def englobar_matriz(B):
    N = B.shape[0]  # Tamanho da matriz B
    # Criar uma matriz de tamanho (N+2) x (N+2) preenchida com 1
    A = np.ones((N+2, N+2), dtype=int)
    # Substituir os valores de dentro por 0
    A[1:N+1, 1:N+1] = 0
    return A
c = englobar_matriz(matrizest)
#erosao de complemento A e C
segundaerosao = histograma.erosao(complementoA, c, 1)
intersecao = np.where((primeiraerosao == 255) & (segundaerosao == 255), 255, 0)
#transformar ponto no elemento estruturante

resultado = intersecao.copy()

coords = np.argwhere(intersecao == 255)

# Substituir o local correspondente na matriz de resultado com matrizest
for coord in coords:
    x, y = coord
    N = matrizest.shape[0] // 2
    # Redimensionar o resultado para incluir a matrizest inteira no ponto indicado
    resultado[x-N:x + matrizest.shape[0] - N, y-N:y + matrizest.shape[1]-N] = matrizest
resultado = np.where((resultado == 1), 255, 0)
resultado = resultado.astype(np.uint8)

cv2.imshow("imagem original", imagem)
cv2.imshow("imagem após primeira erosao", primeiraerosao)
cv2.imshow("imagem após segunda erosao", segundaerosao)
cv2.imshow("imagem apos complemento", complementoA)

#resultado = histograma.buscar_formas(BW, matrizest)
cv2.imshow("imagem apos operacao", resultado)
cv2.waitKey(0) 
