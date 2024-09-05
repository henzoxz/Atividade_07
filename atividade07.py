# Enunciado: Uma loja aplica um imposto de 12% sobre o valor dos produtos. Crie um programa que receba o preço de um produto e calcule o preço final com o imposto incluído.
preco = int(input(" Digite o Preço do Produto "))
imposto = 0.12*preco+preco

print (" Valor Final:" , imposto)
