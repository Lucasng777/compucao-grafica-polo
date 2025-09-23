from PIL import Image
import os

# Pasta onde as imagens estão
pasta = "metades-recortadas"

# Lista para armazenar todas as imagens na ordem correta
todas_imagens = []

# Para cada página de 29 a 32
for i in range(29, 33):
    # Primeiro a metade esquerda
    esquerda_path = os.path.join(pasta, f"pagina_enem_{i}_esquerda.png")
    if os.path.exists(esquerda_path):
        img_esquerda = Image.open(esquerda_path)
        todas_imagens.append(img_esquerda)
        print(f"Adicionada: pagina_enem_{i}_esquerda.png")
    else:
        print(f"Aviso: {esquerda_path} não encontrada")
    
    # Depois a metade direita
    direita_path = os.path.join(pasta, f"pagina_enem_{i}_direita.png")
    if os.path.exists(direita_path):
        img_direita = Image.open(direita_path)
        todas_imagens.append(img_direita)
        print(f"Adicionada: pagina_enem_{i}_direita.png")
    else:
        print(f"Aviso: {direita_path} não encontrada")

# Se encontrou imagens
if todas_imagens:
    # Calcula dimensões da imagem final
    largura_max = max(img.width for img in todas_imagens)
    altura_total = sum(img.height for img in todas_imagens)
    
    # Cria imagem final com fundo branco
    imagem_final = Image.new('RGB', (largura_max, altura_total), color='white')
    
    # Cola cada imagem uma abaixo da outra
    y = 0
    for img in todas_imagens:
        # Centraliza horizontalmente se necessário
        x_offset = (largura_max - img.width) // 2
        imagem_final.paste(img, (x_offset, y))
        y += img.height
    
    # Salva o resultado
    imagem_final.save("todas_metades_29_a_32_vertical.png")
    print("Imagem final salva como 'todas_metades_29_a_32_vertical.png'")
    print(f"Total de {len(todas_imagens)} imagens combinadas")
else:
    print("Nenhuma imagem foi encontrda")