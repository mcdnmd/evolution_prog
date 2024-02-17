import os
import time
import random
import matplotlib.pyplot as plt

from pathlib import Path

DIR = Path().parent
IMAGE_DIR = DIR / 'images'
os.makedirs(IMAGE_DIR, exist_ok=True)


def selection_sort(array: list) -> None:
    """
    Сортирует список array методом сортировки выбором.

    Время: O(n^2)
    Память: O(1)
    :param array: Список, который требуется отсортировать.
    """
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(n):
            if j <= i:
                continue
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


def optimized_selection_sort(array: list) -> None:
    """
    Оптимизированная версия сортировки выбором.

    Время: O(n^2)
    Память: O(1)
    :param array: Список, который требуется отсортировать.
    """
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]


def generate_random_array(size: int) -> list[int]:
    """
    Генерирует список случайных целых чисел заданного размера.

    :param size: Размер списка (количество элементов).
    :return: Список случайных целых чисел.
    """
    return [random.randint(0, 1000) for _ in range(size)]


def test_sorting_algorithm(algorithm: callable, array: list) -> float:
    """
    Тестирует алгоритм сортировки на заданном массиве и возвращает время его выполнения.

    :param algorithm: Функция, реализующая алгоритм сортировки.
    :param array: Массив, который нужно отсортировать.
    :return: Время выполнения алгоритма сортировки.
    """
    start_time = time.time()
    algorithm(array)
    end_time = time.time()
    return end_time - start_time


def show_plot(sizes: list[int], base_sorting_times: list[float], optimized_sorting_times: list[float]) -> None:
    plt.plot(sizes, base_sorting_times, label='Базовая реализация')
    plt.plot(sizes, optimized_sorting_times, label='Оптимизированная реализация')

    plt.xlabel('Размер массива')
    plt.ylabel('Время выполнения (с.)')
    plt.title('Сравнение времени выполнения алгоритмов сортировки')
    plt.legend()
    plt.grid(True)
    plt.savefig(IMAGE_DIR / "plot.png")


if __name__ == '__main__':
    sizes = [100, 1_000, 2_000, 5_000, 10_000, 20_000]
    base_sorting_times = []
    optimized_sorting_times = []

    for size in sizes:
        arr = generate_random_array(size)
        print(f"Размер массива: {size}")

        # Тестирование базовой реализации сортировки выбором
        base_sorting_time = test_sorting_algorithm(selection_sort, arr.copy())
        base_sorting_times.append(base_sorting_time)
        print(f"Базовая реализация: {base_sorting_time} с.")

        # Тестирование оптимизированной реализации сортировки выбором
        optimized_sorting_time = test_sorting_algorithm(optimized_selection_sort, arr.copy())
        optimized_sorting_times.append(optimized_sorting_time)
        print(f"Оптимизированная реализация: {optimized_sorting_time} с.")

        print("-"*30)

    show_plot(sizes, base_sorting_times, optimized_sorting_times)