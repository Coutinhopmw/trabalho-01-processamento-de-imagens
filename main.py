import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('capivara.jpeg')

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

print("Matriz da imagem:")
print(imagem)

# altura, largura = imagem.shape
# print(f"Dimensões: {altura}x{largura}")

# Exibir a imagem
cv2.imshow('Imagem em Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
