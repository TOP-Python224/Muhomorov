from copy import deepcopy
from chess import *


class Game:
    """Опекун и инициатор."""
    def __init__(self):
        self.chessboard = Chessboard()
        self.turns = Turn()
        self.saves = Saves()
        self.saves[0] = deepcopy(self.chessboard)
        ShowIcons.SHOW_ICON = True

    def turn(self, start_square: str, end_square: str) -> None:
        """Осуществляет ход партии с сохранением хода и состояния игровой доски."""
        start_square = self.chessboard[start_square]
        end_square = self.chessboard[end_square]
        self.chessboard.move(start_square, end_square)
        self.turns.save_turn(start_square, end_square)
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
            result += f"Ход №{key}: {piece} - {start} > {end}\n"
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
g1.turn('a2', 'a4')
g1.turn('b7', 'b5')
g1.turn('a4', 'b5')
g1.turn('g8', 'h6')
g1.turn('a1', 'a6')
g1.turn('e7', 'e5')
g1.turn('a6', 'h6')
g1.turn('e8', 'e7')
g1.turn('b2', 'b4')
g1.turn('e7', 'f6')
g1.turn('c1', 'b2')
g1.turn('f6', 'f5')
g1.turn('b2', 'e5')
g1.turn('d8', 'g5')
g1.turn('d1', 'c1')
g1.turn('g5', 'g2')
g1.print_turns()

# stdout:
# Ход №1: ♙ - a2 > a4
# Ход №2: ♟ - b7 > b5
# Ход №3: ♙ - a4 > b5
# Ход №4: ♘ - g8 > h6
# Ход №5: ♜ - a1 > a6
# Ход №6: ♟ - e7 > e5
# Ход №7: ♜ - a6 > h6
# Ход №8: ♔ - e8 > e7
# Ход №9: ♙ - b2 > b4
# Ход №10: ♔ - e7 > f6
# Ход №11: ♝ - c1 > b2
# Ход №12: ♔ - f6 > f5
# Ход №13: ♝ - b2 > e5
# Ход №14: ♕ - d8 > g5
# Ход №15: ♛ - d1 > c1
# Ход №16: ♕ - g5 > g2
