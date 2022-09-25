from pathlib import Path

def csv_dict(file_name: str | Path, sep: str = ',') -> dict:
    """Возвращает словарь, сформированный из полученного на вход csv-файла, где элементы 1-й строки файла являются ключами, а элементы последующих строк являются элементами списка значений ключа.
    :param file_name: csv-файл
    :param sep: разделитель полей, по умолчанию ','
    """
    out_dict = {}
    
    if sep not in ',;\t':
        raise ValueError('Введен некорретный разделитель')
    
    with open(file_name, encoding = 'utf-8' ) as file:
    
        def get_line():
            return file.readline().rstrip().split(sep)
    
        cols = get_line()
        cols_len = len(cols)
        curr_line = get_line()
    
        while curr_line != ['']:
            for i in range(cols_len):
                out_dict[cols[i]] = out_dict.setdefault(cols[i], []) + [curr_line[i]]
            curr_line = get_line()
    
    return out_dict

print(csv_dict('test.csv'))
print(csv_dict(Path('test.csv')))

# stdout:
# {'col1': ['1', '2', '3'], 'col2': ['10', '20', '30'], 'col3': ['100', '200', '300']}
# {'col1': ['1', '2', '3'], 'col2': ['10', '20', '30'], 'col3': ['100', '200', '300']}