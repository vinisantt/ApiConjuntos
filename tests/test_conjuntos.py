import unittest
from Conjuntos import Conjunto


class ConjuntosTest(unittest.TestCase):

    def test_nome_do_conjunto_deve_ser_o_mesmo_que_o_do_parametro(self):
        conjunto = Conjunto('A', 1, 2, 3, 4)
        assert conjunto.nome == 'A'

    def test_conjunto_deve_ter_tamanho_igual_ao_do_parametro(self):
        conjunto = Conjunto('A', 1, 2, 3, 4)
        assert conjunto.tamanho() == 4

    def test_inserir_elemento_deve_adicionar_elemento_a_lista_de_elementos(
            self):
        conjunto = Conjunto('A', 1, 2, 3, 4)
        conjunto.inserir(5)
        assert conjunto.elementos == [1, 2, 3, 4, 5]

    def test_inserir_elemento_ja_existente_nao_deve_adicionar_elemento(
            self):
        conjunto = Conjunto('A', 1, 2, 3, 4)
        conjunto.inserir(2)
        assert conjunto.elementos == [1, 2, 3, 4]

    def test_deve_retornar_true_se_conjunto_contem_elemento(self):
        conjunto = Conjunto('A', 1, 2)
        assert conjunto.possui(1)
        assert conjunto.possui(2)

    def test_deve_retornar_false_se_conjunto_nao_contem_elemento(self):
        conjunto = Conjunto('A', 1, 2)
        assert not conjunto.possui(8)
        assert not conjunto.possui(7)

    def test_deve_retornar_true_se_conjunto_contem_conjunto(self):
        conjunto_a = Conjunto('A', 1, 2, (2, 3))
        conjunto_b = Conjunto('B', (2, 3))

        assert conjunto_a.contem(conjunto_b)

    def test_deve_retornar_false_se_conjunto_nao_contem_conjunto(self):
        conjunto_a = Conjunto('A', 1, (2, 3))
        conjunto_b = Conjunto('B', (2, 3, 4))
        conjunto_c = Conjunto('C', (2, 3))
        assert not conjunto_a.contem(conjunto_b)
        assert not conjunto_b.contem(conjunto_c)

    def test_deve_retornar_true_se_conjunto_esta_vazio(self):
        conjunto = Conjunto('A')
        assert conjunto.eh_vazio()

    def test_deve_retornar_false_se_conjunto_nao_esta_vazio(self):
        conjunto = Conjunto('A', 1)
        assert not conjunto.eh_vazio()

    def test_deve_retornar_true_se_conjunto_e_igual_a_outro(self):
        conjunto_a = Conjunto('A', 1, 2, 3)
        conjunto_b = Conjunto('B', 1, 2, 3)
        assert conjunto_a.eh_igual(conjunto_b)

    def test_deve_retornar_false_se_conjunto_e_diferente_de_outro(self):
        conjunto_a = Conjunto('A', 1, 2, 3)
        conjunto_b = Conjunto('B', 1, 2, 4)
        assert not conjunto_a.eh_igual(conjunto_b)

    def test_deve_retornar_true_se_conjunto_contem_propriamente_outro_conjunto(
            self):
        conjunto_a = Conjunto('A', 1, 2, 3)
        conjunto_b = Conjunto('B', 3)
        assert conjunto_a.contem_propriamente(conjunto_b)

    def test_deve_retornar_false_se_conjunto_nao_contem_propriamente_outro_conjunto(
            self):
        conjunto_a = Conjunto('A', 1, 2, 3)
        conjunto_b = Conjunto('B', 1, 2, 4)
        assert not conjunto_a.contem_propriamente(conjunto_b)

    def test_contem_propriamente_deve_retornar_false_se_conjunto_e_vazio(self):
        conjunto = Conjunto('A')
        conjunto_a = Conjunto('B', 1, 2, 3)
        assert not conjunto.contem_propriamente(conjunto_a)

    def test_contem_propriamente_deve_retornar_false_se_tamanho_do_conjunto_parametro_for_menor_que_o_conjunto(
            self):
        conjunto_a = Conjunto('A', 1, 2, 3)
        conjunto_b = Conjunto('B', 1, 2)
        assert not conjunto_b.contem_propriamente(conjunto_a)

    def test_conjunto_das_partes_deve_retornar_conjunto_contendo_combinacao_de_elementos_de_um_conjunto(
            self):
        conjunto_parametro = Conjunto('A', 1, 2, 3)
        conjunto_esperado = Conjunto(
            'Conjunto das Partes', '{}', '{1}', '{2}', '{3}', '{1, 2}', '{1, 3}', '{2, 3}', '{1, 2, 3}')

        assert conjunto_parametro.conjunto_das_partes(
        ).elementos == conjunto_esperado.elementos

    def test_conjunto_das_partes_deve_retornar_um_conjunto(self):
        assert isinstance(
            Conjunto(
                'A',
                1,
                2,
                3).conjunto_das_partes(),
            Conjunto
        )

    def test_conjunto_das_partes_deve_retornar_conjunto_vazio_se_conjunto_parametro_for_vazio(
            self):
        assert Conjunto('A').conjunto_das_partes(
        ).elementos == Conjunto('Conjunto das Partes', '{}').elementos

    def test_produto_cartesiano_deve_retornar_um_conjunto(self):
        assert isinstance(
            Conjunto(
                'A',
                1,
                2,
                4
            ).produto_cartesiano(Conjunto(
                'B',
                7,
                12,
                (4,18)
            )),
            Conjunto
        )

    def test_produto_cartesiano_produto_deve_ser_maior_que_o_conjunto_base(self):
        ConjuntoA = Conjunto('A', 1, 4, 6)
        ConjuntoB = Conjunto('C', 4, 6, 8)
        assert ConjuntoA.produto_cartesiano(ConjuntoB).tamanho() > ConjuntoA.tamanho()

    def test_produto_cartesiano_quando_segundo_conjunto_passado_for_vazio_retornar_proprio_conjunto(self):
        assert Conjunto('A', 4, 5, 12).produto_cartesiano(Conjunto('B')).elementos == Conjunto('A', 4, 5, 12).elementos