peso = float(input('Digite o peso do peixe que você pescou: '))
pesoL = 50
multa = (peso - pesoL) * 4
excesso =(peso - pesoL)
if peso > pesoL:
    print(f'O peso limite ultrapassou {excesso}kg e você terá que pagar R${multa:.2f}')

else:
    print('Você não terá multa')