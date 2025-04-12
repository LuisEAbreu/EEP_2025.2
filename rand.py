#coding: utf-8

import random as r
TotNum = 10
print(f"Imprimir {TotNum} numeros aleatórios entre 0 e 1:")
for _ in range(TotNum): 
	print(r.random())
	
inicio = 10
fim = 20	
print(f"Imprimir {TotNum} numeros aleatórios inteiros entre {inicio} e {fim} inclusive:")
for _ in range(TotNum): 
	print(r.randint(inicio, fim))

