Questao_25.py

#coding:utf-8

'''
É dada a distribuição de 300 estudantes segundo o sexo e a área de concentração numa faculdade:

          Biologia Exatas Humanas
Masculino    52      40     58
Feminino     38      32     80

Um estudante é sorteado ao acaso.
a) Qual é a probabilidade de que ele seja do sexo feminino e da área de humanas?
b) Qual é a probabilidade de que ele seja do sexo masculino e não seja da área de biológicas?
c) Dado que foi sorteado um estudante da área de humanas, qual é a probabilidade de que ele seja do sexo feminino?
'''

import random as rn

def resolucao_q162():
   
    Distribuicao = [0,0,0,0,0,0]
    NumeroRepeticoes = 1e06
    
    for _ in range(int(NumeroRepeticoes)):
                  
        x = rn.randint(1 , 300)
        sexo=0
        if(x<=150):
            sexo=1
        elif(x>150):
            sexo=2

        y = rn.randint(1,150)

        if(sexo==1):
            if(y<=52):
                Distribuicao[0]+=1
            elif(y>52 and y<=92):
                Distribuicao[1]+=1
            elif(92<y and y<=150):
                Distribuicao[2]+=1
                    
        elif(sexo==2):
            if(y<=38):
                Distribuicao[3]+=1
            elif(y>38 and y<=70):
                Distribuicao[4]+=1
            elif(70<y and y<=150):
                Distribuicao[5]+=1
                
    print("a) A probabilidade de ser do sexo feminino e da área de humanas é", (Distribuicao[5])/NumeroRepeticoes)
    print("b) A probabilidade de ser do sexo masculino e não ser da área de biológicas é", (Distribuicao[1]+Distribuicao[2])/NumeroRepeticoes)
    print("c) A probabilidade de um estudante sorteado da área de humanas ser do sexo feminino é", (Distribuicao[5])/(Distribuicao[2]+Distribuicao[5]))

