from PIL import Image
import os

pasta_imagens = "metades"
pasta_saida = "metades-recortadas"

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith(".png"):
        caminho_entrada = os.path.join(pasta_imagens, nome_arquivo)
        imagem = Image.open(caminho_entrada)

        largura, altura = imagem.size

        # Verifica se o nome do arquivo termina com "direita.png" ou "esquerda.png"
        if nome_arquivo.lower().endswith("direita.png"):
            # Se for "direita.png", cortamos 25 pixels da esquerda
            caixa_corte = (25, 0, largura, altura)
        elif nome_arquivo.lower().endswith("esquerda.png"):
            # Se for "esquerda.png", cortamos 25 pixels da direita
            caixa_corte = (0, 0, largura - 25, altura )
        else:
            # Para os outros casos, mantém o corte original
            caixa_corte = (276, 390, largura - 276, altura - 280)

        imagem_cortada = imagem.crop(caixa_corte)

        caminho_saida = os.path.join(pasta_saida, nome_arquivo)
        imagem_cortada.save(caminho_saida)

print("Recorte das bordas concluído.")
