import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """
    Функция принимает номер карты или счета и меняет необходимые цифры по примеру:
    ДЛЯ КАРТ показывает первые 6 цифр и последние 4 цифры в блоке по 4 цифры,
    а остальные цифры заменяет на символ'*'
    ДЛЯ СЧЕТА заменяет все цифры символом '*' и возвращает последние 4 цифры
    """
    logger.info(f"Получение значения карты: {card_num}")

    if len(card_num) == 16:
        encrypted_value = f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"
        logger.info(f"Вывод зашифрованного значения карты: {encrypted_value}")
    elif len(card_num) == 20:
        encrypted_value = f"**{card_num[-4:]}"
        logger.info(f"Вывод зашифрованного значения счета: {encrypted_value}")
    else:
        logger.error(f"Значения карты {card_num} не соответствует параметрам 16/20 цифр")
        raise ValueError("неверный номер карты/счета")

    return encrypted_value


