from bagulho.jogo import brincadeira
from pytest import mark

def test_meu_primeiro_test():
    assert True


def test_quando_brincadeira_receber_1_então_deve_retornar_1():
    entrada = 1    #dado
    esperado = 1    #dado
    resultado = brincadeira(entrada)    #Quando

    assert resultado == esperado    #então


def test_quando_brincadeira_receber_2_então_deve_retornar_2():
    #TDD - Kent beck - One-step_Test
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_então_deve_retornar_queijo():
    #TDD - Kent beck - One-step_Test
    assert brincadeira(3) == 'queijo'


@mark.goiabada
def test_quando_brincadeira_receber_5_então_deve_retornar_goiabada():
    #TDD - Kent beck - One-step_Test
    assert brincadeira(5) == 'goiabada'


@mark.goiabada
def test_quando_brincadeira_receber_10_então_deve_retornar_goiabada():
    #TDD - Kent beck - One-step_Test
    assert brincadeira(10) == 'goiabada'


@mark.goiabada
def test_quando_brincadeira_receber_20_então_deve_retornar_goiabada():
    #TDD - Kent beck - One-step_Test
    assert brincadeira(20) == 'goiabada'


@mark.skip(reason="Pq ainda não implementei")
def test_quando_brincadeira_receber__1_então_deve_retornar_None():
    #TDD - Kent beck - One-step_Test
    assert brincadeira(20) == 'goiabada'