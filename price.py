def format_price(price):
    price=int(price)
    a=f'Цена: {price} руб.'
    return a
result=format_price(100.90)
print(result)