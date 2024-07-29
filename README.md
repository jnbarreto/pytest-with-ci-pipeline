# Implementação do pipeline CI no aprendizado de testes com pytest

Pytest - commands
Documentação pytest - https://docs.pytest.org/en/stable/index.html

pytest: roda todos os testes<br>
pytest [name_archive_test]: roda o teste especifico<br>
pytest -v: da um detalhamento a mais<br>
pytest -x: Fast error, Se um erro quebrar ele já vai parar os teste<br>
pytest --pdb: ele para o debugger exatamente na onde quebrou<br>
pytest -k [name_test]: funciona como uma keyword, ele vai executar os testes com aquele nome<br>
pytest -s: mostra os prints na execução do teste<br>
pytest -rs: mostra a razão de ter pulado<br>


# Status de Falhas
.: passou
F: Falhou
x: Falha esperada
X: Falha esperada, mas não falhou
s: Pulou(skiped)


# Salvar o Resultados do teste
pytest --junitxml report_1.xml


# Mark tags ou grupos

from pytest import mark

@mark.[tag]

pytest -m [tag]: vai executar todos desse grupo
pytest -m "not [tag]": vai executar todos que não for desse grupo

## Marcadores defaults do pytest

@mark.skip: Para pular um test
ex: @mark.skip(reason="Pq ainda não implementei")

@mark.skipif: Para pular um teste em deteminado contexto
ex: @mark.skipif(sys.platform == "win32", reason="does not run on windows")

@mark.xfail: É esperado que este teste falhe em algum contexto
ex: @pytest.mark.xfail(reason="known parser issue")

@mark.usefixture: É basicamente uma maneira de "entrar" em um contexto. ou prover uma ferramenta que precisa ser executada "antes" ou "depois" dos testes 

@mark.parametrize: permite a parametrização de argumentos para uma função de teste
ex: @pytest.mark.parametrize("entrada,esperado", [(1, 1), (2, 2), (3, "queijo"), (4, 4), (5, "goiabada")])






