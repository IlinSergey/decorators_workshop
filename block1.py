def camel_string(word: str, multiplier: int) -> str:
    '''Возвращает строку, в которой каждый второй вхождение `string` в верхнем регистре, а остальные в нижнем.'''
    multiplied_word = [word.lower() if i % 2 != 0 else word.upper() for i in range(1, multiplier + 1)]
    return ''.join(multiplied_word)


test = camel_string

#print(camel_string) --> <function camel_string at 0x7fdc78d63d90>

#print(test('hello', 5)) --> helloHELLOhelloHELLOhello
