from datetime import datetime, timedelta


class PeriodOfDay:
    """
    Определяет текущий период суток пользователя в соответствии с его часовым поясом.
    """
    def __init__(self, offset: int = 0):
        if isinstance(offset, int):
            self.offset = offset
        else:
            raise TypeError('Должно быть целое число!')

    def curr_user_time(self) -> str:
        """Возвращает текущий период суток пользователя в соответствии с переданным смещением."""
        self.userhour = (datetime.now() + timedelta(hours=self.offset)).hour
        return ['night', 'morning', 'day', 'evening'][self.userhour//6]

    def __str__(self):
        return f"{self.curr_user_time()}"


print(datetime.now())
p1 = PeriodOfDay()
p2 = PeriodOfDay(-6)
p3 = PeriodOfDay(6)
p4 = PeriodOfDay(-12)
print(p1)
print(p2)
print(p3)
print(p4)


# stdout:
# 2022-11-10 21:47:15.188748
# evening
# day
# night
# morning
