mb = int(input('Informe o tamanho do arquivo em MB que deseja fazer download: '))
link = int (input('Informe a velocidade do seu link em Mbps: '))
tempo = (mb / (link / 8)) / 60

print(f'Para efetuar um donwload de {mb} MB com a velocidade {link} Mbps, irá demorar {tempo:.0f} minutos.')