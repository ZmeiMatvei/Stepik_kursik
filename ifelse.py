# if условие:
# блок кода
# else
# блок кода
#i = int(input())
#if i // 2 != 0:
#    print(i, 'нечётное')
#else:
#    print(i, 'чётное')

#pas1 = str(input())
#pas2 = str(input())
#if pas1 == pas2:
#    print("Пароль принят")
#else:
#    print("Пароль не принят")

#num = int(input())
#if num % 2 == 0:
#    print("Четное")
#else:
#    print("Нечетное")

#num = int(input())
#a = num // 1000
#b = (num // 100) % 10
#c = (num // 10) % 10
#d = num % 10
#if a+d == b-c:
#    print("ДА")
#else:
#    print("НЕТ")

#age = int(input())
#if 0<=age<18:
#    print("Доступ запрещен")
#else:
#    print("Доступ разрешен")

#a = int(input())
#b = int(input())
#c = int(input())
#if b - a == c - b:
#    print("YES")
#else:
#    print("NO")

#numbers_1 = int(input())
#numbers_2 = int(input())
#if numbers_1 < numbers_2:
#    print(numbers_1)
#else:
#    print(numbers_2)

#num_1 = int(input())
#num_2 = int(input())
#num_3 = int(input())
#num_4 = int(input())
#num_m1 = 0
#num_m2 = 0
#if num_1 <= num_2:
#    num_m1 = num_1
#else:
#    num_m1 = num_2
#if num_3 <= num_4:
#    num_m2 = num_3
#else:
#    num_m2 = num_4
#if num_m1 <= num_m2:
#    print(num_m1)
#else:
#    print(num_m2)

#age = int(input())
#if age <= 13:
#    print("детство")
#if 14 <= age <= 24:
#    print("молодость")
#if 25 <= age <= 59:
#    print("зрелость")
#if 60 <= age:
#    print("старость")

#num_1 = int(input())
#num_2 = int(input())
#num_3 = int(input())
#a = 0
#if num_1 > 0:
#    a = num_1
#if num_2 > 0:
#    a = a + num_2
#if num_3 > 0:
#    a = a + num_3
#if a <= 0:
#    a = 0
#print(a)

#x = int(input())
#if -1 < x < 17:
#    print("Принадлежит")
#else:
#    print("Не принадлежит")

#x =int(input())
#if -3 < x < 7:
#    print("Не принадлежит")
#else:
#    print("Принадлежит")

#x= int(input())
#if (-30 < x <= -2) or (7 < x <= 25):
#    print("Принадлежит")
#else:
#    print("Не принадлежит")

#num = int(input())
#if (1000 < num < 9999) and (num % 7 == 0 or num % 17 == 0):
#    print("YES")
#else:
#    print("NO")

#a = int(input())
#b = int(input())
#c = int(input())
#if a + b > c and a + c > b and b + c > a:
#    print("YES")
#else:
#    print("NO")

#year = int(input())
#if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#    print("YES")
#else:
#    print("NO")

#a_stolb = int(input())
#b_stolb = int(input())
#a_str = int(input())
#b_str = int(input())
#if a_stolb == a_str or b_stolb == b_str:
#    print("YES")
#else:
#    print("NO")

#a_stolb = int(input())
#b_stolb = int(input())
#a_str = int(input())
#b_str = int(input())
#if (a_stolb + 1 == a_str or a_stolb - 1 == a_str or a_stolb == a_str) and (b_stolb + 1 == b_str or b_stolb - 1 == b_str or b_stolb == b_str):
#    print("YES")
#else:
#    print("NO")

#zoom, flesh = int(input()), int(input())
#if zoom > flesh:
#    print("NO")
#elif flesh > zoom:
#    print("YES")
#else:
#    print("Don't know")

#a = int(input())
#b = int(input())
#c = int(input())
#if a == b and a == c and b == c:
#    print("Равносторонний")
#elif a == b or a == c or b == c:
#    print("Равнобедренный")
#elif a != b and a != c and b != c:
#    print("Разносторонний")

#num1 = int(input())
#num2 = int(input())
#num3 = int(input())
#if num1 < num2 < num3 or num1 > num2 > num3:
#    print(num2)
#elif num2 < num1 < num3 or num2 > num1 > num3:
#    print(num1)
#elif num1 < num3 < num2 or num1 > num3 > num2:
#    print(num3)

#month = int(input())
#if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#    print("31")
#elif month == 4 or month == 6 or month == 9 or month == 11:
#    print("30")
#elif month == 2:
#    print("28")

#weight = int(input())
#if weight < 60:
#    print("Легкий вес")
#elif 60 <= weight < 64:
#    print("Первый полусредний вес")
#elif 64 <= weight < 69:
#    print("Полусредний вес")

#num1 = int(input())
#num2 = int(input())
#operation = str(input())
#if operation != "+" and operation != "-" and operation != "*" and operation != "/":
#    print("Неверная операция")
#elif operation == '/' and num2 == 0:
#        print("На ноль делить нельзя!")
#elif operation == '+':
#    print(num1 + num2)
#elif operation == '-':
#    print(num1 - num2)
#elif operation == '*':
#    print(num1 * num2)
#elif operation == '/':
#    print(num1 / num2)

#colour1 = str(input())
#colour2 = str(input())
#if (colour1 != "красный" and colour1 != "синий" and colour1 != "желтый") or (colour2 != "красный" and colour2 != "синий" and colour2 != "желтый"):
#   print("ошибка цвета")
#elif colour1 == colour2:
#    print(colour1)
#elif (colour1 == "красный" and colour2 == "синий") or (colour1 == "синий" and colour2 == "красный"):
#    print("фиолетовый")
#elif (colour1 == "красный" and colour2 == "желтый") or (colour1 == "желтый" and colour2 == "красный"):
#    print("оранжевый")
#elif (colour1 == "синий" and colour2 == "желтый") or (colour1 == "желтый" and colour2 == "синий"):
#    print("зеленый")

#num = int(input())
#if 0 > num or num > 36:
#    print("ошибка ввода")
#elif num == 0:
#    print("зеленый")
#elif 1 <= num <= 10 and num % 2 == 0:
#    print("черный")
#elif 1 <= num <= 10 and num % 2 == 1:
#    print("красный")
#elif 11 <= num <= 18 and num % 2 == 0:
#    print("красный")
#elif 11 <= num <= 18 and num % 2 == 1:
#    print("черный")
#elif 19 <= num <= 28 and num % 2 == 0:
#    print("черный")
#elif 19 <= num <= 28 and num % 2 == 1:
#    print("красный")
#elif 29 <= num <= 36 and num % 2 == 0:
#    print("красный")
#elif 29 <= num <= 36 and num % 2 == 1:
#    print("черный")

#a1 = int(input())
#b1 = int(input())
#a2 = int(input())
#b2 = int(input())
#if a1 < b1 and b1 < b2 and b1 < a2 and b1 != a2:
#    print("пустое множество")
#elif a1 < a2 and b2 < b1:
#    print(a2, b2)
#elif a1 < a2 and a2 < b1 < b2:
#    print(a2, b1)
#elif a2 < a1 and a1 < b2 < b1:
#    print(a1, b2)
#elif a2 < a1 and b1 < b2:
#    print(a1, b1)
#elif a1 < b1 and a2 < b2 and b1 == a2:
#    print(b1)
#elif a2 < b2 == a1 and a1 < b1:
#    print (b2)
#elif a1 == a2 and b1 == b2:
#    print(a1, b1)
#elif a1 == a2 and b1 < b2:
#    print (a1, b1)
#elif a2 < a1 and b1 == b2:
#    print (a1, b2)
#elif a1 < a2 and b1 == b2:
#    print (a2, b2)
#elif a1 == a2 and b2 < b1:
#    print (a1, b2)
#else:
#    print("пустое множество")


#print("Сколько рублей хотите обменять?")
#rub = int(input())
#currency = print("Какую валюту хотите получить?")
#if currency == "Доллар" or "доллар":
#    dol = (rub / 82.59)
#    dol = int(dol * 100 + 0.5) / 100
#    print("Доллар =", dol)
#if currency == "Евро" or "евро":
#    eur = (rub / 93.34)
#    eur = int(eur * 100 + 0.5) / 100
#    print("Евро =", eur)
#if currency == "Таиландский бат" or "таиландский бат" or "Бат" or "бат":
#    thb = (rub / 2.48)
#    thb = int(thb * 100 + 0.5) / 100
#    print("Таиландский бат =", thb)
#if currency == "Дирхам" or "дирхам":
#    aed = (rub / 22.49)
#    aed = int(aed * 100 + 0.5) / 100
#    print("Дирхам =", aed)
#if currency == "Турецкая лира" or "турецкая лира":
#    tr = (rub / 2.17)
#    tr = int(tr * 100 + 0.5) / 100
#    print("Турецкая лира =", tr)