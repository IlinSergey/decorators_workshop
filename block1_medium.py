def summarizer(num1: int, num2: int, num3: int, num4: int, *args: int) -> int:
    '''Функция, которая принимает 4 обязательных аргумента и произвольное количество
      дополнительных аргументов. Возвращает их сумму'''
    total_summ = num1 + num2 + num3 + num4 + sum(args)
    return total_summ


# print(summarizer(1)) --> TypeError: summarizer() missing 3 required positional arguments: 'num2', 'num3', and 'num4'
# print(summarizer(num1=2, num2=3, num3=3, num4=5))  --> 13

# nums = (2, 3, 3, 5)
# print(summarizer(*nums))  --> 13


# nums = {'num1': 2, 'num2': 2, 'num3': 3, 'num4': 4}
# print(summarizer(**nums))
# При использовании * распаковываются только ключи, т.к. они str -> TypeError
# При использовании ** ключ попадает в 'имя' аргумента, а значение  в 'значение' аргумента, функция отрабатыват.
# Но нужно учитывать чтобы ключи совпадали с 'именами' аргументов
