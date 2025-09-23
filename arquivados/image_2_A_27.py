import os
from PIL import Image

def concatenar_imagens_verticalmente():
    # Configurações
    pasta = "metades-recortadas"
    arquivos_para_concatenar = []
    
    # Gerar lista de arquivos da página 2_direita até 27_esquerda
    for i in range(2, 28):  # De 2 a 27
        arquivos_para_concatenar.append(f"pagina_enem_{i}_direita.png")
        arquivos_para_concatenar.append(f"pagina_enem_{i}_esquerda.png")
    
    # Filtrar apenas arquivos que existem
    imagens_validas = []
    largura_maxima = 0
    altura_total = 0
    
    print("Verificando arquivos...")
    for arquivo in arquivos_para_concatenar:
        caminho_arquivo = os.path.join(pasta, arquivo)
        
        if os.path.exists(caminho_arquivo):
            try:
                img = Image.open(caminho_arquivo)
                imagens_validas.append((arquivo, img))
                largura_maxima = max(largura_maxima, img.width)
                altura_total += img.height
                print(f"✓ {arquivo} - {img.width}x{img.height}")
            except Exception as e:
                print(f"✗ Erro ao abrir {arquivo}: {e}")
        else:
            print(f"⚠ Arquivo não encontrado: {arquivo}")
    
    if not imagens_validas:
        print("❌ Nenhuma imagem válida encontrada")
        return
    
    # Criar imagem final
    print(f"\nCriando imagem final: {largura_maxima}x{altura_total}")
    imagem_final = Image.new('RGB', (largura_maxima, altura_total), (255, 255, 255))
    
    # Colar imagens verticalmente
    y_offset = 0
    for nome_arquivo, img in imagens_validas:
        # Centralizar horizontalmente se necessário
        x_offset = (largura_maxima - img.width) // 2
        imagem_final.paste(img, (x_offset, y_offset))
        y_offset += img.height
        print(f"✓ {nome_arquivo} adicionado")
    
    # Salvar imagem final
    nome_saida = "enem_concatenado_paginas_2a27.png"
    imagem_final.save(nome_saida, format='PNG', quality=95)
    print(f"\n✅ Concatenação concluída! Imagem salva como: {nome_saida}")
    print(f"📏 Dimensões finais: {imagem_final.width}x{imagem_final.height}")

# Executar a função
if __name__ == "__main__":
    concatenar_imagens_verticalmente()