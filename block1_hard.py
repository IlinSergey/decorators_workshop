from random import choice


def summarizer(num1: int, num2: int, num3: int, num4: int,
               *args: int, **kwargs: int) -> int:
    total_summ = num1 + num2 + num3 + num4
    if len(args) > 1:
        total_summ += (args[0] + args[1])
    if len(kwargs) >= 1:
        total_summ += choice(list(kwargs.values()))
    return total_summ


#print(summarizer(2, 2, 3, 4, ))
