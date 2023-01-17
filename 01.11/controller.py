"""Контроллер MVC."""

from model import Email
from view import CLIView


class Application:
    """Обеспечивает взаимодействие модели и представления."""

    @staticmethod
    def save_email(email: Email) -> None:
        """Сохраняет принятый валидный e-mail в файл."""
        email.save()

    @classmethod
    def get_email(cls) -> None:
        """Запрашивает e-mail в условно-бесконечном цикле, в случае валидности вызывает метод для сохранения в файл."""
        while True:
            email = CLIView.enter_email()
            if email:
                try:
                    email_to_save = Email(email)
                except ValueError:
                    CLIView.print_msg(False)
                else:
                    cls.save_email(email_to_save)
                    CLIView.print_msg(True)
            else:
                break
