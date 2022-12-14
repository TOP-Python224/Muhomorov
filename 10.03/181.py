coins = (25, 10, 5, 1)


def check_coins(money, amount, coins) -> bool:
    """Проверяет возможно ли составить введенную сумму из введенного количества монет номиналом 25, 10, 5, 1 центов в любом """
    quotient, remainder = divmod(money, coins[0])
    if remainder == 0:
        if quotient == amount: 
            return True
        else:
            return False
    else:
        if quotient == amount:
            return False
        else:
            if quotient > amount:
                return False
            else:
                money -= quotient * coins[0]
                amount -= quotient
                coins = coins[1:]
                return check_coins(money, amount, coins)


money = int(input('Введите сумму в центах: '))
amount = int(input('Введите количество монет: '))
print(check_coins(money, amount, coins))


# stdout:
# Введите сумму в центах: 3
# Введите количество монет: 10
# False
# Введите сумму в центах: 152
# Введите количество монет: 8
# True
# Введите сумму в центах: 63
# Введите количество монет: 6
# True


# ИТОГ: отлично — 6/6
