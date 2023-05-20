## [rna.py](rna.py)

Tentativa de criação de rede neural em python.

## [zebra.pl](zebra.pl)

Programa para resolver o quebra cabeça da zebra (também conhecido como teste de Einstein) em prolog.

casaN(N, C, Casas): verifica se a casa N é a casa informada.

ehCasa(C, Casas): verifica se a casa informada é uma das 5 casas.

direita(C, D, Casas): verifica se a casa D está à direita da casa C.

vizinho(C, D, Casas): verifica se as casas C e D são vizinhas.

casas(Casas): verifica (e encontra) uma possível solução do problema.
As regras do problema estão dispostas como predicatos utilizando as funções anteriores.

Para descobrir quem bebe água, chame a função quemBebeAgua(C).

Para descobrir onde fica a zebra, chame a função quemTemZebra(C).

Para mostrar todas as casas, chame casas(C).

Para realizar perguntas diversas, chame pergunta((Morador, Cor, Animal, Bebida, Cigarro)).
