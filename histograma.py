# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 16:41:02 2024

@author: 19123556714
"""

import numpy as np
import matplotlib.pyplot as plt

#transformar uma imagem em tons de cinza
def CanalCinza(imagem):
    canalCinza = np.zeros((imagem.shape[0], imagem.shape[1]), dtype= np.uint8)
    for linha in range (imagem.shape[0]):
            for coluna in range (imagem.shape[1] ):
                canalCinza[linha, coluna] = (imagem[linha, coluna].sum()//3)
    return canalCinza

#gerar histograma de um canal de imagem
def hist(imagem, canal):
    histograma = np.zeros(256, dtype=np.uint)
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] += 1
    return histograma


#plotar um gráfico para o histograma
def plotarGrafico(imagem, cor):
    X = [0] * 256
    for i in range(256):
        X[i] = i
    plt.xlabel('Pixel')
    plt.ylabel('Quantidade')
    plt.title('Histograma da Imagem em Tons da cor do gráfico')
    plt.bar(X, imagem, color=cor)
    plt.show()
    
#transformar uma imagem em tons de cinza em uma imagem branca e uma preta
def BrancoPreto(imagemCinza, corte):
    corBranca = imagemCinza.copy()
    corPreta = imagemCinza.copy()
    for i in range(corBranca.shape[0]):
        for j in range(corBranca.shape[1]):
            if  corBranca[i][j] < corte:
               corBranca[i][j] = 255
               
    for i in range(corPreta.shape[0]):
        for j in range(corPreta.shape[1]):
            if  corPreta[i][j] > corte:
                corPreta[i][j] = 255
                
    return corBranca, corPreta

#retornar uma imagem de canalCinza em imagem em preto e branco
def BWimg(imagemCinza, corte):
    BWimg = imagemCinza.copy()
    for i in range(BWimg.shape[0]):
        for j in range(BWimg.shape[1]):
            if  BWimg[i][j] < corte:
               BWimg[i][j] = 0
            if  BWimg[i][j] >= corte:
               BWimg[i][j] = 255
    return BWimg

#alterar imagem com curva de tom - contraste ou luminosidade
def curvaTom(imagem, c, l):
    imagem = imagem.astype(np.float32)
    toned_image = c * imagem + l
    toned_image = np.clip(toned_image, 0, 255)
    toned_image = toned_image.astype(np.uint8)
    plotCurvaTom(c,l)   
    return toned_image           

#transformar imagem no negativo
def curvaTomNeg(imagem, c, l):
    imagem = imagem.astype(np.float32)
    imagem = 255 - imagem
    toned_image = c * imagem + l
    toned_image = np.clip(toned_image, 0, 255)
    toned_image = toned_image.astype(np.uint8)
    plotCurvaTomNeg(c,l)   
    return toned_image    

#gerar grafico da curva de tom
def plotCurvaTom(c, l):
    r = np.linspace(0, 255, 256)
    tone_curve = c*r+l
    tone_curve = np.clip(tone_curve, 0, 255)
    plt.figure(figsize=(8,6))
    plt.plot(r, tone_curve, color='blue', label=f'c= {c}, l = {l}')
    plt.xlabel('origem r')
    plt.ylabel('ajustado cr +l')
    plt.title('curva de tom')
    plt.legend()
    plt.grid()
    plt.show()
   
   #gerar grafico da curva de tom negativa
def plotCurvaTomNeg(c, l):
    r = np.linspace(0, 255, 256)
    r_neg = 255 - r
    tone_curven = c*r_neg+l
    tone_curven = np.clip(tone_curven, 0, 255)
    plt.figure(figsize=(8,6))
    plt.plot(r, tone_curven, color='blue', label=f'c= {c}, l = {l} (Negativo)')
    plt.xlabel('origem r')
    plt.ylabel('ajustado cr +l')
    plt.title('curva de tom negativa')
    plt.legend()
    plt.grid()
    plt.show()

#expandir uma imagem de baixo contraste (enviar uma img em tons de cinza)
def expansaohist(img,r1,r2):
    expansao = img.copy()
    for i in range(expansao.shape[0]):
        for j in range(expansao.shape[1]):
            if expansao[i][j] >= r2:
                expansao[i][j] = 255
            if expansao[i][j] <= r1:
                expansao[i][j] = 0
            if r1 < expansao[i][j] < r2:
                expansao[i][j] = 255 *((expansao[i][j] - r1)/(r2-r1))
    return expansao
    
#gerar histograma original, histograma normalizado e histograma acumulado
def histogramaplus(imagem):
    histograma = np.zeros(256, dtype=np.uint)
    for i in range(imagem.shape[0]):
        for j in range(imagem.shape[1]):
            histograma[imagem[i][j]] += 1
    
    total_pixels = imagem.shape[0] * imagem.shape[1]
    
    # Histograma normalizado
    histograma_normalizado = histograma / total_pixels
    
    #histograma normalizado, somatorio das probabilidades (acumulado normalizado)
    
    # Histograma acumulado normalizado 
    histograma_acumulado = np.zeros(256)
    acumulado = 0.0
    for i in range(256):
        acumulado += histograma_normalizado[i]
        histograma_acumulado[i] = acumulado
    print('acumulado', acumulado)
    
    return histograma, histograma_normalizado, histograma_acumulado
    
def normalizados(histacumulado,imagem):
    niveis_normalizados = np.round(histacumulado * 255).astype(np.uint8)
  
  # Aplicar o mapeamento para cada pixel da imagem
  #a linha abaixo utiliza indexação, muito pratico
    #imagem_normalizada = niveis_normalizados[imagem]
    
    
    #o codigo abaixo faz a indexação manualmente
    imagem_normalizada = np.zeros_like(imagem)
    for i in range(imagem.shape[0]):
       for j in range(imagem.shape[1]):
           imagem_normalizada[i][j] = niveis_normalizados[imagem[i][j]]
    return niveis_normalizados, imagem_normalizada #histogramaualizado

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

def dilatacao(imagem, estruturante, n):  # n = número de repetições
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
        imagem_dilatada = np.zeros((altura_imagem - 2 * borda, largura_imagem - 2 * borda), dtype=np.uint8)
        
        # Aplicar a operação de erosão
        for i in range(altura_imagem - 2 * borda):
            for j in range(largura_imagem - 2 * borda):
                # Extrair submatriz
                submatriz = imagem_com_bordas[i:i + altura_estruturante, j:j + largura_estruturante]
                
                # Verificar se o estruturante encaixa perfeitamente
                if np.any(submatriz[estruturante == 1] == 255):  # Checa o "hit"
                    imagem_dilatada[i, j] = 255  # "Hit"
                else:
                    imagem_dilatada[i, j] = 0  # Não encaixa

        # Atualizar imagem para a próxima iteração
        imagem = imagem_dilatada.copy()
        n -= 1

    return imagem_dilatada
