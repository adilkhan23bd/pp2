def sum_all(*args):
    print(f"Получено аргументов: {len(args)}")
    print(f"Аргументы: {args}")
    return sum(args)
print(sum_all(1, 2, 3, 4))