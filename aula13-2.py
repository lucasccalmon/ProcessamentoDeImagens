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
entrada = 'jbase.png'
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
matrix = matrix = np.array([
    [255, 255, 255, 255, 0, 0, 0],
    [255, 255, 255, 255, 0, 0, 0],
    [255, 255, 255, 255, 0, 0, 0],
    [255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255]
])
#se usar a matriz:
#matriz_uint8 = matrix.astype(np.uint8)
#imagem = matriz_uint8
#BW = histograma.BWimg(imagem, 150)

def esqueletizacao(imagem, estruturante):
    k = 1
    esqueleto = np.zeros(
        (imagem.shape[0], imagem.shape[1]),
        dtype=imagem.dtype,
    ) # Inicializa matriz do mesmo tamanho com zeros
    abertura_inicial = histograma.abertura(imagem, estruturante, 1)
    diferenca_inicial = imagem - abertura_inicial
    esqueleto = diferenca_inicial
    while True:
        # Chama a função erosao e atribui o valor de retorno à erosao_k
        erosao_k = histograma.erosao(imagem, estruturante, k)  # A ⊖ kB
        print(f"Erosão (k={k}):\n", erosao_k)  # Depuração: visualize a erosão
        
        abertura_k = histograma.abertura(erosao_k, estruturante, 1)  # (A ⊖ kB) ∘ B
        print(f"Abertura (k={k}):\n", abertura_k)  # Depuração: visualize a abertura
        
        diferenca_k = erosao_k - abertura_k  # A ⊖ kB - ((A ⊖ kB) ∘ B)
        print(f"Diferença (k={k}):\n", diferenca_k)  # Depuração: visualize a abertura
        
        esqueleto = np.maximum(esqueleto, diferenca_k)  # União das diferenças
        
        if np.all(abertura_k == 0):  # Condição de parada
            break
        
        k += 1
    
    return esqueleto

esqueleto = esqueletizacao(BW, mascara)
inversao = histograma.inverterBW(BW)
sobrepor = np.maximum(esqueleto, inversao) 

print("Matriz inicial:\n", imagem)
print("Matriz final esqueletica:\n", esqueleto)

cv2.imshow("imagem original", imagem)
cv2.imshow("imagem esqueletica", esqueleto)
cv2.imshow("imagem final", sobrepor)
cv2.waitKey(0) 