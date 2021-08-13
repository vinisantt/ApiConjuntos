# from pylatex import Document, Section
import Conjuntos

Conjunto = Conjuntos.Conjunto

A = Conjunto("A", 1, 2, (2, 9))
B = Conjunto("B", 2)

print(A.possui((2, 9)))
print(B.possui(3))
print(A.tamanho())