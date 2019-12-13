quantity, price = map(lambda x: int(x), input().split())
cheque = []
for i in range(quantity):
    cheque_position = input()
    price_per_item, quantity, total_price = cheque_position.split()
    quantity = quantity[1:]
    total_price = total_price[1:]
    cheque.append({'price_per_item': int(price_per_item),
                   'quantity': int(quantity),
                   'total_price': int(total_price),
                   'id': i + 1})
price_in_cheque = (sum(item['total_price'] for item in cheque))
print(price - price_in_cheque)
if price_in_cheque != price:
    for item in cheque:
        print(item['id']) if item['price_per_item'] * item['quantity'] != item['total_price'] else None