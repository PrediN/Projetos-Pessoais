# Calculadora de frete QBello doces
# Autoral de Pedro Sanchez

from math import ceil

print('-=-'*20)
print(f"{'FRETES QBELLO DOCES':^60}")
print('-=-'*20)
print()

while True:
    # Inserção de variaveis
    etanol = float(input('Insira o valor do litro do álcool: R$'))
    kmlitro = float(input('Quantos km/L o carro faz? '))
    distancia = float(input('Quantos km para a entrega? '))
    print()

    # Calculos de frete
    disTotal = distancia*2
    etaUsado = disTotal/kmlitro
    frete = ceil((etaUsado*etanol)*1.2)

    # Impressão de resultados
    print('-=-'*20)
    print(f"{'VALORES DE FRETE':^60}")
    print(f"{'-'*30:^60}")
    print(f"{'DISTÂNCIA CLIENTE    \033[31m{:.1f}\033[mkm'.format(disTotal):^70}")
    print(f"{'ETANOL USADO         \033[31m{:.1F}\033[mL'.format(etaUsado):^70}")
    print(f"{'-'*30:^60}")
    print(f"{'VALOR FRETE         R$\033[31m{:.2F}\033[m'.format(frete):^70}")
    print('-=-'*20)
    print()
    
    # Verificação para fechar programa
    continuar = input('Deseja calcular outro frete? (s/n): ').strip().lower()
    print()
    if continuar == 'n':
        break