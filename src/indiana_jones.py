def read_file(file_path):
    """
    Читає дані з файлу, що містить лабіринт.

    Args:
        file_path (str): Шлях до файлу з лабіринтом.

    Returns:
        tuple or int: Кортеж, що містить матрицю лабіринту, словник позицій символів,
        кількість рядків та кількість стовпців у лабіринті. Якщо не вдається прочитати
        дані з файлу, повертає 0.
    """
    file = open(file_path, 'r')
    try:
        columns, lines = map(int, file.readline().split(' '))
    except ValueError:
        file.close()
        return 0

    matrix = []
    dict_of_letters = dict()
    cur_line = 0
    for line in file:
        line = line.replace('\n', '')
        cur_column = 0
        temp_line = []
        for char in line:
            temp_line.append(char)
            if char in dict_of_letters:
                dict_of_letters[char].append((cur_line, cur_column))
            else:
                dict_of_letters[char] = [(cur_line, cur_column)]

            cur_column += 1

        matrix.append(temp_line)
        cur_line += 1
    file.close()
    return matrix, dict_of_letters, lines, columns


def get_result(matrix, dict_of_letters, rows, columns):
    """
    Знаходить кількість можливих шляхів в лабіринті.

    Args:
        matrix (list): Матриця лабіринту.
        dict_of_letters (dict): Словник, що містить позиції символів у лабіринті.
        rows (int): Кількість рядків у лабіринті.
        columns (int): Кількість стовпців у лабіринті.

    Returns:
        int: Кількість можливих шляхів від лівого боку лабіринту до правого.
    """
    memo = {}

    def dfs(x, y):
        if y == columns - 1:
            if x == 0 or x == rows - 1:
                return 1
            else:
                return 0

        if (x, y) in memo:
            return memo[(x, y)]

        paths = 0
        # Переходимо на сусідні клітинки з таким же символом
        for neighbor in dict_of_letters[matrix[x][y]]:
            if neighbor[1] > y:
                paths += dfs(neighbor[0], neighbor[1])
        # Переходимо на праву клітинку
        if y + 1 < columns:
            paths += dfs(x, y + 1)

        memo[(x, y)] = paths
        return paths

    result = 0
    for j in range(rows):
        result += dfs(j, 0)
    return result


def write_result(output_file, result):
    """
    Записує результат у файл.

    Args:
        output_file (str): Шлях до файлу для запису результату.
        result (int): Результат, що записується.
    """
    with open(output_file, 'w') as file:
        file.write(str(result))
    print(result)


def indiana_jones(input_file, output_file):
    """
    Основна функція для запуску програми.

    Args:
        input_file (str): Шлях до вхідного файлу з лабіринтом.
        output_file (str): Шлях до вихідного файлу для запису результату.
    """
    input_data = read_file(input_file)
    if input_data == 0:
        write_result(output_file, 0)
        return

    indiana_jones_matrix, letters_dict, rows, columns = input_data
    result = get_result(indiana_jones_matrix, letters_dict, rows, columns)
    write_result(output_file, result)

