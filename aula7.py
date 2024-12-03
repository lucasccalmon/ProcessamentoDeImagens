# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:48:46 2024

@author: aluno
"""
#entrada = 'entrada.jfif'
entrada = 'taj.jfif'
#entrada = 'pisaa.jfif'
#entrada = 'alpes.jpg'
#entrada = 'arrozfeijao.png'
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
##### Aula 7: convolução
np.random.seed(0)




def borda_convolucao(imagem, mascara, n): #n = n de repetições na convolucao
    while(n>0):
        
        #adicionar borda:
        tamanho_matriz = mascara.shape[0]
        borda = (tamanho_matriz - 1) // 2
        #bordas devem ser +2 em matriz 3x3 e + 4 em matriz 5x5 (ou seja, sempre aumenta em 2 o valor)
        imagem_com_bordas = np.zeros((imagem.shape[0] + 2 * borda, imagem.shape[1] + 2 * borda), dtype=canalCinza.dtype)
        #deve ser -1 em matriz 3x3 e -2 em matriz 5x5 (ou seja, sempre diminui em 1 o valor)
        imagem_com_bordas[borda:-borda, borda:-borda] = imagem
        # Obter as dimensões da imagem e da máscara
        imagem_altura, imagem_largura = imagem_com_bordas.shape
        mascara_altura, mascara_largura = mascara.shape
        
        # Calcular as dimensões da saída
        altura_saida = imagem_altura - (mascara_altura - 1)
        largura_saida = imagem_largura - (mascara_largura - 1)
        
        # Matriz de saída
        imagem_convoluida = np.zeros((altura_saida, largura_saida))  
    
    
        for i in range(altura_saida):
            for j in range(largura_saida):
                # Extrair a submatriz da imagem que corresponde à máscara
                submatriz = imagem_com_bordas[i:i + mascara_altura, j:j + mascara_largura]
                
                # Aplicar a máscara (multiplicação elemento a elemento e soma dos resultados)
                resultado = np.sum(submatriz * mascara)
                
                # Garantir que o resultado não seja negativo
                if resultado < 0:
                    resultado = 0
                
                imagem_convoluida[i, j] = resultado
    
        # Converter para uint8 após a convolução
        imagem_convoluida = imagem_convoluida.astype(np.uint8) 
        imagem = imagem_convoluida.copy()
        n = n-1
    return imagem_com_bordas, imagem_convoluida

#mascara 5x5
matriz = np.full((5, 5), 1/5*5)
#mascara 3x3
mascara = np.array([[0, 1, 0],
                    [1, -4, 1],
                    [0, 1, 0]])
#escolher qual matriz-máscara utilzar
bordas, resultado = borda_convolucao(canalCinza, matriz, 2)

# Exibir os resultados
print("Imagem Original:")
print(canalCinza)

print("\nMáscara 3x3:")
print(mascara)

print("\nResultado da Convolução:")
print(resultado)

print('tamanho da img orig: ', canalCinza.shape)
print('tamanho da img com bordas: ', bordas.shape)
print('tamanho da img convol: ', resultado.shape)


cv2.imshow("imagem original", canalCinza )
cv2.imshow("imagem com bordas", bordas)
cv2.imshow("imagem convolucionada", resultado)
#cv2.imshow("imagem expandida", img_expandida) #bom para usar com a imagem de neve
cv2.waitKey(0) 