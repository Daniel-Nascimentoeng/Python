#Na disciplina de Introdução a programção o professor inicio o assunto de matrizes
#Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela.Com a formatação correta.
matriz = [[0,0,0], [0,0,0],[0,0,0]]
for l in range(0,3):
  for c in range(0,3):
    matriz[l] [c] = int(input(f'digite um valor para [{l},{c}]: '))
print('-='*30)
for l in range(0,3):
  for c in range(0,3):
      print(f'[{matriz[l] [c]:^5}]',end='')
  print()
print('-='*30)
