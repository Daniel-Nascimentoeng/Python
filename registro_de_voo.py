# Esse algoritmo foi desenvolvido para simular um registro de voo.
class Passageiro:
  def __init__(self, nvoo, compaerea, assento, portao, horario):
    self.nvoo, self.compaerea, self.assento, self.portao, self.horario, = nvoo, compaerea, assento, portao, horario
passageiros = []
for c in range(3):
  nvoo = int(input('digite o n° do voo: '))
  compaerea = input('digite a sua companhia aerea: ')
  assento = int(input('digite o numero do seu assento: '))
  portao=int(input('digite o numero do portão de embarque: '))
  horario = int(input('digite o horario de embarque: '))
  passageiro= Passageiro(nvoo, compaerea, assento, portao, horario)
  passageiros.append(passageiro)

for k in range(3):
  print(passageiros[k].nvoo)
  print(passageiros[k].compaerea)
  print(passageiros[k].assento)
  print(passageiros[k].portao)
  print(passageiros[k].horario)

for j in range(3):
  if passageiros[j].nvoo==135:
    print(passageiros[j].nvoo)
    print(passageiros[j].compaerea)
    print(passageiros[j].assento)
    print(passageiros[j].portao)
    print(passageiros[j].horario)


for v in range(3):
  if passageiros[v].compaerea == 'azul':
    print(passageiros[v].compaerea)
    print(passageiros[v].nvoo)
    print(passageiros[v].assento)
    print(passageiros[v].portao)
    print(passageiros[v].horario)

    totalazu = 0

for d in range(3):
  if passageiros[d].compaerea == 'azul':
    totalazu = totalazu +1

print('O total de passageiros da Azul é :', totalazu)