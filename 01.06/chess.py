from pprint import pprint
from typing import Optional

from dataclasses import dataclass
from enum import Enum
from string import ascii_lowercase as a_lc

import re

# SHOW_ICON = False
# SHOW_ICON = True


class ShowIcons:
    """Переключатель строкового представления фигур: False - выводить в буквенном обозначении, True - в символьном."""
    SHOW_ICON = False


class SquareColor(int, Enum):
    """Цвет поля на доске."""
    LIGHT = 0
    DARK = 1


class PieceColor(Enum):
    """Цвет фигуры."""
    WHITE = 0
    BLACK = 1


class PieceKind(Enum):
    """Вид фигуры."""
    KING = 0
    QUEEN = 1
    ROOK = 2
    BISHOP = 3
    KNIGHT = 4
    PAWN = 5


class PieceIcon(Enum):
    """Иконки фигур."""
    KING = ('♚', '♔')
    QUEEN = ('♛', '♕')
    ROOK = ('♜', '♖')
    BISHOP = ('♝', '♗')
    KNIGHT = ('♞', '♘')
    PAWN = ('♙', '♟')


@dataclass
class Piece:
    """Описывает сущность фигуры."""
    color: PieceColor
    kind: PieceKind
    square: Optional['Square']
    icon: str = None

    def __post_init__(self):
        self.removed: bool = False

    def __del__(self):
        """Удаляет фигуру с поля."""
        self.square.piece = None
        self.square = None
        self.removed = True
    
    def __repr__(self):
        return f'{self.color.name.title()} {self.kind.name.title()}'
    
    def __str__(self):
        return self.icon if ShowIcons.SHOW_ICON \
            else self.color.name[0] + self.kind.name[0]

    # def move(self, end_square: 'Square') -> None:
    #     """Осуществляет проверку, ход фигуры и взятие фигуры противника."""
    #     if self.check_move(end_square):
    #         if end_square.piece is not None:
    #             if end_square.piece.color is self.color:
    #                 raise Exception('недопустимый ход')
    #             else:
    #                 del end_square.piece
    #         self.square.piece = None
    #         self.square = end_square
    #         end_square.piece = self
    #     else:
    #         raise Exception('недопустимый ход')

    # def check_move(self, end_square: 'Square') -> bool:
    #     turn_len = self.square - end_square
    #     match self.kind:
    #         case PieceKind.PAWN:
    #             if self.square.rank == ('2', '7')[self.color.value()]:
    #                 if turn_len in ((-1, -2), (1, 2))[self.color.value()]:
    #                     return True
    #                 elif turn_len in ((9, -11), (-9, 11))[self.color.value()]:
    #                     return True
    #             else:
    #                 if turn_len == (-1, 1)[self.color.value()]:
    #                     return True
    #             return False
    #
    #         case PieceKind.ROOK:
    #             if self.square.file == end_square.file \
    #                     or self.square.rank == end_square.rank:
    #                 return True
    #             return False
    #
    #         case PieceKind.KNIGHT:
    #             if abs(turn_len) in (8, 12, 19, 21):
    #                 return True
    #             return False
    #
    #         case PieceKind.BISHOP:
    #             if abs(turn_len) % 9 == 0 \
    #                     or abs(turn_len) % 11 == 0:
    #                 return True
    #             return False
    #
    #         case PieceKind.KING:
    #             if abs(turn_len) in (1, 9, 10, 11):
    #                 return True
    #             return False
    #
    #         case PieceKind.QUEEN:
    #             if self.square.file == end_square.file \
    #                     or self.square.rank == end_square.rank \
    #                     or abs(turn_len) % 9 == 0 \
    #                     or abs(turn_len) % 11 == 0:
    #                 return True
    #             return False


@dataclass
class Square:
    """Описывает сущность поля."""
    color: SquareColor
    file: str
    rank: str
    piece: Optional[Piece] = None
    
    def __repr__(self):
        return f'<{self.file + self.rank}: {self.piece!r}>'
    
    def __str__(self):
        return self.file + self.rank

    def __sub__(self, other: 'Square') -> int:
        start = str(a_lc.index(self.file) + 1) + self.rank
        end = str(a_lc.index(other.file) + 1) + other.rank
        # print(f"({self}=>{int(start)}) - ({other}=>{int(end)}) = {int(start)-int(end)}")
        return int(start) - int(end)


class Chessboard(dict):
    """Описывает сущность игровой доски."""

    class File(dict):
        """Вертикаль игровой доски."""
        def __init__(self, file: str, start_color: SquareColor):
            super().__init__()
            for i in range(4):
                for j in range(2):
                    rank = i*2 + j + 1
                    self[rank] = Square(
                        list(SquareColor)[start_color-j],
                        file,
                        str(rank)
                    )
    
    def __init__(self):
        """Создаёт и нумерует игровою доску и заполняет её пустыми полями соответствующих цветов."""
        super().__init__()
        for i in range(8):
            for _ in range(4):
                for j in range(2):
                    self[a_lc[i]] = self.__class__.File(a_lc[i], list(SquareColor)[j-i % 2])
        self.__post_init__()
    
    def __post_init__(self):
        """Расставляет фигуры на игровой доске в начальную позицию."""
        self['a1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['a1'],
                                 PieceIcon.ROOK.value[PieceColor.WHITE.value])
        self['b1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['b1'],
                                 PieceIcon.KNIGHT.value[PieceColor.WHITE.value])
        self['c1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['c1'],
                                 PieceIcon.BISHOP.value[PieceColor.WHITE.value])
        self['d1'].piece = Piece(PieceColor.WHITE, PieceKind.QUEEN, self['d1'],
                                 PieceIcon.QUEEN.value[PieceColor.WHITE.value])
        self['e1'].piece = Piece(PieceColor.WHITE, PieceKind.KING, self['e1'],
                                 PieceIcon.KING.value[PieceColor.WHITE.value])
        self['f1'].piece = Piece(PieceColor.WHITE, PieceKind.BISHOP, self['f1'],
                                 PieceIcon.BISHOP.value[PieceColor.WHITE.value])
        self['g1'].piece = Piece(PieceColor.WHITE, PieceKind.KNIGHT, self['g1'],
                                 PieceIcon.KNIGHT.value[PieceColor.WHITE.value])
        self['h1'].piece = Piece(PieceColor.WHITE, PieceKind.ROOK, self['h1'],
                                 PieceIcon.ROOK.value[PieceColor.WHITE.value])
        for rank in a_lc[:8]:
            self[rank][2].piece = Piece(PieceColor.WHITE, PieceKind.PAWN, self[rank][2],
                                        PieceIcon.PAWN.value[PieceColor.WHITE.value])
        self['a8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['a8'],
                                 PieceIcon.ROOK.value[PieceColor.BLACK.value])
        self['b8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['b8'],
                                 PieceIcon.KNIGHT.value[PieceColor.BLACK.value])
        self['c8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['c8'],
                                 PieceIcon.BISHOP.value[PieceColor.BLACK.value])
        self['d8'].piece = Piece(PieceColor.BLACK, PieceKind.QUEEN, self['d8'],
                                 PieceIcon.QUEEN.value[PieceColor.BLACK.value])
        self['e8'].piece = Piece(PieceColor.BLACK, PieceKind.KING, self['e8'],
                                 PieceIcon.KING.value[PieceColor.BLACK.value])
        self['f8'].piece = Piece(PieceColor.BLACK, PieceKind.BISHOP, self['f8'],
                                 PieceIcon.BISHOP.value[PieceColor.BLACK.value])
        self['g8'].piece = Piece(PieceColor.BLACK, PieceKind.KNIGHT, self['g8'],
                                 PieceIcon.KNIGHT.value[PieceColor.BLACK.value])
        self['h8'].piece = Piece(PieceColor.BLACK, PieceKind.ROOK, self['h8'],
                                 PieceIcon.ROOK.value[PieceColor.BLACK.value])
        for rank in a_lc[:8]:
            self[rank][7].piece = Piece(PieceColor.BLACK, PieceKind.PAWN, self[rank][7],
                                        PieceIcon.PAWN.value[PieceColor.BLACK.value])
    
    def __rank(self, number) -> list[Square]:
        """Возвращает горизонталь игровой доски."""
        return [file[number] for file in self.values()]
    
    def __getitem__(self, key: str | int):
        """Обеспечивает вариативный доступ к полям игровой доски."""
        if re.match(r'^[a-h][1-8]$', key := str(key).lower()):
            return super().__getitem__(key[0])[int(key[1])]
        elif re.match(r'^[a-h]$', key):
            return super().__getitem__(key)
        elif re.match(r'^[1-8]$', key):
            return self.__rank(int(key))
        else:
            raise KeyError

    def move(self, start_square: 'Square', end_square: 'Square') -> None:
        """Осуществляет проверку, ход фигуры и взятие фигуры противника."""
        if self.check_move(start_square, end_square):
            if end_square.piece is not None:
                if end_square.piece.color is start_square.piece.color:
                    raise Exception('нельзя есть свою фигуру')
                else:
                    del end_square.piece
            end_square.piece = start_square.piece
            end_square.piece.square = end_square
            start_square.piece = None
        else:
            raise Exception('недопустимый ход')

    def check_move(self, start_square: 'Square', end_square: 'Square') -> bool:
        """Проверяет возможность хода для видов фигур."""
        turn_len = start_square - end_square

        match start_square.piece.kind:
            case PieceKind.PAWN:
                if turn_len in ((9, -11), (-9, 11))[start_square.piece.color.value] \
                     and end_square.piece is not None:
                    return True

                elif turn_len == (-2, 2)[start_square.piece.color.value]:
                    next_square = start_square.file \
                                  + str(int(start_square.rank)
                                        + (1, -1)[start_square.piece.color.value])
                    if start_square.rank == ('2', '7')[start_square.piece.color.value]:
                        if self[next_square].piece is None:
                            return True

                elif turn_len == (-1, 1)[start_square.piece.color.value]:
                    return True

                return False

            case PieceKind.ROOK:
                return self.check_line(start_square, end_square, turn_len)

            case PieceKind.KNIGHT:
                return abs(turn_len) in (8, 12, 19, 21)

            case PieceKind.BISHOP:
                return self.check_diagonal(start_square, turn_len)

            case PieceKind.KING:
                return abs(turn_len) in (1, 9, 10, 11)

            case PieceKind.QUEEN:
                return self.check_diagonal(start_square, turn_len) \
                       or self.check_line(start_square, end_square, turn_len)

    def check_diagonal(self, start_square: 'Square', turn_len: int) -> bool:
        """Проверяет диагональ между началом и концом хода на отсутствие фигур."""
        curr_diagonal = []
        div_9 = divmod(turn_len, 9)
        div_11 = divmod(turn_len, 11)

        if div_9[1] == 0:
            # turn_up_left
            if div_9[0] > 0:
                for i in range(1, div_9[0]):
                    curr_diagonal += [self[a_lc[a_lc.index(start_square.file) - i]
                                           + str(int(start_square.rank) + i)].piece]
                return not any(curr_diagonal)

            # turn_down_right
            elif div_9[0] < 0:
                for i in range(1, abs(div_9[0])):
                    curr_diagonal += [self[a_lc[a_lc.index(start_square.file) + i]
                                           + str(int(start_square.rank) - i)].piece]
                return not any(curr_diagonal)

        if div_11[1] == 0:
            # turn_up_right
            if div_11[0] < 0:
                for i in range(1, abs(div_11[0])):
                    curr_diagonal += [self[a_lc[a_lc.index(start_square.file) + i]
                                           + str(int(start_square.rank) + i)].piece]
                return not any(curr_diagonal)

            # turn_down_left
            elif div_11[0] > 0:
                for i in range(1, div_11[0]):
                    curr_diagonal += [self[a_lc[a_lc.index(start_square.file) - i]
                                           + str(int(start_square.rank) - i)].piece]
                return not any(curr_diagonal)

        return False

    def check_line(self, start_square: 'Square', end_square: 'Square', turn_len: int) -> bool:
        """Проверяет линию между началом и концом хода на отсутствие фигур."""
        if start_square.file == end_square.file:
            curr_file = [s.piece for s in self[start_square.file].values()]
            # turn_up
            if turn_len < 0:
                return not any(curr_file[int(start_square.rank): int(end_square.rank)-1])

            # turn_down
            elif turn_len > 0:
                return not any(curr_file[int(start_square.rank)-2: int(end_square.rank)-1: -1])

        elif start_square.rank == end_square.rank:
            curr_rank = [s.piece for s in self[start_square.rank]]
            # turn_right
            if turn_len < 0:
                return not any(curr_rank[a_lc.index(start_square.file)+1: a_lc.index(end_square.file)])

            # turn_left
            elif turn_len > 0:
                return not any(curr_rank[a_lc.index(start_square.file)-1: a_lc.index(end_square.file): -1])

        return False
