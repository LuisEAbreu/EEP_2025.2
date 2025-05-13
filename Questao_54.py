Questao_25.py

#coding:utf-8

'''
Considerando os dígitos 1, 2, 3, 4 e 5, quantos números de 2 algarismos distintos podem ser formados?
'''

def resolucao_q54():
	#Valores Fixos
	NumeroDeDigitos=5
	#Valores Variaveis
	NumeroDeAlgDistintos=0
	
	for i in range(NumeroDeDigitos):
		for j in range(NumeroDeDigitos):
			if i!=j:
				NumeroDeAlgDistintos+=1
				
	print("A quantidade de números com 2 algarismos distintos é:", NumeroDeAlgDistintos)
