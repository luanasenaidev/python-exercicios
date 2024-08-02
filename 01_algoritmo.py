def coletar_informacoes():
    # Coleta as informações do usuário
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura (em metros): "))
    peso = float(input("Digite seu peso (em kg): "))
    cidade = input("Digite sua cidade: ")
    
    # Exibe as informações coletadas
    print("\nInformações do Usuário:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Altura: {altura} metros")
    print(f"Peso: {peso} kg")
    print(f"Cidade: {cidade}")

# Chama a função para coletar e exibir as informações
coletar_informacoes()
