area = int(input('Digite quantos m² deseja pintar: '))
cobertura = area / 3
latas = round(cobertura / 18 + 0.5)
valor = latas * 80
print(f'Para cobrir os {area}m² que deseja, você irá precisar de {latas} latas e irá custar R$ {valor:.2f}')