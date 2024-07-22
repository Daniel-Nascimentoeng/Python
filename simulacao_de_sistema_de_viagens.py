#Vamos simular a compra de bilhetes de aviâo num site da azul'
#ao abrir o site da azul , o sistema pede alguma entradas.
#1° entrada= origem e destino
#2° entrada= voo só de ida ou ida e volta
#3° entrada= data da ida e da volta se necessario
#Após esse dados de entrada, o sistema propoe alguns voos
#Em seguidas,você escolhe um dos voo ou sai do site.
#Nesse momento, o cliente digita o seu email.
#Se escolheu um dos voos, voce faz o pagamento e sai do sistema.

#Esse código abaixo simula os dados de entrada em um sistema de viagem 
origem=input('Origem: ')
destino=input('Destino: ')
ida_volta=int(input('Só ida (1),ida e volta (2): '))
data_ida=input("digite a data de ida: ")
if ida_volta==2:
  data_volta=input('digite a data de volta: ')
#Em seguida é mostrado ao usuário o Banco de dados do sistema de viagem  
import numpy as np
horario1=12
horario2=14
horario3=6
horario4=8
data1="27 de setembro de 2023"
data2="02 de outubro de 2023"

voo1=np.array([['Recife'],['Salvador'],[data1],[horario1],[1000]])
voo2=np.array([['Recife'],['Salvador'],[data1],[horario2],[1200]])
voo3=np.array([['Salvador'],["Recife"],[data2],[horario3],[800]])
voo4=np.array([['Salvador'],['Recife'],[data2],[horario4],[700]])

if (voo1[0]=='Recife')&(voo1[1]=="Salvador")&(voo1[2]==data1):
  print('Seu vou vai sair de,',voo1[0],"para",voo1[1],'em',voo1[2],"as",voo1[3],"horas",',no preço',voo1[4],'reais')
if (voo2[0]=='Recife')&(voo2[1]=="Salvador")&(voo2[2]==data1):
  print('Seu vou vai sair de,',voo2[0],"para",voo2[1],'em',voo2[2],"as",voo2[3],"horas",',no preço',voo2[4],'reais')
if ida_volta==2:
  if (voo3[0]=='Salvador')&(voo3[1]=="Recife")&(voo3[2]==data2):
    print('Seu vou vai sair de,',voo3[0],"para",voo3[1],'em',voo3[2],"as",voo3[3],"horas",',no preço',voo3[4],'reais')
  if (voo4[0]=='Salvador')&(voo4[1]=="Recife")&(voo4[2]==data2):
    print('Seu vou vai sair de,',voo4[0],"para",voo4[1],'em',voo4[2],"as",voo4[3],"horas",',no preço',voo4[4],'reais')
#Ao final é calculado e computado o gasto da viagem.
vooida=input('escolha voo de ida 1 ou 2 ')
if ida_volta==2:
  voovolta=input('escolha voo de volta 3 ou 4? ')

if ida_volta==1:
 if vooida==1:
  print('total em reais', voo1[4])
 else:
     print('total em reais', voo2[4])
else:
 if(vooida==1)&(voovolta==3):
    print('total em reais',voo1[4]+voo3[4])