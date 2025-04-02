import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('curiosidades-sobre-leao2.jpg')

# Verificar se a imagem foi carregada corretamente
if imagem is None:
    print("Erro ao carregar a imagem!")
    exit()

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

print("Matriz da imagem em escala de cinza:")
print(imagem_cinza)

# Obter as dimensões da imagem corretamente
altura, largura = imagem_cinza.shape  # Agora a imagem tem apenas 2 dimensões
print(f"Dimensões: {altura}x{largura}")

# Acessar um pixel específico (por exemplo, na posição x=50, y=100)
x, y = 50, 100
valor_pixel = imagem_cinza[y, x]  # Agora acessamos na matriz em escala de cinza
print(f"Valor do pixel em ({x}, {y}): {valor_pixel}")

# Exibir a imagem em escala de cinza
cv2.imshow('Imagem em Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
