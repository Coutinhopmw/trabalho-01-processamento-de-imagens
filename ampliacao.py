import cv2
import numpy as np

def interpolacao_bilinear_ampliacao(imagem, escala):
    altura_original, largura_original = imagem.shape
    nova_altura = int(altura_original * escala)
    nova_largura = int(largura_original * escala)

    imagem_ampliada = np.zeros((nova_altura, nova_largura), dtype=np.uint8)

    for y in range(nova_altura):
        for x in range(nova_largura):
            # Mapeia a posição do pixel na imagem original
            x_original = x / escala
            y_original = y / escala

            # Pega os pixels vizinhos
            x0 = int(np.floor(x_original))
            x1 = min(x0 + 1, largura_original - 1)
            y0 = int(np.floor(y_original))
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
            imagem_ampliada[y, x] = int(p1 + p2 + p3 + p4)

    return imagem_ampliada

# Carregar a imagem em escala de cinza
# imagem = cv2.imread("img1.jpeg", cv2.IMREAD_GRAYSCALE)
imagem = cv2.imread("img2.jpg", cv2.IMREAD_GRAYSCALE)

# Definir fator de ampliação (ex: 2.0 para dobrar o tamanho)
escala = 5.0
imagem_ampliada = interpolacao_bilinear_ampliacao(imagem, escala)

# Mostrar e salvar a imagem ampliada
cv2.imshow("Imagem Ampliada", imagem_ampliada)
cv2.imwrite("imagem_ampliada.jpg", imagem_ampliada)
cv2.waitKey(0)
cv2.destroyAllWindows()
