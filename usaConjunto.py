# from pylatex import Document, Section
import Conjuntos

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 2)
B = Conjunto("B", 2)

#Contem, Possui, Tamanho e Contem propriamente dito.
print(A.contem(B))
print(B.possui(3))
print(A.tamanho())
print(A.contem_propriamente(B))

#Igual e Vazio
print(A.eh_vazio())
print(A.eh_igual(B))

# Interseção e União
A.intersecao(B).imprimir()
B.uniao(A).imprimir()