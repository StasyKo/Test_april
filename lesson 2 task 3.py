# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

number = int(input("Ведите целое число от 1 до 12: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'зиме', 2: 'зиме', 3: 'весне', 4: 'весне',
                  5: 'весне', 6: 'лету', 7: 'лету', 8: 'лету', 9: 'осени',
                  10: 'осени', 11: 'осени', 12: 'зиме'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Месяц из списка относится к {month_list[i]},")
            break
    print(f"Месяц из словаря относится к {month_dict[number]}.")
else:
    print("Вы ввели неверное число, попробуйте снова!")

