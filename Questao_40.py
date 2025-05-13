Questao_25.py

    #coding:utf-8

'''
Uma prova consta de 15 questões, das quais o aluno deve resolver 10. 
De quantas formas ele podería resolver as 10 questões?
'''

import random as rn

def fatorial(n):
   Resultado=1
   for i in range(1, n+1):
       Resultado=Resultado*i
   return Resultado

def resolucao_q40():
   # Valores Fixos
   NumeroQuestoes=15
   AlunoDeveResolver=10
   
   Combinatoria=(fatorial(NumeroQuestoes))/(fatorial(AlunoDeveResolver)*(fatorial(NumeroQuestoes-AlunoDeveResolver)))
   
   print("A quantidade de formas que o Aluno pode resolver as 10 questões é:", Combinatoria)

