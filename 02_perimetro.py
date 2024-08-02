def calcular_perimetro(largura, comprimento):
    # Calcula o perímetro usando a fórmula 2 * (largura + comprimento)
    perimetro = 2 * (largura + comprimento)
    return perimetro

# Dimensões do terreno
largura_terreno = 10
comprimento_terreno = 30

# Calcula o perímetro do terreno
perimetro_terreno = calcular_perimetro(largura_terreno, comprimento_terreno)

# Exibe o resultado
print(f"O perímetro do terreno de {largura_terreno} x {comprimento_terreno} metros é: {perimetro_terreno} metros")
