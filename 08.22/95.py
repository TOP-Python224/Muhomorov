from string import punctuation, whitespace
import re 

# ИСПРАВИТЬ: имена функция мы даём в нижнем регистре, разделяя слова в имени символом подчёркивания — это называется snake_lower_case
# КОММЕНТАРИЙ: на Стивенсона внимания не обращайте, он вообще не очень хорошо Python знает ))
def to_cap(text: str) -> str:
    """Функция озаглавливает необходимые буквы."""
    puncts = ('.', '!', '?')
    # ИСПРАВИТЬ: а если первый символ — это пробел? (см. тесты ниже) используйте строковый метод strip()
    text = text.strip().capitalize() + ' '

    # ИСПРАВИТЬ: боюсь, что такой способ замены себя не оправдывает (см. тесты ниже)
    # Гулять так гулять )
    clear_text = re.sub(r'\bi([’\']?)\b', r'I\1', text)
    # КОММЕНТАРИЙ: по-хорошему, здесь, конечно, нужна регулярка — но это не значит, что нельзя справиться без неё: вам нужно рассмотреть все случаи, когда I является самостоятельным словом, но при этом может быть окружено символами пространства и знаками препинания
    # ИСПОЛЬЗОВАТЬ: если бы мне было пофиг на производительность — а в этой задаче с короткими фразами на неё явно можно забить — то я бы написал что-то вроде такого перебора:
    # clear_text = text
    # for start_char in punctuation + whitespace:
    #     for end_char in punctuation + whitespace:
    #         substr = f'{start_char}i{end_char}'
    #         replace = f'{start_char}I{end_char}'
    #         clear_text = clear_text.replace(substr, replace)

    text_lst = clear_text.split(' ')

    for word in text_lst:
        if word.endswith(puncts):
            # ИСПРАВИТЬ: метод title() считает последовательности буквенных символов, разделённые только знаком препинания, отдельными словами — именно поэтому у вас появляется What’S в исходном примере — лучше использовать capitalize()
            text_lst[text_lst.index(word) + 1] = text_lst[text_lst.index(word) + 1].capitalize()
    clear_text = ' '.join(text_lst)
    return clear_text.strip()


# Чувствую себя индусом)
# text = """what time do i have to be there? what’s the address? this time i’ll try to be on time! and i? i. yes, i, i!"""
text = input('Введите текст: ')
print(to_cap(text))

# stdout:
# Введите текст: what time do i have to be there? what’s the address? this time i’ll try to be on time! and i? i. yes, i, i!
# What time do I have to be there? What’S the address? This time I’ll try to be on time! And I? I. Yes, I, I!

# СДЕЛАТЬ: тесты, ещё раз тесты, и снова тесты — с разными входными данными — и вы увидите много удивительного
# Введите текст: call for taxi
# Call for taxI

# Введите текст:  two glasses of martini, please.
# two glasses of martinI, please.

# Введите текст: он сказал: "i'll be back" — и ушёл
# Он сказал: "i'll be back" — и ушёл

# stdout2:
# Введите текст: call for taxi
# Call for taxi

# Введите текст:  two glasses of martini, please.
# Two glasses of martini, please.

# Введите текст: он сказал: "i'll be back" — и ушёл
# Он сказал: "I'll be back" — и ушёл

# Введите текст:   - i'll go to long island 
# - I'll go to long island

# ИТОГ: так-то код неплохой, но дотошности не хватило — 4/7
