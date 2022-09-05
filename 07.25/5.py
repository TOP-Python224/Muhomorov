text = input('Введите текст: ')

text_norm = ''
word_cnt = {}
res = []

for chr in text:
    if chr.isalpha() or chr == ' ':
        text_norm += chr.lower()

for word in text_norm.split(' '):
    word_cnt[word] = word_cnt.setdefault(word, 0) + 1

min_val = min(word_cnt.values())

for key, value in word_cnt.items():
    if value == min_val:
        res.append(key)

print(sorted(res)[0])

# Введите текст: one, two, two, hello-bye, bad, good, Python, Python, Python
# bad

# Введите текст: И восстали машины из пепла ядерного огня, и началась война на уничтожение…
# война