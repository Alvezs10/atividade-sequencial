genero = input('Informe seu genero, (h) para homens e (m) para mulheres: ')
altura = float(input('Digite sua altura: '))

if genero =='h':
    pesoIh = (72.7*altura)-58
    print(f'Já que sua altura é {altura:.2f}cm seu peso ideal sera: {pesoIh}')


else:
    pesoIm = (62.1*altura)-44.7
    print(f'Já que sua altura é {altura:.2f}cm seu peso ideal sera: {pesoIm:.1f}')





