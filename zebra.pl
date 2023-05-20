% 1. Existem cinco casas.
casaN(1, C, (C, _, _, _, _)).
casaN(2, C, (_, C, _, _, _)).
casaN(3, C, (_, _, C, _, _)).
casaN(4, C, (_, _, _, C, _)).
casaN(5, C, (_, _, _, _, C)).

casa(C, CS):-
   casaN(1, C, CS);
   casaN(2, C, CS);
   casaN(3, C, CS);
   casaN(4, C, CS);
   casaN(5, C, CS).

direita(C, D, CS):-
    casaN(1, C, CS), casaN(2, D, CS);
    casaN(2, C, CS), casaN(3, D, CS);
    casaN(3, C, CS), casaN(4, D, CS);
    casaN(4, C, CS), casaN(5, D, CS).

vizinho(C, V, CS):-
    direita(C, V, CS);
    direita(V, C, CS).

casas(Casas):-
    % 2. O Inglês vive na casa vermelha.
    casa((ingles, vermelha, _, _, _), Casas),
    % 3. O Espanhol tem um cachorro.
    casa((espanhol, _, cachorro, _, _), Casas),
    % 4. Café é a bebida da casa verde.
    casa((_, verde, _, cafe, _), Casas),
    % 5. O Ucraniano bebe chá.
    casa((ucraniano, _, _, cha, _), Casas),
    % 6. A casa verde está à direita da casa marfim.
    direita((_, marfim, _, _, _), (_, verde, _, _, _), Casas),
    % 7. O fumante de Old Gold tem caramujos de estimação.
    casa((_, _, caramujos, _, oldgold), Casas),
    % 8. Cigarros Kools são consumidos na casa amarela.
    casa((_, amarela, _, _, kool), Casas),
    % 9. Leite é a bebida da casa do meio.
    casaN(3, (_, _, _, leite, _), Casas),
    % 10. O norueguês vive na primeira casa.
    casaN(1, (noruegues, _, _, _, _), Casas),
    % 11. O homem que fuma Chesterfields vive na casa vizinha do homem que tem uma raposa.
    vizinho((_, _, _, _, chesterfield), (_, _, raposa, _, _), Casas),
    % 12. Kools  é o cigarro da casa vizinha à casa onde existe um cavalo.
    vizinho((_, _, _, _, kool), (_, _, cavalo, _, _), Casas),
    % 13. O fumante de Lucky Strike bebe suco de laranja.
    casa((_, _, _, suco, luckystrike), Casas),
    % 14. O Japonês fuma Parliaments.
    casa((japones, _, _, _, parliament), Casas),
    % 15. O Norueguês é vizinho da casa azul.
    vizinho((noruegues, _, _, _, _), (_, azul, _, _, _), Casas),
    % alguém bebe água
    casa((_, _, _, agua, _), Casas),
    % alguém tem uma zebra
    casa((_, _, zebra, _, _), Casas).

pergunta(C):-
    casas(Casas),
    casa(C, Casas).

quemTemZebra(C):-
    C = (_, _, zebra, _, _),
    pergunta(C).

quemBebeAgua(C):-
    C = (_, _, _, agua, _),
    pergunta(C).
