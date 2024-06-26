ganhaH = float(input('Digite o quanto você ganha por hora: '))
horasT = float(input('Horas trabalhadas por mês: '))
salarioB = horasT * ganhaH
ir = salarioB * (11/100)
inss = salarioB * (8/100)
sindicato = salarioB * (5/100)
salarioLiquido = salarioB - ir - inss - sindicato 
print(f'+ Salário Bruto:   R${salarioB:.2f}''\n'
      f'- IR (11%):        R${ir:.2f}''\n'
      f'- INSS (8%):       R${inss:.2f}''\n'
      f'- Sindicato(5%0:   R${sindicato:.2f}''\n'
      f'= Salário Líquido: R${salarioLiquido:.2f}')