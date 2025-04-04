import cv2
import numpy as np

def interpolacao_bilinear(imagem, escala):
    altura_original, largura_original = imagem.shape
    nova_altura = int(altura_original * escala)
    nova_largura = int(largura_original * escala)
    
    imagem_redimensionada = np.zeros((nova_altura, nova_largura), dtype=np.uint8)
    
    for y in range(nova_altura):
        for x in range(nova_largura):
            # Mapeia a posição do pixel na imagem original
            x_original = x / escala
            y_original = y / escala

            # Pega os pixels vizinhos
            x0 = int(x_original)
            x1 = min(x0 + 1, largura_original - 1)
            y0 = int(y_original)
            y1 = min(y0 + 1, altura_original - 1)

            # Calcula os pesos
            dx = x_original - x0
            dy = y_original - y0

            # Obtém os valores dos pixels vizinhos
            p1 = imagem[y0, x0] * (1 - dx) * (1 - dy)
            p2 = imagem[y0, x1] * dx * (1 - dy)
            p3 = imagem[y1, x0] * (1 - dx) * dy
            p4 = imagem[y1, x1] * dx * dy

            # Calcula o valor do pixel interpolado
            imagem_redimensionada[y, x] = int(p1 + p2 + p3 + p4)

    return imagem_redimensionada

# Carregar a imagem em escala de cinza
# imagem = cv2.imread("img1.jpeg", cv2.IMREAD_GRAYSCALE)
imagem = cv2.imread("img2.jpg", cv2.IMREAD_GRAYSCALE)

# Definir fator de redução (ex: 0.5 para reduzir pela metade)
escala = 0.04
imagem_reduzida = interpolacao_bilinear(imagem, escala)

# Mostrar e salvar a imagem reduzida
cv2.imshow("Imagem Reduzida", imagem_reduzida)
cv2.imwrite("imagem_reduzida.jpg", imagem_reduzida)
cv2.waitKey(0)
cv2.destroyAllWindows()
