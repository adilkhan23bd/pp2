
def squares_to_n(n):
    for i in range(n+1):
        yield i*i

print("1.", list(squares_to_n(5)))


n = int(input("2. Введите n: "))
print(','.join(str(i) for i in range(0, n+1, 2)))


def div_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("3.", list(div_3_and_4(50)))


def squares(a, b):
    for i in range(a, b+1):
        yield i*i

print("4. Квадраты от 3 до 7:")
for val in squares(3, 7):
    print(val, end=" ")
print()


def countdown(n):
    for i in range(n, -1, -1):
        yield i

print("5.", list(countdown(5)))