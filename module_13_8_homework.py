ticket_count = int(input('Введите количество билетов: '))
payment_amount = 0
for i in range(1, ticket_count + 1):
    age = int(input('Введите количество лет: '))
    if age < 18:
        payment_amount += 0
    elif 18 <= age < 25:
        payment_amount += 990
    else:
        payment_amount += 1390
if ticket_count > 3:
    payment_amount = payment_amount - (payment_amount * 0.1)

print(f'Сумма к оплате: {payment_amount} руб.')






