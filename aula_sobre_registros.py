#Nesta aula desenvovi alguns resgistros para trabalhar com aferramenta "class".
#Registro de pessoas 
class Pessoa :
  def __init__(self,nome,idade):
    self.nome,self.idade,=nome,idade
pessoas = []
for c in  range(3):
  nome = input('digite o nome da pessoa: ')
  idade = int(input('digite agora a idade da pessoa:  '))
  pessoa= Pessoa(nome, idade)
  pessoas.append(pessoa)
#pessoa = min(pessoas,key = lambda p: p.idade)
#print(f'{pessoa .nome} é a pessoa mais nova, com {pessoa})
print(pessoas[0].nome)
for j in range(3):
  print(pessoas[j].nome)
  print(pessoas[j].idade)

#Registro de Alunos 
class Aluno:
  def __init__(self,nome, idade, matricula, curso):
    self.nome,self.idade,self.matricula,self.curso,=nome,idade,matricula,curso
alunos = []
for c in range(3):
  nome = input('digite o nome do aluno: ')
  idade = int(input('digite a idade do aluno: '))
  matricula = int(input('digite a matricula do aluno: '))
  curso = input('digite o curso do aluno: ')
  aluno= Aluno(nome, idade, matricula, curso)
  alunos.append(aluno)

for j in range(3):
  print(alunos[j].nome)
  print(alunos[j].idade)
  print(alunos[j].matricula)
  print(alunos[j].curso)

for k in range(3):
  if alunos[k].idade<70:
   print(alunos[k].idade)