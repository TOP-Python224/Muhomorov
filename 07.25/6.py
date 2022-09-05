inp = input('Введите список файлов, разделенных символом пробела: ')
file_cnt = {}

for file in inp.split(' '):
    if file in file_cnt:
        file_cnt[file] += 1
        file_name, file_ext = file.split('.')
        print(f'{file_name}_{file_cnt[file]}.{file_ext}', end=' ')
       
    else:
        file_cnt[file] = 1
        print(file, end=' ')


# Введите список файлов, разделенных символом пробела: 1.py 1.py aux.h main.cpp functions.h main.cpp 2.py main.cpp
# 1.py 1_2.py aux.h main.cpp functions.h main_2.cpp 2.py main_3.cpp

# Введите список файлов, разделенных символом пробела: script.sh 1.txt 2.txt python.py doc.doc script.sh 1.txt start.exe script.sh
# script.sh 1.txt 2.txt python.py doc.doc script_2.sh 1_2.txt start.exe script_3.sh