user_name = 'Иван'
user_surname = 'Петров'
user_age = 32
name = input ('Введите имя: ')
if name.istitle() and name.isalpha() and name == user_name:
    print ('Имя указано верно')
else:
    print ('Имя указано не верно')
surname = input ('Введите фамилию: ')
if surname.istitle() and surname.isalpha() and surname == user_surname:
    print ('Фамилия указана верно')
else:
    print('Фамилия указана не верно')
age = input ('Введите возраст: ')
if age.isdigit() and age == user_age:
    print('Возраст указан верно')
else:
    print ('Возраст указан не верно')



