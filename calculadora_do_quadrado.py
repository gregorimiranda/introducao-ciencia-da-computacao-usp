# Exercício 1
# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
# Observação: a saída deve estar no formato: "perímetro: x - área: y"
# Abaixo um exemplo de como devem ser a entrada e saída de dados do programa:

# Exemplo:
# Entrada de Dados: 
# Digite o valor correspondente ao lado de um quadrado: 3
# Saída de Dados:
# perímetro: 12 - área: 9

# Dica: lembre-se que um quadrado tem quatro lados iguais, logo só é necessário pedir o lado uma vez

valor_lado = float(input("Digite o valor correspondente ao lado de um quadrado"))
perimetro_quadrado = valor_lado * 4
area_quadrado = valor_lado ** 2 

print("perímetro:",perimetro_quadrado,"- área:",area_quadrado)

