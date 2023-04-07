# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город
# проживания, email, телефон. Функция должна принимать параметры как
# именованные аргументы. Осуществить вывод данных о пользователе одной
# строкой.

def information(name,surname, birthday, city, email, phone):
    return f'name: {name}, surname: {surname}, birthday: {birthday},' \
           f' city: {city}, email: {email}, phone: {phone}'
print(information(name='Tom', surname='Ford', birthday='27.08.1961',
                  city='New York', email='TomFord@yndex.com',
                  phone='+1 322 223 322 322'))






