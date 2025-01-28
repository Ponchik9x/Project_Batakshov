from datetime import datetime

from examples import (account_card_number, account_card_number_invalid, account_number_score,
                      account_number_score_invalid, my_dict, transactions)
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

print(filter_by_state(my_dict))

print(sort_by_date(my_dict))

print(get_mask_card_number(account_card_number))

print(get_mask_account(account_number_score))

print(mask_account_card(account_number_score_invalid))

print(mask_account_card(account_card_number_invalid))

print(get_date(datetime.now()))

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

for card_number in card_number_generator(1, 5):
    print(card_number)
