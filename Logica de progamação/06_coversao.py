# entrada de dados
nome = input("Informe o seu nome: ")
idade = input("Informe sua idade: ")
altura = input("Informe sua altura: ").replace(",",".")

# conversão de tipo
idade = int(idade)
altura = float(altura)

# saída de dados
print(f"Nome: {nome}. Tipo: {type(nome)}")
print(f"Idade: {idade}. Tipo {type(idade)}")
print(f"altura: {altura} metros. Tipo: {type(altura)}")