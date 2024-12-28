def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for n in numbers:
            if isinstance(n, (int, float)):
                result += n
            else:
                incorrect_data += 1
                print(f'Некорректный тип данных для подсчёта суммы - {n}')
    except TypeError:
        return 0, 0
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result_summ, count_incorrect = personal_sum(numbers)
        count = len(numbers) - count_incorrect
        # if count == 0:
        #     return 0
        # print(result_summ, count_incorrect, count)
        return result_summ / count
    except ZeroDivisionError:
        return 0
    except TypeError:
        print("В numbers записан некорректный тип данных'")
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
# print(f'Результат 4: {calculate_average([])}')  # пустой список
