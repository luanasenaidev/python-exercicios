def converter_dolar_para_euro(valor_em_dolar, taxa_de_conversao):
    # Converte o valor de dólar para euro usando a taxa de conversão
    valor_em_euro = valor_em_dolar * taxa_de_conversao
    return valor_em_euro

# Solicita o valor em dólares do usuário
valor_em_dolar = float(input("Digite o valor em dólares: "))

# Define a taxa de conversão 
taxa_de_conversao = 0.85

# Converte o valor para euros
valor_em_euro = converter_dolar_para_euro(valor_em_dolar, taxa_de_conversao)

# Exibe o resultado
print(f"{valor_em_dolar} dólares é equivalente a {valor_em_euro:.2f} euros")
