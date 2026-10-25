arr = [1, 3, 5, 7, 9, 11, 13, 15]

def binary_search_iterative(arr,x):
    left = 0
    right = len(arr) -1 
    iterations = 0
    
    while left <= right :
        mid = (left +right) //2
        iterations +=1
        if arr[mid] == x:            
            return mid, iterations
        elif arr[mid] < x:
           left = mid +1
        else:
            right = mid - 1
    return -1, iterations        





def binary_search_recursive(arr, x, left, right, depth):
    if left > right:
        return -1, depth
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid, depth
    elif arr[mid] < x:
        return binary_search_recursive(arr, x, mid+1, right, depth+1)
    else:
        return binary_search_recursive(arr, x, left, mid -1, depth+1)      






print(binary_search_iterative(arr, 1))    # первый элемент
print(binary_search_recursive(arr, 1, 0, len(arr) - 1, 1))

print(binary_search_iterative(arr, 15))   # последний элемент
print(binary_search_recursive(arr, 15, 0, len(arr) - 1, 1))

print(binary_search_iterative(arr, 4))    # отсутствует
print(binary_search_recursive(arr, 4, 0, len(arr) - 1, 1))

print(binary_search_iterative([], 5))     # пустой массив
print(binary_search_recursive([], 5, 0, -1, 1))

print(binary_search_iterative(arr, 7))
print(binary_search_recursive(arr, 7, 0, len(arr) -1, 1))






"""
Задача 3. Бинарный поиск: итеративно и рекурсивно

Оценка сложности:

1) Итеративная версия:
   - Лучший случай:    O(1)     — x совпал с первым mid.
   - Худший случай:    O(log n) — область поиска уменьшается вдвое на каждой итерации.
   - Время:            O(log n) — логарифмический класс.
   - Память:           O(1)     — только left, right, mid, iterations.
   - Класс сложности:  логарифмический.

2) Рекурсивная версия:
   - Лучший случай:    O(1)     — x совпал с первым mid (один вызов).
   - Худший случай:    O(log n) — глубина рекурсии ~ log₂ n.
   - Время:            O(log n).
   - Память:           O(log n) — каждый вызов занимает кадр в стеке,
                                  глубина стека ~ log₂ n.
   - Класс сложности:  логарифмический.

Почему O(log n):
   На каждом шаге (итерации или рекурсивном вызове) область поиска
   [left, right] сокращается примерно вдвое. После k шагов остаётся
   n / 2^k элементов. Поиск заканчивается, когда n / 2^k ≈ 1, откуда
   k ≈ log₂ n. Значит, число шагов растёт логарифмически с n.

Сравнение версий:
   - Время одинаковое — O(log n).
   - Итеративная версия экономичнее по памяти: O(1) против O(log n)
     у рекурсивной (стек вызовов).
   - В Python глубина рекурсии ограничена (~1000 по умолчанию),
     поэтому для очень больших n рекурсивная версия может упасть
     с RecursionError — итеративная лишена этого недостатка.

Требование к данным:
   Массив должен быть отсортирован по возрастанию. Иначе свойство
   «если arr[mid] < x, то x правее» не выполняется, и алгоритм
   может вернуть неверный результат.

Расхождение счётчиков:
   Для ненайденных элементов depth (рекурсивная) на 1 больше
   iterations (итеративная), потому что последний рекурсивный вызов
   сразу попадает в базовый случай left > right и не делает сравнения.
   Для найденных элементов значения совпадают.
"""