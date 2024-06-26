import math

area = int(input('Digite quantos m² deseja pintar: '))
litros = (area / 6) * 1.1
latas = math.ceil(litros / 18)
valorLA = latas * 80
galao =  math.ceil(litros / 3.6)
valorGA = galao * 25

mixlatas = round(litros / 18)
mixgaloes = round((litros - mixlatas * 18) / 3.6)

if ((litros - (mixlatas * 18)% 3.6 != 0)):
    mixgaloes +=1
    totalMix = (mixlatas * 80) + (mixgaloes * 25)
    
print(f'Se for comprar só latas de 18 litros irá precisar de {latas} lata(s) e irá custar R$ {valorLA:.2f}')
print(f'Se for comprar só galões de 3,6 litros irá precisar de {galao} galão(ões) e irá custar R$ {valorGA:.2f}')
print(f'Se deseja mesclar latas e galões para dar o que precisar realmente será necessario {mixlatas} lata(s)'
      f'e {mixgaloes} galão(ões) e irá custar R${totalMix:.2f}')