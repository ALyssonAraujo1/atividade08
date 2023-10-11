from time import sleep
valor = float(input("digite o valor do produto:"))
sleep(1)
desconto = (input("insira o valor do desconto em %"))
valornovo = float(valor - desconto )
print(valornovo)