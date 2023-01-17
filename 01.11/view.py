"""Представление MVC."""


class CLIView:
    """Описывает интерфейс с пользователем."""

    @staticmethod
    def enter_email() -> str:
        """Запрашивает ввод e-mail из stdin."""
        input_email = input('Введите e-mail: ')
        return input_email

    @staticmethod
    def print_msg(result: bool) -> None:
        """Выводит сообщение об успехе/неуспехе операции в stdout."""
        messages = ['Введен некорректный e-mail', 'Введенный e-mail успешно сохранен в файл']
        print(messages[result])
