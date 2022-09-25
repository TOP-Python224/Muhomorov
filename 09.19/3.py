from pathlib import Path

directory = Path('./# TestFolder')
keywords_file = Path('./# keywords.txt')
result = []

# Приложение состоит из 3-х функций: get_txt_files находит текстовые файлы в заданном каталоге, get_keywords считывает ключевые слова из заданного файла, find_keywords производит поиск ключевых слов в текстовых файлах и выводит результат. На мой взгяд так нииболее логично: одна функция работает с файлами, другая с ключевыми словами, третья используя результаты первых двух осуществляет поиск и вывод. Каждую из функций при необходимости можно отдельно дорабатывать. Также код выглядит менее горомоздким.

def get_txt_files(directory: Path) -> list[str]:
    """Выводит список текстовых файлов в принятом каталоге."""
    txt_files = []
    for elem in directory.iterdir():
        if Path.is_file(elem) and elem.match('*.txt'):
            txt_files += [directory / elem.name]
    return txt_files

def get_keywords(keywords_file: Path) -> list[str]:
    """Выводит список ключевых слов из принятого файла."""
    with open(keywords_file, encoding = 'utf-8') as file:
        keywords = []
        for line in file:
            for word in line.split():
                keywords += [word]
    return keywords

def find_keywords(directory: Path, keywords_file: Path, n = 0) -> list:
    """Выводит список словарей, содержащих данные о текстовых файлах, в которых найдены ключевые слова.
    :param directory: каталог с текстовыми файлами
    :param keywords_file: файл с ключевыми словами
    :param n: глубина сохраняемого контекста, n строк перед и n строк после строки, содержащей ключевое слово, по умолчанию 0.
    """
    for txt_file in get_txt_files(directory):
        with open(txt_file, encoding = 'utf-8') as file:
            text = file.readlines()
        for keyword in get_keywords(keywords_file):
            line_index = -1
            for line in text:
                line_index += 1
                for word in line.split():
                    if word.startswith(keyword):
                        start_pos = line_index - n
                        stop_pos = line_index + n + 1
                        if start_pos < 0: start_pos = 0
                        result.append({'filename': file.name, 
                                    'line_number': line_index, 
                                    'keyword': keyword, 
                                    'context': n, 
                                    'text': text[start_pos: stop_pos]})
    return result

print(find_keywords(directory, keywords_file, n=2))

# [{'filename': '# TestFolder\\E3ln1.txt', 'line_number': 14, 'keyword': 'закон', 'context': 2, 'text': ['- Лучше всего мне даётся магия земли, если ты о стихии. Но я умею оперировать и другими элементами, а также немного владею магией иллюзий. Всему этому ты тоже можешь научиться, если примешь моё предложение.\n', '- Научится... а что за предложение?\n', '- Дело в том, что дикие маги вне закона. Они опасны как для окружающих, так и для себя. Поэтому я и подобные мне люди ищем таких магов, чтобы отправить их на обучение. Это не бесплатно, придётся отработать. Но если будешь усердно учиться, то это не займёт много времени. Кроме того, все маги должны пройти регистрацию у жрецов, но на это можешь не обращать внимания. Обычная формальность.\n', '- А что такое дикий маг? Может я не дикий?\n', '- Ахаха, насмешил. Вот скажи, ты обучение проходил? Нет! Значит, ты дикий маг.\n']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 19, 'keyword': 'закон', 'context': 2, 'text': ['- Но у меня память отшибло, может я учился!\n', '- Ладно, допустим даже так, но ты должен это доказать. Ты должен сдать базовый экзамен, чтобы получить права, - угу, значит, выбора 
# у меня нет и не было.\n', '- Не хочу я работать ради кого-то из-за каких-то глупых законов, - проворчал я.\n', '- Поверь мне, мне это тоже не нравится. Но если ты будешь упрямиться, то это лишь подтвердит то, что дикие маги опасны. Всего-то и надо, что научиться необходимому минимуму, да подтвердить свои права перед Творцом. Всё. Остальное - не самая обременительная часть в виде отработки затраченных на твоё обучение усилий. Понятно?\n', '- Да я понимаю. Необходимость подобных законов мне ясна. Что от меня требуется.\n']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 
# 21, 'keyword': 'закон', 'context': 2, 'text': ['- Не хочу я работать ради кого-то из-за каких-то глупых законов, - проворчал я.\n', '- Поверь мне, мне это тоже не нравится. Но если ты будешь упрямиться, то это лишь подтвердит то, что дикие маги опасны. Всего-то и надо, что научиться необходимому минимуму, да подтвердить свои права перед Творцом. Всё. Остальное - не самая обременительная часть в виде отработки затраченных на твоё обучение усилий. Понятно?\n', '- Да я понимаю. Необходимость подобных законов мне ясна. Что от меня требуется.\n', '- Ничего особенного. Сейчас я познакомлю тебя с Хинтоном, жрецом создателя. Он подтвердит перед Творцом твоё желание стать законопослушным магом, пройти обучение и регистрацию.\n', 
# '- Понятно, - я постучал пальцами по столу. - А почему местные себя так странно ведут?\n']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 22, 'keyword': 'закон', 'context': 2, 'text': ['- Поверь мне, мне это тоже не нравится. Но если ты будешь упрямиться, то это лишь подтвердит то, что дикие маги опасны. Всего-то и надо, что научиться необходимому минимуму, да подтвердить свои права перед Творцом. Всё. Остальное - не самая обременительная часть в виде отработки затраченных на твоё обучение усилий. Понятно?\n', '- Да я понимаю. Необходимость подобных законов мне ясна. 
# Что от меня требуется.\n', '- Ничего особенного. Сейчас я познакомлю тебя с Хинтоном, жрецом создателя. Он подтвердит перед Творцом твоё желание стать законопослушным магом, пройти обучение и регистрацию.\n', '- Понятно, - я постучал пальцами по столу. - А почему местные себя так странно ведут?\n', '- Потому, что счастливы, - маг пожал плечами.\n']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 9, 'keyword': 'ум', 'context': 2, 'text': ['- Что ты можешь? Обычно маги обладают какими-то склонностями к определённой стихии. Например, легче удаётся зажигать огонь, залечивать раны, создавать свет или что-то ещё. Что можешь ты?\n', '"Убивать всё вокруг", - мысленно проворчал я. Тут я точно - спец. Если что-то живое, то мне даже никаких усилий прикладывать не надо. Почти.\n', '- Ну, я могу зажечь огонь, - я почесал макушку, старательно изображая усиленный мыслительный процесс и недалёкий ум одновременно. - А ещё могу его погасить, наверное.\n', '- Понятно. Скорее всего, у тебя склонность к огню. Надеюсь, 
# ты контролируешь свою способность? А то можно случайно что-то сжечь, если быть неосторожным.\n', '- Да, конечно! Чтобы зажечь надо коснуться, но на мне одежа же не горит! - рассмеялся я. - А ты что умеешь?\n']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 11, 'keyword': 'ум', 'context': 2, 'text': ['- Ну, я могу зажечь огонь, - я почесал макушку, старательно изображая усиленный мыслительный процесс и недалёкий ум одновременно. - А ещё могу его погасить, наверное.\n', '- Понятно. Скорее всего, у тебя склонность к огню. Надеюсь, ты контролируешь свою способность? А то 
# можно случайно что-то сжечь, если быть неосторожным.\n', '- Да, конечно! Чтобы зажечь надо коснуться, но на мне одежа же не горит! - рассмеялся я. - А ты что умеешь?\n', '- Лучше всего мне даётся магия земли, если ты о стихии. Но я умею оперировать и другими элементами, а также немного владею магией иллюзий. Всему этому ты тоже можешь научиться, если примешь моё предложение.\n', '- Научится... а что за предложение?\n']}, {'filename': 
# '# TestFolder\\E3ln1.txt', 'line_number': 12, 'keyword': 'ум', 'context': 2, 'text': ['- Понятно. Скорее всего, у тебя склонность к огню. Надеюсь, ты контролируешь свою способность? А то можно случайно что-то сжечь, если быть неосторожным.\n', '- Да, конечно! Чтобы зажечь надо коснуться, но 
# на мне одежа же не горит! - рассмеялся я. - А ты что умеешь?\n', '- Лучше всего мне даётся магия земли, если ты о стихии. Но я умею оперировать и 
# другими элементами, а также немного владею магией иллюзий. Всему этому ты тоже можешь научиться, если примешь моё предложение.\n', '- Научится... 
# а что за предложение?\n', '- Дело в том, что дикие маги вне закона. Они опасны как для окружающих, так и для себя. Поэтому я и подобные мне люди ищем таких магов, чтобы отправить их на обучение. Это не бесплатно, придётся отработать. Но если будешь усердно учиться, то это не займёт много времени. Кроме того, все маги должны пройти регистрацию у жрецов, но на это можешь не обращать внимания. Обычная формальность.\n']}, {'filename': '# 
# TestFolder\\E3ln1.txt', 'line_number': 1, 'keyword': 'вопрос', 'context': 2, 'text': ['- Язык - незнаком. Местность тоже незнакома, да и местные не отличаются дружелюбием. Вот и думаю, кто я такой и откуда взялся, - усмехнулся я, допивая порцию вина.\n', '- Не думаю, что у меня есть ответ на этот вопрос. Но я знаю тех, кто может знать. Я ученик великого мага, известного как Хантирский Старец...\n', '- Мага? - перебил я его. - Что такое маг? Я незнаком с таким словом, что оно означает?\n', '- Я - маг. Ты - тоже маг, только дикий. Смотри, - он сформировал над ладонью шарик белого света. - Полагаю, именно магия позволила выжить тебе в лесу, а не навыки егеря.\n']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 28, 
# 'keyword': 'вопрос', 'context': 2, 'text': ['- Именно. Это часть праздника Благодарения Создателя.\n', '- Надеюсь, меня в нём участвовать не заставят?\n', '- Нет, это абсолютно добровольный праздник. Жрецы никого насильно не тянут, - поморщился маг. - В этих вопросах они довольно щепетильны.\n', '- Я согласен. Но можешь пока рассказать ещё, что знаешь? Как проходит обучение, чему учат. Сколько вообще стоит это обучение и как придётся 
# отрабатывать?\n', '- Ну, - маг налил себе ещё вина, - могу. Только я учился так недолго: меня взял в учителя сам Разхор, великий Хантирский Старец!']}, {'filename': '# TestFolder\\E3ln1.txt', 'line_number': 20, 'keyword': 'вид', 'context': 2, 'text': ['- Ладно, допустим даже так, но ты должен это доказать. Ты должен сдать базовый экзамен, чтобы получить права, - угу, значит, выбора у меня нет и не было.\n', '- Не хочу я работать ради 
# кого-то из-за каких-то глупых законов, - проворчал я.\n', '- Поверь мне, мне это тоже не нравится. Но если ты будешь упрямиться, то это лишь подтвердит то, что дикие маги опасны. Всего-то и надо, что научиться необходимому минимуму, да подтвердить свои права перед Творцом. Всё. Остальное - не самая обременительная часть в виде отработки затраченных на твоё обучение усилий. Понятно?\n', '- Да я понимаю. Необходимость подобных законов мне ясна. Что от меня требуется.\n', '- Ничего особенного. Сейчас я познакомлю тебя с Хинтоном, жрецом создателя. Он подтвердит перед Творцом твоё 
# желание стать законопослушным магом, пройти обучение и регистрацию.\n']}, {'filename': '# TestFolder\\le1UO.txt', 'line_number': 21, 'keyword': 'план', 'context': 2, 'text': ['То сразу становится легче.\n', 'Во-первых, дело откладывается,\n', 'Во-вторых, создается план действий,\n', 'В-третьих, появляется радость от того, что можно будет сделать так много дел.\n', '  \n']}, {'filename': '# TestFolder\\le1UO.txt', 'line_number': 8, 'keyword': 'инструмент', 'context': 2, 'text': ['Чтобы мы не делали, надо помнить, что мы делаем это ради блага\n', 'Нашего мира, наших близких и во 
# славу Бога.\n', 'Когда мы берем и используем инструмент, то хочется относится к нему, как к врагу,\n', 'Которого надо победить.\n', 'Так поступать ни в коем случае не надо.\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 10, 'keyword': 'акт', 'context': 2, 'text': ['И Анастасия 
# неожиданно застонала.\n', '- Жора... Жора... о...о...о...\n', 'Так она стонала во время постельной сцены в глупом Екатерининском сериале. Правда, 
# сама не снималась, отказалась наотрез. А вот голос остался её. Ничего, зритель проглотил и дублершу. Хан в удивлении смотрел на актрису. Та же вдруг прыгнула на него, повисла, обхватив ногами поясницу. Жора чуть не упал, хорошо, что перила помешали.\n', '- Да, потрясись ты что ли, - сердито 
# прошептала женщина между стонами. - и держи меня, а то свалюсь.\n', 'Жора невольно хохотнул. Анастасия стонала:\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 16, 'keyword': 'акт', 'context': 2, 'text': ['Плечи Хана заходили ходуном, он молча и неистово хохотал, только иногда какое-то непонятное фырканье вырывалось из его губ. Анастасия шепнула между стонами:\n', '- И так сойдет. Матушка за оргазм посчитает...\n', 'Мамаша шарахнулась, увидев сына с актрисой в двусмысленной позе, женщина обхватывала его ногами, он держал её за плечи, а когда услышала непонятные звуки, то ли пыхтение, то ли стоны, то моментально скрылась в доме.\n', '- Теперь и сплетничать не надо, - заметила Анастасия после исчезновения матушки, освобождая от своих нелепых объятий мужчину.\n', 'Хан хохотал.\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 27, 'keyword': 'акт', 'context': 2, 'text': ['- Сам расскажешь, если надо будет. Только...\n', '- Что только?\n', '- Все остальные наши половые акты только в комнате, и без свидетелей. Я не хочу больше висеть на тебе даже в джинсах, - решительно выпалила Анастасия.']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 0, 'keyword': 'ум', 'context': 2, 'text': ['Актриса внимательно смотрела на мужчину и ни о чем больше не спрашивала. В её глазах светились воля и ум. Жора понял: эта женщина умеет не задавать лишних вопросов. Он тихо и медленно сказал:\n', '- Для начала сделай так, чтобы все 
# узнали, что я уже переспал с тобой. Прямо здесь, в беседке.\n', 'Анастасия подняла на Хана вопросительные глаза. Но тут же заставила замолчать все свои чувства.\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 0, 'keyword': 'ум', 'context': 2, 'text': ['Актриса внимательно смотрела на мужчину и ни о чем больше не спрашивала. В её глазах светились воля и ум. Жора понял: эта женщина умеет не задавать лишних вопросов. Он тихо и медленно сказал:\n', '- Для начала сделай так, чтобы все узнали, что я уже переспал с тобой. Прямо здесь, в беседке.\n', 'Анастасия подняла на 
# Хана вопросительные глаза. Но тут же заставила замолчать все свои чувства.\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 7, 'keyword': 'ум', 'context': 2, 'text': ['Теперь глаза женщины стали круглыми, удивленными. Она явно чего-то не понимала.\n', '- А вот и моя матушка на горизонте. Любопытно старой холере. Сейчас я её назад отправлю. Свидетели нам не нужны, - решил Хан. - Пусть все гадают, для чего мы уединились.\n', '- Погоди, - зеленые глаза женщины загорелись озорством. - Сама матушка сейчас уйдет, уметелит одним моментом.\n', 'И Анастасия неожиданно застонала.\n', '- Жора... Жора... о...о...о...\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 0, 'keyword': 'вопрос', 'context': 2, 'text': ['Актриса внимательно смотрела на мужчину и ни о чем больше не спрашивала. В её глазах светились воля и ум. Жора понял: эта женщина умеет не задавать лишних вопросов. Он тихо и медленно сказал:\n', '- Для начала сделай так, чтобы все узнали, что я уже переспал с тобой. Прямо здесь, в беседке.\n', 'Анастасия подняла на Хана вопросительные глаза. Но тут же заставила замолчать все свои чувства.\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 2, 'keyword': 'вопрос', 'context': 2, 'text': ['Актриса внимательно смотрела на мужчину и ни о чем больше не спрашивала. В её 
# глазах светились воля и ум. Жора понял: эта женщина умеет не задавать лишних вопросов. Он тихо и медленно сказал:\n', '- Для начала сделай так, чтобы все узнали, что я уже переспал с тобой. Прямо здесь, в беседке.\n', 'Анастасия подняла на Хана вопросительные глаза. Но тут же заставила замолчать все свои чувства.\n', '- Мне раздеваться полностью? Или только трусы снять? - спокойно осведомилась она.\n', '- Нет, оставайся в одежде, - в 
# тон ей также спокойно проговорил Жора. - Тебе надо только всем натрепать. Пусть все думают, что я сплю с тобой. Больше ничего не надо. Никогда не 
# будет надо.\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 22, 'keyword': 'вид', 'context': 2, 'text': ['Но хан не мог остановиться:\n', '- Я же в штанах был! А ты в джинсах.\n', '- Ничего, - констатировала Анастасия. - Нас было видно только выше пояса. Матушка должна проглотить первую серию нашей любви. Идем к остальным. Да, сделай утомленно-довольный вид...\n', 'Но Хан остановил её:\n', '- А ты спросить ни о чем не хочешь?\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 22, 'keyword': 'вид', 'context': 2, 'text': ['Но хан не мог остановиться:\n', '- Я же в штанах был! А ты в джинсах.\n', '- Ничего, - констатировала Анастасия. - Нас было видно только выше пояса. Матушка должна проглотить первую серию нашей любви. Идем к остальным. Да, сделай утомленно-довольный вид...\n', 'Но Хан остановил её:\n', '- А ты спросить ни о чем не хочешь?\n']}, {'filename': '# TestFolder\\r62Bf.txt', 'line_number': 4, 'keyword': 'тон', 'context': 2, 'text': ['Анастасия подняла на Хана вопросительные глаза. Но тут же заставила замолчать все свои чувства.\n', '- Мне раздеваться полностью? Или только трусы снять? - спокойно осведомилась она.\n', '- Нет, оставайся в одежде, - в тон ей также спокойно проговорил Жора. - Тебе надо только всем натрепать. Пусть все думают, что я сплю с тобой. Больше ничего не надо. Никогда не будет надо.\n', 'Теперь глаза женщины стали круглыми, удивленными. Она явно чего-то не понимала.\n', '- А вот и моя матушка на горизонте. Любопытно старой холере. Сейчас я её назад отправлю. Свидетели нам не нужны, - решил Хан. - Пусть все гадают, для чего мы уединились.\n']}]