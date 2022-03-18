from random import randint


class Solution:
    '''

    TASK DESCRIPTION

    Преобразуйте список целых чисел: оставьте только кратные пяти.

    Примечание, ввод производится в синтаксисе списка

    EXAMPLES:

    Sample Input:
    [4, 5, 7, 237895, 32, 432, 45, 0]

    Sample Output:
    5 237895 45 0

    '''

    def eval_list_filter(self, line: str):
        # или from ast import literal_eval
        number_list = eval(line)
        return tuple(filter(lambda number: not number % 5, number_list))

    def core_list_filter(self, line: str) -> tuple:
        number_list = list(map(int, line.strip('[]').split(', ')))
        return tuple(filter(lambda number: not number % 5, number_list))


if __name__ == '__main__':
    line = input()
    result = Solution()
    print(*result.core_list_filter(line))

    # заменить на юнит тесты
    for i in range(100):
        temporary_list = [randint(-500, 500) for _ in range(randint(5, 30))]
        temporary_line = str(temporary_list)

        assert result.core_list_filter(temporary_line) == result.eval_list_filter(temporary_line), 'Test failed'
