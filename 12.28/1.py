from copy import deepcopy
from chess import *


class Game:
    """Опекун и инициатор."""
    def __init__(self):
        self.chessboard = Chessboard()
        self.turns = Turn()
        self.saves = Saves()
        self.saves[0] = deepcopy(self.chessboard)

    def turn(self, start_square: str, stop_square: str) -> None:
        """Осуществляет ход партии с сохранением хода и состояния игровой доски."""
        start_square = self.chessboard[start_square]
        stop_square = self.chessboard[stop_square]
        start_square.piece.move(stop_square)
        self.turns.save_turn(start_square, stop_square)
        self.saves.add_saves(deepcopy(self.chessboard))

    def print_turns(self) -> None:
        """Выводит список ходов партии."""
        print(self.turns)

    def restore_saves(self, turn: int) -> None:
        """Возвращает партию к началу заданного хода."""
        self.chessboard = self.saves[turn-1]
        for i in range(turn, len(self.turns)+1):
            self.turns.pop(i)
            self.saves.pop(i)


class Turn(dict):
    """Сохраняет ходы партии."""
    def __init__(self):
        super().__init__()
        self.turn_cnt = 1

    def save_turn(self,
                  start_square: Square,
                  end_square: Square) -> None:
        self.__setitem__(self.turn_cnt,
                         (end_square.piece,
                          str(start_square),
                          str(end_square)))
        self.turn_cnt += 1

    def __str__(self):
        result = ''
        for key, value in self.items():
            piece, start, end = value
            result += f"Ход №{key}: {repr(piece)} - {start} > {end}\n"
        return result


class Saves(dict):
    """Сохраняет состояние игровой доски."""
    def __init__(self):
        super().__init__()
        self.saves_cnt = 1

    def add_saves(self, chessboard: Chessboard):
        self.__setitem__(self.saves_cnt, chessboard)
        self.saves_cnt += 1


g1 = Game()
g1.turn('a2', 'a3')
g1.turn('a7', 'a6')
g1.turn('a3', 'a4')
g1.turn('a6', 'a5')
g1.turn('a4', 'a5')
g1.print_turns()
print(g1.chessboard['a'])
g1.restore_saves(4)
g1.print_turns()
print(g1.chessboard['a'])

# stdout:
# Ход №1: White Pawn - a2 > a3
# Ход №2: Black Pawn - a7 > a6
# Ход №3: White Pawn - a3 > a4
# Ход №4: Black Pawn - a6 > a5
# Ход №5: White Pawn - a4 > a5
#
# {1: <a1: White Rook>, 2: <a2: None>, 3: <a3: None>, 4: <a4: None>, 5: <a5: White Pawn>, 6: <a6: None>, 7: <a7: None>, 8: <a8: Black Rook>}
# Ход №1: White Pawn - a2 > a3
# Ход №2: Black Pawn - a7 > a6
# Ход №3: White Pawn - a3 > a4
#
# {1: <a1: White Rook>, 2: <a2: None>, 3: <a3: None>, 4: <a4: White Pawn>, 5: <a5: None>, 6: <a6: Black Pawn>, 7: <a7: None>, 8: <a8: Black Rook>}
