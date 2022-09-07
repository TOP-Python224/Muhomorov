from random import randrange as rr

lst1 = [rr(0, 51, 5) for i in range(10)]
lst2 = [rr(0, 51, 5) for i in range(10)]
print(f"{lst1 = }\n{lst2 = }\n")

for number in set(lst1) & set(lst2):
    for lst in (lst1, lst2):
        for _ in range(lst.count(number)):
            lst.remove(number)
print(f"{lst1 = }\n{lst2 = }")

#stdout:
# lst1 = [25, 35, 0, 0, 20, 10, 50, 40, 30, 15]
# lst2 = [15, 30, 45, 0, 5, 10, 15, 5, 25, 40]

# lst1 = [35, 20, 50]
# lst2 = [45, 5, 5]