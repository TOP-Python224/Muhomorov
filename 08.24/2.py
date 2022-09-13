def parse_sound_file(
        # КОММЕНТАРИЙ: полностью согласен
        # Параметр строго позиционный, т.к. путь к файлу выглядит самодостаточно, дополнять его именем параметра избыточно. Также нахождение его на 1-м месте среди параметров функции делает код более читаемым.
        file_path: str,
        /,
        *,
        # КОММЕНТАРИЙ: полностью согласен
        # Остальные параметры строго ключевые, т.к. все они цифровые и похожи между собой, в этом случае использование имени параметра делает код более читаемым.
        # ИСПРАВИТЬ: согласно условию, в эти параметры может быть передан как объект int, так и объект str — последнее полезно, например, когда вы читаете эти параметры из атрибутов файла, либо из базы данных, где они могут храниться как текст, и тому подобные случаи
        format: int | str,
        channels: int | str,
        sample_freq: int | str,
        bit_depth: int | str) -> str:
    """Проверяет корректность переданных аргументов и выдает результат по каждой проверке."""
    sample_freq_dir = (
        8000, 11025, 16000, 22050, 32000, 44100, 48000, 88200, 96000, 176400, 192000, 352800, 384000
    )
    bit_depth_dir = (8, 16, 24, 32)
    parse_result = ''
    
    if file_path and file_path.rsplit(sep=".", maxsplit=1)[1] == "wav": 
        parse_result += f"{file_path = } is Ok!\n"
    else:
        parse_result += f"{file_path = } is incorrect!\n"

    if 0 <= int(format) <= 999:
        parse_result += f"{format = } is Ok!\n"
    else:
        parse_result += f"{format = } is incorrect!\n"
    
    if 1 <= int(channels) <= 10:
        parse_result += f"{channels = } is Ok!\n"
    else:
        parse_result += f"{channels = } is incorrect!\n"

    if int(sample_freq) in sample_freq_dir:
        parse_result += f"{sample_freq = } is Ok!\n"
    else:
        parse_result += f"{sample_freq = } is incorrect!\n"
   
    if (bit_depth) in bit_depth_dir:
        parse_result += f"{bit_depth = } is Ok!\n"
    else:
        parse_result += f"{bit_depth = } is incorrect!\n"

    return parse_result


print(parse_sound_file(
    "/home/ioann/file.wav",
    format='77',
    channels=5,
    sample_freq='32000',
    bit_depth=24
))

print(parse_sound_file("/home/ioann/file.ogg", format=77, channels=5, sample_freq=32001, bit_depth=25))
print(parse_sound_file("/home/ioann/file.wav", 77 , 5, sample_freq=8000, bit_depth=24))


# stdout
# file_path = '/home/ioann/file.wav' is Ok!
# format = 77 is Ok!
# channels = 5 is Ok!
# sample_freq = 32000 is Ok!
# bit_depth = 24 is Ok!

# file_path = '/home/ioann/file.ogg' is incorrect!
# format = 77 is Ok!
# channels = 5 is Ok!
# sample_freq = 32001 is incorrect!
# bit_depth = 25 is incorrect!

# Traceback (most recent call last):
#   File "d:\Step\python\ДЗ\08.24\2.py", line 42, in <module>
#     print(parse_sound_file("/home/ioann/file.wav", 77, 5, sample_freq=8000, bit_depth=24))
# TypeError: parse_sound_file() takes 1 positional argument but 3 positional arguments (and 2 keyword-only arguments) were given


# ИТОГ: отлично! — 5/5
