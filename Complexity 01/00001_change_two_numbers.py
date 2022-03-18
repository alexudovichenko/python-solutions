class Solution:
    '''

    TASK DESCRIPTION

    Поменяйте местами два числа без использования третьей переменной.
    Попробуйте решить задачу без хитростей Python, как, например, этой:
    a, b = b, a

    Примечание, могут быть как целые, так и вещественные числа.
    Гарантируется, что в строке их 2 и они разделены пробелом.

    EXAMPLES:

    Sample Input:
    8 11
    Sample Output:
    11 8

    '''

    def change_two_numbers(self, line: str) -> tuple:
        temporary_list = line.split()[::-1]
        for i in range(len(temporary_list)):
            try:
                temporary_list[i] = int(temporary_list[i])
            except:
                temporary_list[i] = float(temporary_list[i])
        return tuple(temporary_list)


if __name__ == '__main__':
    line = input()
    result = Solution()
    print(*result.change_two_numbers(line))

    # заменить на юнит тесты
    assert result.change_two_numbers('8.1 10') == (10, 8.1), 'Test failed'
    assert result.change_two_numbers('123 321') == (321, 123), 'Test failed'
    assert result.change_two_numbers('8.123 0.00005') == (0.00005, 8.123), 'Test failed'
    assert result.change_two_numbers('-200.0 -0.1') == (-0.1, -200.0), 'Test failed'
