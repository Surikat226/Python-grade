### Вызов функции с несовпадающим кол-вом аргументов
def show_zarplata(salary = 35000, nds = 10, ndfl = 20, pzdc = 17):
    final_salary = salary - nds + ndfl * pzdc
    print(f"Конечная зарплата - {final_salary} миска рис")
show_zarplata(50000, pzdc=10)

print("-------------------")

### Функция с именованными аргументами
def show_pet_names(cat, dog, parrot, squirrel):
    print(f"Имя кота - {cat}")
    print(f"Имя собаки - {dog}")
    print(f"Имя попуги - {parrot}")
    print(f"Имя белки - {squirrel}")
# В отличие от позиционных аргументов, именованные аргументы при вызове можно указывать в произвольном порядке:
show_pet_names(dog="Собакен", squirrel="Белка ежжи", cat="Маруся", parrot="Одноглазый Джо")

print("-------------------")

### Лямбда-функция
# С помощью лямбда-функции можно писать простые функции и в каких-то моментах сократить свой код. К примеру:
# Есть обычная функция-калькулятор:
def calc_sum(a, b):
    c = a+b
    return c
print(calc_sum(10, 20))

# а есть лямбда-функция (загоним её в переменную):
calc_sum_lambda = lambda a, b: a+b  # лямбда-функция по дефолту возвращает результат её выполнения, и return дописывать не нужно
print(calc_sum_lambda(10, 20))
# три строки против одной))

# лямда-функция может быть элементом списка:
list_228 = [666, 201.1, lambda: print("Это лямбда"), "строчка"]
list_228[2]()

print("-------------------")

### Функции с переменным числом аргументов
# Функция с произвольным кол-вом аргументов:
def show_employee_surnames(*surnames):
    for surname in surnames:
        print(surname)
show_employee_surnames("Костылёв", "Простынёв", "Обосрамс", "Младов", "Овчинников")

print("-------------------")

# Функция с произвольным числом именованных аргументов:
def show_employee_info(**info):
    for name, age in info.items():
        print(f"Имя сотрудника: {name}, возраст: {age}")
show_employee_info(Артём=24, Газгулл=4000, Петька=13)

# *args — list неименованных аргументов, **kwargs — dict именованных аргументов