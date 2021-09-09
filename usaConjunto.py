# from pylatex import Document, Section
import Conjuntos
import pprint as pp

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, 3)
B = Conjunto("B", 'a', 'b', 'c')
C = Conjunto("C", 1, 2, 4, 5)
D = Conjunto("D", A, 1, 2)
E = Conjunto("E", B, C)

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
# print(A.intersecao(B).elementos)
# B.uniao(A).string()
print(D.conjunto_das_partes().string())
# pp.pprint(A.produto_cartesiano(C).elementos)
