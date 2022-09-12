from itertools import permutations
letters_set = {'a', 'r', 't', 'i'}
letters = ''

for c in letters_set:
    letters += c

def all_perms(elements):
    # Алгоритм не мой (
    """Генерирует перестановки для переданного множества элементов."""
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]                
              
generator_perm = all_perms(letters)
print(*list(sorted(generator_perm)))

itertool_perm = sorted(permutations(letters_set))
print(*[''.join(permut) for permut in itertool_perm])

#stdout:
# airt aitr arit arti atir atri iart iatr irat irta itar itra rait rati riat rita rtai rtia tair tari tiar tira trai tria
# airt aitr arit arti atir atri iart iatr irat irta itar itra rait rati riat rita rtai rtia tair tari tiar tira trai tria