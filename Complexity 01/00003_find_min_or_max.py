class Solution:
    '''

    TASK DESCRIPTION

    Среди приведённых ниже трёх натуральных чисел, записанных в различных системах счисления
    (двоичная, восьмеричная, шестнадцатеричная), найдите максимальное или минимальное
    (в зависимости от того, что написано в четвертой строке: max или min) и выведите его в ответе в
    десятичной системе счисления. Введенные числа не превышают 51110.
    В ответе выведите только число, основание системы счисления указывать не нужно.

    Примечание:

    Ввод гарантируется, дополнительных проверок не требуется, в том числе на соответствие функций

    EXAMPLES:

    Sample Input 1:
    11100111
    77
    B8
    min

    Sample Output 1:
    63

    Sample Input 2:
    1100011
    311
    CD
    max

    Sample Output 2:
    205

    '''

    def find_min_or_max(self, bin_number: str, oct_number: str, hex_number: str, function: str) -> int:
        function_types = {'min': min, 'max': max}
        temporary_list = []
        for number, radix in zip((bin_number, oct_number, hex_number), (2, 8, 16)):
            temporary_list.append(int(number, radix))
        return function_types[function](temporary_list)


if __name__ == '__main__':
    bin_number, oct_number, hex_number, function = (input() for _ in range(4))
    result = Solution()
    print(result.find_min_or_max(bin_number, oct_number, hex_number, function))

    # заменить на юнит тесты
    assert result.find_min_or_max('11100111', '77', 'B8', 'min') == 63, 'Test failed'
    assert result.find_min_or_max('1100011', '311', 'CD', 'max') == 205, 'Test failed'
