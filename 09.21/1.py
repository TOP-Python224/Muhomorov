from pathlib import Path
from sys import path, modules
from importlib.util import spec_from_file_location, module_from_spec


script_dir = Path(path[0])
module_path = script_dir / '1_2.py'
spec = spec_from_file_location('module_for_print_msg', module_path)
print_mod = module_from_spec(spec)
modules['digit_name_module'] = print_mod
spec.loader.exec_module(print_mod)


while True:
    cmd, sep, msg = input('Введите команду msg, затем через пробел ваше сообщение, либо команду quit для выхода: ').partition(' ')
    if cmd == 'msg':
        print_mod.important_message(msg)
    elif cmd == 'quit':
        break
    else:
        raise ValueError('Введена некорректная команда!')


# stdout:
# Введите команду msg, затем через пробел ваше сообщение, либо команду quit для выхода: quit

# Введите команду msg, затем через пробел ваше сообщение, либо команду quit для выхода: exit
# Traceback (most recent call last):
#   File "d:\Step\python\ДЗ\09.21\1.py", line 19, in <module>
#     raise ValueError('Введена некорректная команда!')
# ValueError: Введена некорректная команда!

# Введите команду msg, затем через пробел ваше сообщение, либо команду quit для выхода: msg Now you're looking at the very important message from the team of the developers of this miraculous script
#=========================================================================================================================================================#
#                                                                                                                                                         #
#  Now you're looking at the very important message from the team of the developers of this miraculous script                                             #
#                                                                                                                                                         #
#=========================================================================================================================================================#

# Введите команду msg, затем через пробел ваше сообщение, либо команду quit для выхода: msg Now you're looking at the very important message from the team of the developers of this miraculous script Now you're looking at the very important message from the team of the developers of this miraculous script Now you're looking at the very important message from the team of the developers of this miraculous script
#=========================================================================================================================================================#
#                                                                                                                                                         #
#  Now you're looking at the very important message from the team of the developers of this miraculous script Now you're looking at the very important m  #
#  essage from the team of the developers of this miraculous script Now you're looking at the very important message from the team of the developers of   #
#  this miraculous script                                                                                                                                 #
#                                                                                                                                                         #
#=========================================================================================================================================================#


# ИТОГ: отлично — 6/6
