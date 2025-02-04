import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_num: str) -> str:
    """Функция показывает первые 6 цифр и последние 4 цифры в блоке по 4 цифры,
    а остальные цифры заменяет на символ'*'"""
    logger.info(f"Получение значения карты: {card_num}")

    if len(card_num) > 16 or len(card_num) < 16:
        logger.error(f"Значения карты {card_num} меньше 16 цифр")
        raise ValueError("неверный номер карты")

    encrypted_card = f"{card_num[0:4]} {card_num[4:6]}** **** {card_num[-4:]}"
    logger.info(f"Вывод зашифрованного значения карты: {encrypted_card}")

    return encrypted_card


def get_mask_account(card_num: str) -> str:
    """ "Функция заменяет все цифры символом '*' и возвращает последние 4 цифры"""
    logger.info(f"Получение значения счета: {card_num}")

    if len(card_num) > 20 or len(card_num) < 20:
        logger.error(f"Значения карты {card_num} меньше 20 цифр")
        raise ValueError("неверный номер карты")

    encrypted_account = f"**{card_num[-4:]}"
    logger.info(f"Вывод зашифрованного значения карты: {encrypted_account}")

    return encrypted_account
