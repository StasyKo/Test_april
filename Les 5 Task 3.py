# 3. Создать текстовый файл (не программно). Построчно записать фамилии
# сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

summa = 0
count = 0
persons = []
with open("file2.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if float(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += float(tokens[1])
        count += 1
result = summa / count
print(f"Средняя зарплата: {result}")