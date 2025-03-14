'''saldo = 5000
print(f"O sau saldo atual é {saldo}")

saque = float(input("Digite o valor do saque:"))

if saque <= saldo:
    print("Saque realizado!")

if saque > saldo:
    print("Saldo insuficiente!")
'''

#Usando elif

MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Digite a sua idade:"))

if idade >= MAIOR_IDADE:
    print("Você está apto para fazer a carta de condução")
elif idade >= IDADE_ESPECIAL and idade < MAIOR_IDADE:
    print("Apenas pode fazer aulas teoricas!" )
else:
    print("Infelizmente ainda não posivel fazer aulas de condução.")