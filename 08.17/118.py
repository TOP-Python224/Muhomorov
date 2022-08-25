from string import punctuation as puncts

text = input('Введите предложение: ')
clear_text = []

for word in text.split():
    clear_text += [word.lower().strip(puncts)]
    
rev_text = clear_text.copy()
rev_text.reverse()

if clear_text == rev_text: 
    print('Предложение является словесным палиндромом!')
else:
    print('Предложение НЕ является словесным палиндромом!')

# stdout:
# Введите предложение: Is1 it crazy: how saying sentences backwards creates backwards sentences, saying how crazy it is!
# Предложение НЕ является словесным палиндромом!

# Введите предложение: Is it crazy: how saying sentences backwards creates backwards sentences, saying how crazy it is!  
# Предложение является словесным палиндромом!