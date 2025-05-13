Questao_25.py

#coding:utf-8
'''
 Um polígrafo (detector de mentiras) é um aparelho que mede usualmente três sinais fisiológicos de uma pessoa:
    atividade respiratória;
    atividade cardiovascular;
    condutância galvânica da pele.
 O teste todavia não é perfeito, há pessoas que são capazes de controlar conscientemente os 
sinais fisiológicos citados e passam no teste poligráfico mentindo, e há outras que o próprio 
teste desequilibra a pessoa gerando resultados inconclusivos ou falsos. Estatisticamente, 
o teste poligráfico identifica com 92% de acurácia que uma pessoa está mentindo, e tem 
proporção de 2% de falso positivos, ou seja, identifica como mentira uma afirmação verdadeira 
de uma pessoa. Uma agência de inteligência precisa identificar um agente duplo que vazou uma 
informação sensível, e sabe que somente uma pessoa dentre as 30 que trabalham na agência teve 
acesso de forma ilegal à informação. Suponha que somente o agente duplo iría mentir quando 
perguntado se vazou a informação, e que esta sería a informação comparada pelo perito com outras 
verdadeiras que faría ao investigado. Avalie os resultados do polígrafo da seguinte forma:
a) se o polígrafo identifica que um dado agente
está mentindo, qual a probabilidade de ser o culpado.
b) se o polígrafo identifica que um dado agente
não está mentindo, qual a probabilidade de ele ser o culpado.
'''

import random as rn

def resolucao_q238():
   #Varíaveis Fixas
   NumeroRepeticoes=1e06
   Acuracia=0.92
   FalsoPositivo=0.02
   #Variáveis mutáveis
   DetectouMentira=0
   AchouCulpado=0
   Nao_DetectouMentira=0
   Nao_AchouCulpado=0
   
   for _ in range(int(NumeroRepeticoes)):

      Culpado=rn.randint(0,29)
      PegoMentindo=[]
      
      for i in range(30): 
         if i==Culpado:
            if rn.random()<Acuracia:
               PegoMentindo.append(i)
         else:
            if rn.random()<FalsoPositivo:
               PegoMentindo.append(i)

      if Culpado in PegoMentindo:
         DetectouMentira+=1
         AchouCulpado+=1

      elif PegoMentindo: 
         DetectouMentira+=1

      else:
         Nao_DetectouMentira+=1
         if Culpado==0:
            Nao_AchouCulpado+=1

   print("a) A probabilidade de um agente mentindo ser o culpado é:", AchouCulpado/DetectouMentira)
   print("b) A probabilidade de um agente que não está mentindo ser o culpado é:", Nao_AchouCulpado/Nao_DetectouMentira)

