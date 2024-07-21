#LISTA 1 da disciplina introdução à programação

#Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print("Olá mundo")

#1.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
x= int(input("digite um número:"))
print('o número informado foi',x)

#2.Faça um Programa que peça dois números e imprima a soma.
x=int(input('digite um número: '))
y=int(input("digite um número; "))
soma= x + y
print(soma)

#3.Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1=int(input('digite a primeira nota: '))
nota2=int(input('digite a segunda nota: '))
nota3=int(input('digite a terceira nota: '))
nota4=int(input("digite a quarta nota: "))
media= nota1+nota2+nota3+nota4/4
print(media)

#4.Faça um Programa que converta metros para centímetros.
metros=int(input('digite sua medidada em metros: '))
cent=metros*100
print(cent, "cm")

#5.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
math.pi
raio=int(input('digite o raio do círculo: '))
area=2*math.pi*raio**2
print(area,'u.a')

#6.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado=int(input('digite o lado do quadrado '))
area=lado**2
print(area,'u.a')
area2=2*area
print(area2,'u.a')

#7.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 
ganho=int(input("digite o valor que você ganha por hora: "))
trabalho=int(input('digite a quantidade de horas que você trabalha: '))
pagamento=ganho*trabalho*20
print(pagamento,"reais")

#8.Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#•C = 5 * ((F-32) / 9).
temp=int(input('digite o valor da temperatura em fahrenheit'))
C=5*((temp-32)/9)
print(C)

#9.Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temp=float(input('digite o valor da temperatura em celsius'))
F=((temp*9)/5)+32
print(F)

#10.Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#•o produto do dobro do primeiro com metade do segundo .
#•a soma do triplo do primeiro com o terceiro.
#•o terceiro elevado ao cubo.
num1=int(input('digite um número inteiro: '))
num2=int(input('digite um número inteiro: '))
num3=float(input('digite um número real: '))

r1=(2*num1)*(num2/2)
print(r1)
r2=(3*num1)+num3
print(r2)
r3=num3**3
print(r3)

#11.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
h=float(input('digite sua altura: '))
peso=(72.7*h)-58
print("seu peso ideal é ",peso)

#12.Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#•Para homens: (72.7*h) - 58
#•Para mulheres: (62.1*h) - 44.7
h=float(input('digite sua altura por favor: '))
sexo=int(input('digite 1 para sexo masculio , digite 2 para sexo femino: '))
if sexo == 1 :
  peso=(72.7*h)-58
  print(peso)
if sexo ==2 :
  peso2=(62.1*h)-44.7
  print(peso2)

#13.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
pesop =int(input('digite a quantidade de quilograma de peixe pescado: '))
if pesop>50:
  excesso=pesop-50
  valor=excesso*4
  print('voce de pagar de multa ',valor,"reais")

#14.Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#•salário bruto.
#•quanto pagou ao INSS.
#•quanto pagou ao sindicato.
#•o salário líquido.
#•calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
ganho=int(input("digite o valor que você ganha por hora: "))
trabalho=int(input('digite a quantidade de horas que você trabalha: '))
dias=int(input('digite quantos dias você trabalhou no mês: ' ))
print("---"*20)
bruto=ganho*trabalho*dias
print(bruto,"reais")
print('=-'*20)
ir=(bruto*11)/100
print("você paga de imposto de renda",ir,'reais')
print('=-'*20)
inss=(bruto*8)/100
print('você paga de INSS',inss,'reais')
print('=-'*20)
sd=(bruto*5)/100
print('você paga ao sindicato',sd,"reais")
print('=-'*20)
liq=bruto-ir-inss-sd
print('seu salário líquido é',liq,'reais')
print('---'*20)

#15.Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area=int(input('quantos m² deseja pintar? '))
qntl=area/54
qntlv=round(qntl+0.5)
if qntl==int(qntl):
  total=qntl*80
  print("---"*20)
  print('você deve comprar',qntl,"latas")
  print('que sai por',int(total),"reais")
  print('---'*20)
print('---'*20)
total=qntlv*80
print('você deve comprar',qntlv,"latas")
print('que sai por',int(total),'reais')
print('---'*20)

#16.Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#•Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#•comprar apenas latas de 18 litros;
#•comprar apenas galões de 3,6 litros;
#•misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
area=int(input('quantos m² deseja pintar? '))
qntl=area/108
qntlv=round(qntl+0.5)
total=qntlv*80
print("---"*20)
print('você deve comprar',qntlv,"latas")
print('que sai por',int(total),"reais")
print('---'*20)
qntg=area/21.6
qntgv=round(qntg+0.5)
totalg=qntgv*25
print('você deve comprar',qntgv,'galões')
print('que sairão por',totalg,'reais')
print('---'*20)
#### Melhor solução
print('solucões melhores')
folga=(area*10)/100
arear=area+folga
cobl=18*6
cobg=3.6*6
pl=80
pg=25
ql=0
qg=0
while arear>0:
 if arear >= cobl:
   ql += 1
   arear -= cobl
 elif arear >= cobg:
   qg += 1
   arear -= cobg
 else:
   ql += 1
   arear = 0
precot= (ql * pl) + (qg * pg)
print('você precisa de',ql,'latas','e',qg,'galões')
print('que sairão por',precot,'reais')

#17.Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tama=float(input('digite o tamanho do arquivo em MB '))
vel=float(input('digite a velocidade da internet em Mbps '))
tp=tama/vel
print('~~~~'*20)
print('o tempo para seu arquivo ser baixado é de',tp,'min')
print('~~~~'*20)