totalCarros = int(input('Digite o número de carros vendidos: '))
valorTotal = int(input('Digite o valor total de carros vendidos: '))
salario = int(input('Digite o sálario fixo: '))
valorVendido = int(input('Digite o valor recebido por carro vendido: '))

print('Salário final R$ ', str(salario+(valorVendido*totalCarros)+0.05*valorTotal).replace('.',','))
