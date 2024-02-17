# СЛОЖНОСТЬ АЛГОРИТМОВ И ИХ ОПТИМИЗАЦИЯ

## Цель работы
Получить навыки вычисления сложности алгоритмов и их оптимизации различными методами.

## Сортировка выбором
### Описание алгоритма
1. Начинаем с предположения, что первый элемент массива уже отсортирован. Далее итеративно проходим по оставшимся элементам.
2. На каждом шаге текущий элемент вставляется в правильную позицию в отсортированной части массива.
3. Для этого сравниваем текущий элемент с элементами в отсортированной части массива и перемещаем его влево, пока не найдём правильную позицию.

### Сложность алгоритма

- В худшем и среднем случае: **O(n^2)**, так как в худшем случае мы должны выполнить n-1 сравнений для каждого из n элементов.

### Результаты замеров

<img src="./images/plot.png" alt="Image" width="800">

### Базовая реализация
В данной реализации используется вложенный цикл для поиска наименьшего элемента. Если индекс вложенного цикла меньше, 
чем основного, то мы пропускаем итерацию.

### Оптимизированная реализация
В оптимизированной реализации исправляется стартовый индекс вложенного цикла. Кроме того, вместо того чтобы каждый раз 
менять элементы местами при обнаружении минимального элемента, мы просто запоминаем индекс минимального элемента и после завершения внутреннего цикла выполняем обмен только один раз. Это позволяет сократить количество операций присваивания.