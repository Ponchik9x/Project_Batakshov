from src.decorators import log


def test_log() -> None:
    """тест на проверку правильности работы декоратора без добавления в модуль для логов"""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    assert add(4, 5) == 9


def test_log_filename() -> None:
    """тест на проверку правильности работы декоратора добавлением в определенный модуль для логов"""

    @log("log_file")
    def add(x: int, y: int) -> int:
        return x + y

    assert add(4, 5) == 9
