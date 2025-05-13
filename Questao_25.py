# coding:utf-8

'''
De quantas maneiras podemos dar 2 prêmios a uma classe com 10 alunos, considerando:
a) que os 2 prêmios não sejam dados a um mesmo aluno?
b) que os 2 prêmios possam ser dados a um mesmo aluno?
'''

def resolucao_q25():
   # Valores Fixos
   NumeroAlunos=10

   # Valores Variáveis
   SemRepeticao=0
   ComRepeticao=0

   for i in range(NumeroAlunos):
      for j in range(NumeroAlunos):
         if i!=j:
            SemRepeticao+=1

   for i in range(NumeroAlunos):
      for j in range(NumeroAlunos):
         ComRepeticao+=1

   print("a) Se o prêmio só for dado a alunos distintos, o total é:", SemRepeticao)
   print("b) Se o prêmio for dado ao mesmo aluno, o total é:", ComRepeticao)

