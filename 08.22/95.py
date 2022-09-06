def toCap(text: str) -> str:
    """Функция озаглавливает необходимые буквы."""
    puncts = ('.', '!', '?')
    text = text.capitalize() + ' '

    clear_text = text.replace(' i', ' I').\
                      replace('i ', 'I ').\
                      replace('i.', 'I.').\
                      replace('i,', 'I,').\
                      replace('i!', 'I!').\
                      replace('i?', 'I?')

    text_lst = clear_text.split(' ')

    for word in text_lst:
        if word.endswith(puncts):
            text_lst[text_lst.index(word) + 1] = text_lst[text_lst.index(word) + 1].title()
    clear_text = ' '.join(text_lst)
    return clear_text.strip()


# Чувствую себя индусом)
# text = """what time do i have to be there? what’s the address? this time i’ll try to be on time! and i? i. yes, i, i!"""
text = input('Введите текст: ')
print(toCap(text))


# stdout:
# Введите текст: what time do i have to be there? what’s the address? this time i’ll try to be on time! and i? i. yes, i, i!
# What time do I have to be there? What’S the address? This time I’ll try to be on time! And I? I. Yes, I, I!