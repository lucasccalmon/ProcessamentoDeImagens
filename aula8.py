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
entrada = 'bolas.png'
#entrada = 'fluminense.png'
import cv2
import numpy as np
import matplotlib.pyplot as plt
import histograma


imagem = cv2.imread(entrada)


#transformando imagem colorida em tons de cinza
canalCinza = histograma.CanalCinza(imagem)



print('tamanho esperado:', (imagem.shape[1] * imagem.shape[0]))





###################
##### Aula 8: transformar imagem em preto e branco e fazer erosão
np.random.seed(0)

histo = histograma.hist(canalCinza, 'a')
histograma.plotarGrafico(histo, 'grey')
BW = histograma.BWimg(canalCinza, 150)

               
def erosao(imagem, estruturante, n):  # n = número de repetições
    while n > 0:
        # Adicionar bordas à imagem
        tamanho_estruturante = estruturante.shape[0]
        borda = (tamanho_estruturante - 1) // 2
        imagem_com_bordas = np.zeros(
            (imagem.shape[0] + 2 * borda, imagem.shape[1] + 2 * borda),
            dtype=imagem.dtype,
        )
        imagem_com_bordas[borda:-borda, borda:-borda] = imagem
        
        # Obter dimensões
        altura_imagem, largura_imagem = imagem_com_bordas.shape
        altura_estruturante, largura_estruturante = estruturante.shape
        
        # Matriz de saída
        imagem_erodida = np.zeros((altura_imagem - 2 * borda, largura_imagem - 2 * borda), dtype=np.uint8)
        
        # Aplicar a operação de erosão
        for i in range(altura_imagem - 2 * borda):
            for j in range(largura_imagem - 2 * borda):
                # Extrair submatriz
                submatriz = imagem_com_bordas[i:i + altura_estruturante, j:j + largura_estruturante]
                
                # Verificar se o estruturante encaixa perfeitamente
                if np.all(submatriz[estruturante == 1] == 255):  # Checa o "fit"
                    imagem_erodida[i, j] = 255  # "Fit"
                else:
                    imagem_erodida[i, j] = 0  # Não encaixa

        # Atualizar imagem para a próxima iteração
        imagem = imagem_erodida.copy()
        n -= 1

    return imagem_erodida

#utilizando uma matriz 3x3 preenchida com 1
matrizest = matriz = np.full((3, 3), 1)
#mascara em cruz suaviza mais
mascara = np.array([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]])
#escolher qual matriz-máscara utilzar

erodida = erosao(BW, mascara, 5)
print('tamanho da img orig: ', BW.shape)
print('tamanho da img erod: ', erodida.shape)

cv2.imshow("imagem em tons de cinza", canalCinza)
cv2.imshow("imagem em preto e branco", BW)
cv2.imshow("imagem erodida", erodida)
cv2.waitKey(0) 
