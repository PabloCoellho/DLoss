arquivo_pts1 = 'pts1.txt'
arquivo_pts2 = 'pts2.txt'

# Ler arquivos removendo quebras de linha e espaços extras
with open(arquivo_pts1, 'r', encoding='utf-8') as f:
    pts1 = {linha.strip() for linha in f if linha.strip()}

with open(arquivo_pts2, 'r', encoding='utf-8') as f:
    pts2 = {linha.strip() for linha in f if linha.strip()}

# Encontrar elementos repetidos
pts_repetidos = pts1 & pts2  # Interseção dos conjuntos

# Exibir resultados
print("\nProntuários que estão repetidos:")
print("_________________________________________")
print('\n'.join(pts_repetidos))
print("_________________________________________")