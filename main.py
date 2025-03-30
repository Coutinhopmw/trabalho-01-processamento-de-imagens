import cv2

# Carregar a imagem
imagem = cv2.imread('curiosidades-sobre-leao2.jpg')

# Redimensionar a imagem
imagem_redimensionada = cv2.resize(imagem, (300, 300))

# Converter para escala de cinza
imagem_cinza = cv2.cvtColor(imagem_redimensionada, cv2.COLOR_BGR2GRAY)

# Exibir a imagem
cv2.imshow('Imagem em Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
