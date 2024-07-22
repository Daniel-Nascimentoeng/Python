#Operações básicas com matrizes
import numpy as np
A=np.array([1,2,3])
print(A)
B=np.array([[2,3,4],[5,2,4]])
print(B)

print(B[1,2])

print(B[0,1])
C=np.array([[2,3,1],[2,4,5],[4,2,0]])
print(C)

D=B.dot(C)
print(D)
E=np.array([[2,-3,1],[-2,-4,5],[4,-2,0]])
F=C+E
print(F)

#Construindo matrizes usando o for.

V=np.zeros(3)
print(V)
for i in range(3):
  V[i]=i+1
print(V)
W=np.ones(3)
print(W)

for i in range(3):
  W[i]=pow(V[i],2)
print(W)

#Criação de Matrizes.
H=np.zeros((3,3))
traco=0
for i in range(3):
  for j in range(3):
    H[i][j]=i+j
print(H)
for i in range(3):
  traco=traco+H[i][i]
print(traco)

#EXERCÍCIO:Considere uma matriz 3x3 (I) onde I [i] [j] vale 1se existe ligação entre as cidades i e j. Assumindo que sempre existe ligação entre a cidade i e ela mesma.

#Construindo uma matriz I que pertecence ao conjunto de matrizes acima. Observe que uma possível matriz I tem a diagonal principal com valores 1 e se um elemento fora da diagonal , nos chamamos ele de I[i][j].assume o valor 1 , então I[j][i] também assume o valor 1.

#Construa uma matriz I que satisfaz as condições acima e que tem pelo menos 5 entradas com o valor 1. Mude um valor de uma das entradas para o valor 2.Em seguida, realize um teste para saber se a matriz satisfaz as condições do enunciado.

#Vocês vão percorrer a matriz e testar se I [i][i]==1,I[i][j]=0 ou 1 e se I[i][j]=I[j][i].)
I=np.array([[1,2,1],[0,1,0],[1,0,1]])
print(I)

testa1=1
testa2=1
testa3=1
for i in range(3):
  if I[i][i]!=1:
    testa1=0
for i in range(3):
  for j in range(3):
   if I[i,j]!=0 & I[i,j]!=1:
    testa2=0
   if I[i,j]!=I[j,i]:
        testa3=0
print(testa1)
print(testa2)
print(testa3)
