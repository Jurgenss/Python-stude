import time


def has_duplicates_bruteforce(numbers):
    """Двойной цикл: сравниваем все пары (i, j), i < j.
    Возвращает (найден_дубликат, число_сравнений)."""
    comparisons = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            comparisons += 1
            if numbers[i] == numbers[j]:
                return True, comparisons
    return False, comparisons


def has_duplicates_set(numbers):
    """Через set: храним уже увиденные элементы.
    Возвращает (найден_дубликат, число_операций in/add)."""
    seen = set()
    operations = 0
    for x in numbers:
        operations += 1              # операция x in seen
        if x in seen:
            return True, operations
        operations += 1              # операция seen.add(x)
        seen.add(x)
    return False, operations


# --- замеры без дубликатов (худший случай для обоих) ---
print("=== без дубликатов ===")
for n in [1000, 10000, 100000]:
    data = list(range(n))
    start = time.perf_counter()
    result = has_duplicates_set(data)
    end = time.perf_counter()
    print(f"set   n={n}: {result}, время = {end - start:.6f} сек")

for n in [1000, 10000]:
    data = list(range(n))
    start = time.perf_counter()
    result = has_duplicates_bruteforce(data)
    end = time.perf_counter()
    print(f"brute n={n}: {result}, время = {end - start:.6f} сек")

# --- замеры с дубликатом в конце ---
print("=== дубликат в конце ===")
for n in [1000, 10000, 100000]:
    data = list(range(n - 1)) + [0]
    start = time.perf_counter()
    result = has_duplicates_set(data)
    end = time.perf_counter()
    print(f"set   n={n}: {result}, время = {end - start:.6f} сек")

for n in [1000, 10000]:
    data = list(range(n - 1)) + [0]
    start = time.perf_counter()
    result = has_duplicates_bruteforce(data)
    end = time.perf_counter()
    print(f"brute n={n}: {result}, время = {end - start:.6f} сек")


"""
Задача 2. Поиск дубликатов: два подхода

Оценка сложности:

1) Двойной цикл (brute force):
   - Лучший случай:   O(1)   — первые два элемента равны, 1 сравнение.
   - Худший случай:   O(n²)  — дубликатов нет, проверяем все пары: n*(n-1)/2.
   - Средний случай:  O(n²).
   - Время:           O(n²) — квадратичный класс.
   - Память:          O(1)  — только счётчик comparisons и индексы i, j.
   - Класс сложности: квадратичный.

2) Через set:
   - Лучший случай:   O(1)   — первые два элемента равны.
   - Худший случай:   O(n²)  — теоретически, при полных коллизиях хешей
                              (для целых чисел в Python практически не встречается).
   - Средний случай:  O(n).
   - Время:           O(n) в среднем — линейный класс.
   - Память:          O(n)  — множество seen хранит до n элементов.
   - Класс сложности: линейный (в среднем).

Почему set даёт O(n) в среднем:
   set в Python — хеш-таблица. Операции x in seen и seen.add(x) вычисляют
   хеш значения x и обращаются к нужному «ведру» напрямую, без перебора
   всех элементов. В среднем это O(1) на операцию, значит цикл по n
   элементам даёт O(n).

Компромисс «время против памяти»:
   - Двойной цикл: O(1) памяти, но O(n²) времени.
   - set:          O(n) памяти, но O(n) времени.
   Для больших n выбор очевиден в пользу set.

Примечание по замерам:
   Для brute на n = 10^5 замер не проводился: по формуле n*(n-1)/2 это
   ~5*10^9 сравнений, что заняло бы порядка 6 минут. Это само по себе
   показывает непригодность квадратичного алгоритма для больших данных.

Примечание по сценарию «дубликат в конце»:
    Данные: list(range(n-1)) + [0]. Дубликат — значение 0, стоит на позиции 0
    и на позиции n-1. Двойной цикл при i=0 сравнивает arr[0] со всеми
    элементами и находит совпадение на j=n-1, выполняя n-1 сравнений.
    Поэтому для brute это не худший, а почти лучший случай — O(n).
    Рост времени ×11.9 при n: 10^3 -> 10^4 подтверждает линейную зависимость.
    Это показывает, что время brute сильно зависит от расположения дубликата,
    а время set — почти нет (set стабильно линеен в обоих сценариях).   
"""