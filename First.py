# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

# Функция проверяет число на необходимые условия кратности
def checked(x):
    return (x % 3 == 0) | (x % 5 == 0)


sum_of_checked = 0
i = 1
int(sum_of_checked)
while i < 1000:
    if checked(i):
        sum_of_checked = sum_of_checked + i
    i = i + 1
print(sum_of_checked)  # Ожидаемое число 233168
