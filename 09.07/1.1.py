from random import choice

def gen_card_deck():
    """Генерирует упорядоченную колоду из 52 карт."""
    for suit in ('черви', 'бубны', 'пики', 'крести'):
        for value in range(1, 14):
            yield value, suit
card_deck = gen_card_deck()

def gen_card_deck_shuffled():
    """Генерирует перемашанную колоду из 52 карт."""
    cards = []
    for suit in ('черви', 'бубны', 'пики', 'крести'):
        for value in range(1, 14):
            cards.append((value, suit))
    for i in range(52):
        curr_card = choice(cards)
        cards.remove(curr_card)    
        yield curr_card
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
