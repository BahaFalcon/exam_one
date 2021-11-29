x = float(input("Введите сумму вклада: "))
y = int(input("Введите желаемую сумму: "))
z = float(input("Введите годовой процент: "))

for i in range(y):
    if i == ((0.12 / 12) * x) + x:
        months = ((y - i) / 12)


print(months)



