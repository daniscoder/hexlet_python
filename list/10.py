# 10. Управляющие инструкции
def get_total_amount(money, currency):
    total = 0
    for elem in money:
        curr, amount = elem.split()
        if curr == currency:
            total += int(amount)
    return total

money1 = [
  'eur 10', 'usd 1', 'usd 10', 'rub 50', 'usd 5',
]
print(get_total_amount(money1, 'usd')) # 16

money2 = [
  'eur 10', 'usd 1', 'eur 5', 'rub 100', 'eur 20', 'eur 100', 'rub 200',
]
print(get_total_amount(money2, 'eur')) # 135

money3 = [
  'eur 10', 'rub 50', 'eur 5', 'rub 10', 'rub 10', 'eur 100', 'rub 200',
]
print(get_total_amount(money3, 'rub')) # 270