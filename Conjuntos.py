from __future__ import annotations
import itertools


operacoes = {}  # Operações feitas são guardadas aqui, para motivos de otimização
universo = []   # Conjunto que contém todos os elementos já criados


def remove_virgulas(texto: str) -> str: return texto.replace(",", "")


def adiciona_chave_inicial(texto: str) -> str: return texto.replace("(", "{")


def adiciona_chave_final(texto: str) -> str: return texto.replace(")", "}")


def tratar_conjunto(conjuntos: str) -> str:
    return adiciona_chave_final(
        adiciona_chave_inicial(conjuntos)
    )


class Conjunto:
    def __init__(self, nome, *elementos) -> object:
        """
        Cria um novo tipo de dados chamado conjunto

        Parâmetros:

        - (string) nome: Nome que será dado ao conjunto
        - (string / int) *elementos: Um ou múltiplos elementos que serão inseridos no conjunto

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        Saída:

        - Conjunto("A", 1, 2, 3)

        """
        self.nome = nome
        self.elementos = []
        for i in elementos:
            if i not in self.elementos:
                self.elementos.append(i)
                if i not in universo:
                    universo.append(i)

    def string(self) -> str:
        """
        Retorna o conjunto chamador como uma string.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        - A.string()

        Retorno:

        - A = {1,2,3}

        """
        conjunto = self.nome + " = {"
        for elemento in self.elementos:
            if isinstance(elemento, str) or isinstance(elemento, int):
                conjunto += str(elemento) + ","
            else:
                try:
                    conjunto += "{" + str(elemento.elementos) + "},"
                except AttributeError:
                    if len(elemento) > 0:
                        complementar = "{"
                        # necessario conversao de tipo
                        lista = list(elemento)
                        for e in lista:
                            # caso n seja o ultimo
                            if e != lista[-1]:
                                complementar += str(e) + ","
                            else:
                                complementar += str(e) + "},"
                        conjunto += complementar
                    else:
                        conjunto += "{},"

        if conjunto[-1] == ',':
            conjunto = conjunto[:-1]

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "") + "}"

        return conjunto

    def tamanho(self) -> int:
        """
        Retorna o tamanho do conjunto.
        Exemplo:
        - A = Conjunto("A", 1, 2, 3)
        - A.tamanho()
        Saída:
        - 3
        """
        return len(self.elementos)

    def atualizaOperacoes(self, nome) -> None:
        """
        Atualiza o dicionário de operações, cache.

        Parâmetros:
        - (string) nome: Nome da operação que será adicionada.

        Exemplo:

        - conjunto.atualizaOperacoes("A U B")
        """
        remove = []
        for operacao in operacoes:
            if nome in operacao:
                remove.append(operacao)

        for i in remove:
            operacoes.pop(i)

    def inserir(self, elemento, operacao=False) -> None:
        """
        Insere determinado elemento no conjunto chamador.

        Parâmetros:
        - (String / int) elemento: Elemento que será inserido.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        - A.inserir(4)
        """
        if operacao == False:
            if elemento not in self.elementos:
                self.elementos.append(elemento)
                self.atualizaOperacoes(self.nome)
        else:
            if elemento not in self.elementos:
                self.elementos.append(elemento)

    def possui(self, elemento) -> bool:
        """
        Checa se o elemento passado possui no conjunto chamador.

        Parâmetros:
        - (String / int) elemento: Elemento que será verificado.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        - A.possui(2)

        Saída:

        - True

        """
        return elemento in self.elementos

    def contem(self, conjunto) -> bool:
        """
        Checa se o conjunto chamador contem tal conjunto.

        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado junto ao conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3, (2, 9))
        - B = Conjunto("B", (2, 9))


        - A.contem(B)

        Saída:

        - True

        """
        if self.tamanho() < conjunto.tamanho():
            return False
        else:
            for elemento in conjunto.elementos:
                if elemento not in self.elementos:
                    return False
            return True

    def eh_vazio(self) -> bool:
        """
        Checa se o conjunto é vazio.

        Exemplo:

        - A = Conjunto("A")

        - A.eh_vazio()

        Saída:

        - True

        """
        return self.tamanho() == 0

    def eh_igual(self, conjunto) -> bool:
        """
        Checa se um conjunto é igual ao outro.

        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será comparado ao conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)
        - B = Conjunto("B", 4, 5, 6)

        - A.eh_igual(B)

        Saída:

        - False

        """
        if self.tamanho() == conjunto.tamanho():
            return self.contem(conjunto)
        return

    def contem_propriamente(self, conjunto) -> bool:
        """
        Checa se o conjunto chamador contem propriamente tal conjunto.
        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado junto ao conjunto chamador.
        Exemplo:
        - A = Conjunto("A", 1, 2, 3, (2, 9))
        - B = Conjunto("B", (2, 9))
        - A.contem_propriamente(B)
        - A.contem_propriamente(A)
        Saída:
        - True
        - False
        """
        if self.contem(conjunto):
            return self.tamanho() > conjunto.tamanho()
        return False

    def uniao(self, conjunto) -> object:
        """
        Une dois conjuntos, retornando um novo conjunto contendo os elementos de ambos.
        Parâmetros:
        - (Conjunto) conjunto: Os elementos deste conjunto serão unidos ao conjunto chamador.
        Exemplo:
        - A = Conjunto("A", 1, 2, 3)
        - B = Conjunto("B", 4, 5, 6)
        - A.uniao(B)
        Saída:
        - Conjunto("A U B", 1, 2, 3, 4, 5, 6)
        """
        uniao = Conjunto(f"{self.nome} ∪ {conjunto.nome}")

        if self.eh_igual(conjunto):
            uniao.elementos = self.elementos
            operacoes[f"{self.nome} ∪ {conjunto.nome}"] = uniao

        elif uniao.nome not in operacoes and uniao.nome[::-1] not in operacoes:
            if not conjunto.eh_vazio() and not self.eh_vazio():
                if conjunto.tamanho() > self.tamanho():
                    uniao.elementos = conjunto.elementos
                    for elemento in self.elementos:
                        uniao.inserir(elemento, True)
                else:
                    uniao.elementos = self.elementos
                    for elemento in conjunto.elementos:
                        uniao.inserir(elemento, True)
            else:
                if conjunto.eh_vazio() and not self.eh_vazio():
                    uniao.elementos = self.elementos
                else:
                    uniao.elementos = conjunto.elementos

            operacoes[f"{self.nome} ∪ {conjunto.nome}"] = uniao

        try:
            return operacoes[uniao.nome]
        except KeyError:
            return operacoes[uniao.nome[::-1]]

    def intersecao(self, conjunto) -> object:
        """
        Retorna um novo conjunto contendo os elementos de que fazem partes de ambos.
        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado na interseção com o conjunto chamador.
        Exemplo:
        - A = Conjunto("A", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        - B = Conjunto("B", 0, 2, 4, 6, ...)
        - A.intersecao(B)
        Saída:
        - Conjunto("A ^ B", 0, 2, 4, 6, 8)
        """
        intersecao = Conjunto(f"{self.nome} ∩ {conjunto.nome}")

        if self.eh_igual(conjunto):
            intersecao.elementos = self.elementos
            operacoes[f"{self.nome} ∩ {conjunto.nome}"] = intersecao

        elif intersecao.nome not in operacoes and intersecao.nome[::-1] not in operacoes:
            if not conjunto.eh_vazio() and not self.eh_vazio():
                for elemento in conjunto.elementos:
                    if self.possui(elemento):
                        intersecao.inserir(elemento)
                operacoes[f"{self.nome} ∩ {conjunto.nome}"] = intersecao
        try:
            return operacoes[intersecao.nome]
        except KeyError:
            if conjunto.eh_vazio():
                return conjunto
            return operacoes[intersecao.nome[::-1]]

    def complemento(self) -> Conjunto:
        """
        Retorna o conjunto complementar.

        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado para complementar o conjunto chamador.

        Exemplo:

        - X = Conjunto("X", 4, 5)
        - Y = Conjunto("Y", 5, 6)
        - U = Conjunto("U", 4, 5, 6)


        - X.complementar(Y)

        Saída:

        - Conjunto("~X", 6)

        """
        complemento = Conjunto(f"~{self.nome}")
        for elemento in universo:
            if elemento not in self.elementos:
                complemento.inserir(elemento, True)
        return complemento

    def diferenca(self, conjunto) -> Conjunto:
        """
        Realiza a diferença entre dois conjuntos, retornando um novo conjunto com os elementos resultantes da diferença.
        Parâmetros:
        - (Conjunto) conjunto: Conjunto que será usado na diferença com o conjunto chamador.
        Exemplo:
        - X = Conjunto("X", 4, 5)
        - Y = Conjunto("Y", 5, 6)
        - X.diferenca(Y)
        Saída:
        - Conjunto("X - Y", 4)
        """

        diferenca = Conjunto(f"{self.nome} - {conjunto.nome}")

        if diferenca.nome not in operacoes:
            if self.eh_vazio() == False and conjunto.eh_vazio() == False:
                for elemento in self.elementos:
                    if elemento not in conjunto.elementos:
                        diferenca.inserir(elemento, True)
                operacoes[f"{diferenca.nome}"] = diferenca
        try:
            return operacoes[diferenca.nome]
        except KeyError:
            return Conjunto()

    def conjunto_das_partes(self) -> Conjunto:
        """
        Retorna um novo conjunto contendo as combinações possíveis dos elementos de um conjunto.

        Exemplo:

        - X = Conjunto("X", 5, 4)

        - X.conjuntoDasPartes().string()

        - Saída em tela:
        - - {}, {5}, {4}, {5, 4}

        """

        elementos = self.elementos
        conjunto_das_partes = Conjunto("Conjunto das Partes")

        for indice in range(0, len(elementos) + 1):
            combinacoes = list(itertools.combinations(elementos, indice))
            for conjuntos in combinacoes:
                try:
                    conjuntos = tratar_conjunto(str(conjuntos))
                    ultimo_caractere = conjuntos[-2]
                    if ultimo_caractere == ',':
                        conjunto_das_partes.inserir(remove_virgulas(conjuntos))
                    else:
                        conjunto_das_partes.inserir(conjuntos)
                except IndexError:
                    pass

        return conjunto_das_partes

    def produto_cartesiano(self, conjunto) -> Conjunto:
        """
        Retorna um novo conjunto contendo o produto cartesiano entre dois conjuntos.

        Exemplo:

        - X = Conjunto("X", 5, 4)
        - Y = Conjunto("Y", 8, 2)

        - X.produto_cartesiano(Y)

        - Saída:
        - Conjunto("X * Y", (5,8), (5,2), (4,8), (4,2))
        """
        if conjunto.eh_vazio():
            return self

        produto_operacao = itertools.product(
            self.elementos, conjunto.elementos)
        conjunto_cartesiano = Conjunto("{self.nome} * {conjunto.nome}")

        for produto_atual in produto_operacao:
            conjunto_cartesiano.inserir(produto_atual)

        return conjunto_cartesiano
