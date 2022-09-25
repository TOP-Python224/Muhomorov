from random import choice

def gen_card_deck():
    """Генерирует упорядоченную колоду из 52 карт."""
    for suit in ('черви', 'бубны', 'пики', 'крести'):
        for value in range(1, 14):
            yield value, suit

def gen_card_deck_shuffled():
    """Генерирует перемешанную колоду из 52 карт."""
    # ИСПОЛЬЗОВАТЬ: у вас ведь есть уже функция для упорядоченной колоды, используйте её — избегайте дублирования кода
    cards = list(gen_card_deck())
    for i in range(52):
        curr_card = choice(cards)
        cards.remove(curr_card)
        yield curr_card


card_deck = gen_card_deck()
card_deck_shuffled = gen_card_deck_shuffled()

print(card_deck.__next__())
print(card_deck.__next__())
print(card_deck.__next__(), end='\n\n')

print(card_deck_shuffled.__next__())
print(card_deck_shuffled.__next__())
print(card_deck_shuffled.__next__())


# stdout:
# (1, 'черви')
# (2, 'черви')
# (3, 'черви')

# (3, 'бубны')
# (5, 'бубны')
# (9, 'черви')


# ИТОГ: очень хорошо — 5/6
