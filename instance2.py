# Переменная для хранения произведения
product = 1

# Флаг для проверки, были ли ненулевые числа
found_non_zero = False

# Цикл для ввода 10 чисел
for _ in range(10):
    num = int(input())
    if num != 0:
        product *= num
        found_non_zero = True

# Проверка, были ли ненулевые числа
if found_non_zero:
    print(product)
else:
    print(0)

print("End of program")