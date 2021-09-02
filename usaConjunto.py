# from pylatex import Document, Section
import Conjuntos
import pprint as pp

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, (2, 9))
B = Conjunto("B")
C = Conjunto("C")

# A.inserir(B)

# Contem, Possui, Tamanho e Contem propriamente dito.
# print(A.contem(B))
# print(B.possui(3))
# print(A.tamanho())
# print(A.contem_propriamente(B))

# #Igual e Vazio
# print(A.eh_vazio())
# print(A.eh_igual(B))

# # Interseção e União
# A.intersecao(B).imprimir()
# B.uniao(A).imprimir()

pp.pprint(A.conjunto_das_partes().elementos)
pp.pprint(A.produto_cartesiano(C).elementos)
