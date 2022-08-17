text = input('Введите текст телеграммы: ')
text_clear = ''

for ch in text:
    if ' ' not in ch:
        text_clear += ch

price = (len(text_clear) * 80)
print(f"{price // 100} руб. {price % 100} коп.")



    