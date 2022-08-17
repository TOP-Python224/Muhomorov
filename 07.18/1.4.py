inp = input('Введите номер билета: ')

part1 = [int(inp[:1]), int(inp[1:2]), int(inp[2:3])]
part2 = [int(inp[3:4]), int(inp[4:5]), int(inp[5:])]


if sum(part1) == sum(part2):
    print('ДА')
else:
    print('НЕТ')


    