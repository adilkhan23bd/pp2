def order(item, price, quantity=1, discount=0):
    total = price * quantity * (1 - discount/100)
    print(f"Товар: {item}, Количество: {quantity}, Итого: {total}")

print(order("por", 3))