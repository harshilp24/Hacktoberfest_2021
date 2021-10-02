% hierarchy of hands
beats(rock, scissors).
beats(scissors, paper).
beats(paper, rock).

win(X, Y, 'You win') :- beats(X, Y).
win(X, Y, 'You lose') :- beats(Y, X).
win(X, X, 'Draw').

game(X) :-
    write('you chose '), writeln(X),
    random_member(Y, [rock, paper, scissors]), % computer
    write('prolog chose '), writeln(Y),
    win(X, Y, Result),
    writeln(Result).