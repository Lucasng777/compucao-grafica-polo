from PIL import Image
import os
import re

# Diretório onde as imagens estão
images_dir = 'metades-recortadas'

# Lista para armazenar todas as imagens na ordem correta
all_images = []

# Número total de páginas (cada página tem 2 imagens: esquerda e direita)
num_pages = 30  # 64 imagens ÷ 2 = 32 páginas

# Função para extrair número da página e posição do nome do arquivo
def get_page_number_and_position(filename):
    match = re.match(r'pagina_enem_(\d+)_(esquerda|direita)\.png', filename)
    if match:
        return int(match.group(1)), match.group(2)
    return None, None

# Coletar todas as imagens
image_files = [f for f in os.listdir(images_dir) 
               if f.endswith('.png') and f.startswith('pagina_enem_')]

# Criar um dicionário para organizar as imagens por página e posição
page_dict = {}
for filename in image_files:
    page_num, position = get_page_number_and_position(filename)
    if page_num is not None:
        if page_num not in page_dict:
            page_dict[page_num] = {}
        page_dict[page_num][position] = filename

# Ordenar as páginas numericamente e para cada página, adicionar primeiro esquerda depois direita
for page_num in sorted(page_dict.keys()):
    page_data = page_dict[page_num]
    
    # Adicionar imagem esquerda (se existir)
    if 'esquerda' in page_data:
        img = Image.open(os.path.join(images_dir, page_data['esquerda']))
        all_images.append(img)
        print(f"Adicionada: página {page_num} - esquerda")
    
    # Adicionar imagem direita (se existir)
    if 'direita' in page_data:
        img = Image.open(os.path.join(images_dir, page_data['direita']))
        all_images.append(img)
        print(f"Adicionada: página {page_num} - direita")

# Calcular a largura máxima e a altura total
if all_images:
    max_width = max(img.width for img in all_images)
    total_height = sum(img.height for img in all_images)

    # Criar uma imagem muito longa
    long_image = Image.new('RGB', (max_width, total_height), (255, 255, 255))

    # Colar cada imagem uma abaixo da outra
    y_offset = 0
    for img in all_images:
        long_image.paste(img, (0, y_offset))
        y_offset += img.height

    # Salvar a imagem resultante
    long_image.save('enem_empilhado_ordenado.png')
    print(f"\nImagem combinada salva como 'enem_empilhado_ordenado.png'")
    print(f"Total de imagens processadas: {len(all_images)}")
    print(f"Largura máxima: {max_width}px")
    print(f"Altura total: {total_height}px")
else:
    print("Nenhuma imagem foi encontrada ou processada.")