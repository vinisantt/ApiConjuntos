import itertools

operacoes = {}  # Operações feitas são guardadas aqui, para motivos de otimização
universo = []   # Conjunto que contém todos os elementos já criados


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

    def imprimir(self, operacao=False) -> str:
        """
        Imprime o conjunto chamador.

        Exemplo:

        - A = Conjunto("A", 1, 2, 3)

        - A.imprimir()

        Saída:

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
                        for ele in lista:
                            # caso n seja o ultimo
                            if ele != lista[-1]:
                                complementar += str(ele) + ","
                            else:
                                complementar += str(ele) + "},"
                        conjunto += complementar
                    else:
                        conjunto += "{},"

        if conjunto[-1] == ',':
            conjunto = conjunto[:-1]

        conjunto = conjunto.replace(
            "[", "").replace("]", "").replace("'", "") + "}"

        if operacao:
            return conjunto
        print(conjunto)

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
        return False

