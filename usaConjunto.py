# from pylatex import Document, Section
import Conjuntos

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 2)
B = Conjunto("B", 2)

print(A.contem(B))
print(B.possui(3))
print(A.tamanho())
print(A.eh_vazio())
print(A.eh_igual(B))
print(A.contem_propriamente(B))
