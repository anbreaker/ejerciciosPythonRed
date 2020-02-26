def binary_search(numbers, number_to_find, low_index, high_index):
    if low_index > high_index:
        return False

    mid_index = int((low_index + high_index) / 2)

    if numbers[mid_index] == number_to_find:
        return True
    elif numbers[mid_index] > number_to_find:
        return binary_search(numbers, number_to_find, low_index, mid_index-1)
    else:
        return binary_search(numbers, number_to_find, mid_index+1, high_index)


if __name__ == '__main__':
    numbers = [1, 43, 3, 4, 12, 6, 9, 10, 31, 11, 25, 5, 27, 28, 34, 48, 53, 7, 36, 49, 2]
    print(numbers)
    numbers.sort()
    print(numbers)

    number_to_find = int(input('Ingresa un número: '))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número NO está en la lista.')
