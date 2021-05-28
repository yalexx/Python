from decimal import Decimal

principal = Decimal('150')
rate = Decimal('0.08')

for year in range(1, 6):
    amount = principal * (1 + rate) ** year
    print(f'{year:>2}{amount:>10.2f}')




