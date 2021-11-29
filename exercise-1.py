#1 x = 5 (str) будет строкой

#2 x будет булевым типом

#3 тип данных dict

#4 тип данных set

#5 тип данных
#6 тип данных None

#7 тип данных int
for i in range(10):
    if i < 5:
        x = 'hello'
    else:
        x = 5
print(x)

#8 тип данных str

#9 тип данных list
a = 5
b = [1, 3, 5]
x = 'x'
a, b, x, = x, a, b
print(x)

#10 тип данных str
def func(x,y = 5):
    return x + y
x = func('Jaguar', 'hunter')
print(x)

