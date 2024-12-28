
def add_everything_up(a, b):
    try:
        return round(a  +  b, 3)

    except TypeError:
        # print("Ошибка типов: число и строку складывать нельзя")
        return str(a) + str(b)



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
