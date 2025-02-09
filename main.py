def transpose_matrix(matrix):
    """Транспонирует матрицу."""
    return [list(row) for row in zip(*matrix)]

def kwargs_to_dict(**kwargs):
    """Принимает ключевые параметры и возвращает словарь со значением в качестве ключа и именем аргумента в качестве значения."""
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Транспонированная матрица:", transpose_matrix(matrix))

    print("Словарь ключевых аргументов:", kwargs_to_dict(a=10, b=20, c=[1, 2, 3], d={"key": "value"}))
