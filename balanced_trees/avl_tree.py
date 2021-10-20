from typing import Optional
from cells.BFBinaryNode import BFBinaryNode
import random as rnd


# Объявляем базовые функции


def height(p: Optional[BFBinaryNode]) -> int:
    """
    Данная фунция нужна, чтобы указывать высоту для нулевых ячеек
    :param p: Передаваемая вершина дерева (или None)
    :return: Высота
    """
    return p.height if p is not None else 0


def balance_factor(p: BFBinaryNode) -> int:
    """
    Данная функция вычисляет разницу высот двух поддеревьев
    :param p: Передаваемая вершина дерева (или None)
    :return: Фактор балансировки (разница высот)
    """
    return height(p.right) - height(p.left)


def fix_height(p: BFBinaryNode) -> None:
    """
    Данная функция восстанавливает высоту вершины
    :param p: Передаваемая вершина дерева (или None)
    """
    lh: int = height(p.left)
    rh: int = height(p.right)
    p.height = (lh if lh >= rh else rh) + 1


def right_rotate(p: BFBinaryNode) -> BFBinaryNode:
    """
    Функция осуществляет правый поворот
    :param p: вершина, для который этот поворот производится
    """
    # Получаем ссылку на левое поддерево
    q: BFBinaryNode = p.left
    p.left = q.right
    q.right = p
    fix_height(p)
    fix_height(q)
    return q


def left_rotate(p: BFBinaryNode) -> BFBinaryNode:
    """
    Функция осуществляет левый поворот
    :param p: Вершина, для которой этот поворот производится
    :return: Ссылка на новую верхнюю ячейку
    """
    q: BFBinaryNode = p.right
    p.right = q.left
    q.left = p
    fix_height(p)
    fix_height(q)
    return q


def balance(p: BFBinaryNode) -> BFBinaryNode:
    """
    :param p: Вершина, для которой происходит балансировка
    :return: Возвращаем ссылку на итоговую вершину
    """
    # Сперва чиним высоту
    fix_height(p)
    # Если правая ветвь ниже и возник дизбаланс
    if balance_factor(p) == 2:
        # Если правое поддерево выше, чем и левое
        if balance_factor(p.right) < 0:
            p.right = right_rotate(p.right)
        return left_rotate(p)
    # Если левая ветвь ниже и возник дизбаланс
    elif balance_factor(p) == -2:
        if balance_factor(p.left) > 0:
            p.left = left_rotate(p.left)
        return right_rotate(p)
    # Если дисбаланса нет
    return p


# Основные функции по работе AVL-дерева


def search(p: Optional[BFBinaryNode], key: int):
    """
    Функция поиска в AVL-дереве
    """
    # Если ничего не найдено
    if p is None:
        return None
    # Если найдено - возвращаем значение
    if p.key == key:
        return p.value
    # Пока не нашли - рекурсивно проходим в нужное поддерево и смотрим там
    return search(p.left, key) if key < p.key else search(p.right, key)


# Вспомогательные функции удаления

def remove_min(p: BFBinaryNode) -> BFBinaryNode:
    """
    Функция удаляет наименьшую по индексу ячейку из дерева (по факту только исключает)
    """
    # Если больше дочерних нет, значит текущая - наименьшая. Возвращаем его родилелю
    # Ссылку на правое поддерево искомой ячейки, исключая её саму, таким образом, из дерева
    if p.left is None:
        return p.right
    # Спускаемся максимально вниз влево (в левое поддерево)
    p.left = remove_min(p.left)
    # На каждом шагу фиксим дерево
    return balance(p)


def find_min(p: BFBinaryNode) -> BFBinaryNode:
    # Спускаемся максимально вниз, пока не найдем самую маленькую по индексу ячейку
    return find_min(p.left) if p.left is not None else p


def delete(p: BFBinaryNode, key: int) -> Optional[BFBinaryNode]:
    """
    Функция удаления в AVL-дереве
    """
    # Если нет искомой ячейки
    if p is None:
        return None
    # Рекурсивно переходим в левое поддерево
    if key < p.key:
        p.left = delete(p.left, key)
    # Рекурсивно переходим в правое поддерево
    elif key > p.key:
        p.right = delete(p.right, key)

    # Если искомая ячейка найдена
    else:
        # Получаем ссылка на её левое и правое поддеревья
        ln = p.left
        rn = p.right
        # Если правое поддерево отсутствует - вместо текущей ячейки возвращаем родителю ссылку
        # на его левое поддерево
        if rn is None:
            return ln
        # Если правое поддерево существует
        # Находим минимальный элемент в нем
        min_item = find_min(rn)
        # Удаляем текущую ячейку
        del p
        min_item.left = ln
        # Удаляем наименьший элемент из правого поддерева и возвращаем ссылку
        # минимальному элементу
        min_item.right = remove_min(rn)
        # Нормируем получившееся дерево и вовращаем его родителю вместо станой ячейки
        return balance(min_item)


def insert(p: Optional[BFBinaryNode], key: int):
    """
    Функция вставки в AVL-дереве
    """
    if p is None:
        return BFBinaryNode(key=key, value=key)
    if key < p.key:
        p.left = insert(p.left, key)
    elif key >= p.key:
        p.right = insert(p.right, key)
    return balance(p)


if __name__ == '__main__':
    random_key = None
    # Тестируем
    tests_count = 100000
    first_key = rnd.randrange(1, 10000)
    first_random_node = BFBinaryNode(key=first_key, value=first_key)
    for i in range(tests_count - 1):
        random_key = rnd.randrange(1, 10000)
        insert(first_random_node, random_key)

    print(search(first_random_node, random_key))
    new_link = delete(first_random_node, random_key)
    print(search(new_link, random_key))
