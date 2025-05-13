Questao_25.py

#coding:utf-8

'''
Hemofilia é um distúrbio genético associado a um gene pertencente ao cromossomo X. 
A doença acomete somente meninos e é transmitido exclusivamente pela mãe. 
Dado o histórico familiar de uma mulher, determinou-se que havia 15% de probabilidade 
de que ela portasse o gene. Suponha que, se a mãe for portadora do gene então cada 
filho tería, independentemente, 30% de chance de ter a doença, e se a mãe não for 
portadora, o filho não tería a doença. Sabendo que esta mulher teve três filhos sem 
a doença, qual é a probabilidade que seja portadora do gene?
'''
import random as rn

def resolucao_q241():
    #Varíaveis Fixas
    NumeroRepeticoes=1e06
    #Variáveis mutáveis
    TotalFilhosSaudaveis=0
    MaePortadora_FilhosSaudaveis=0

    for _ in range(int(NumeroRepeticoes)):
        
        MaePortadora=rn.random()<0.15
        FilhosDoentes=0

        for _ in range(3):
            if MaePortadora:
                if rn.random()<0.3:
                    FilhosDoentes+=1
            else:
                pass

        if FilhosDoentes==0:
            TotalFilhosSaudaveis+=1
            if MaePortadora:
                MaePortadora_FilhosSaudaveis+=1
    
    print("A probabilidade da mãe ser portadora tendo 3 filhos saudáveis é: ", MaePortadora_FilhosSaudaveis/TotalFilhosSaudaveis)

