from cells.BinaryNode import BinaryNode
from typing import Optional, TypeVar

T = TypeVar('T')


def insert(p: BinaryNode, key: int, value: T) -> BinaryNode:
    # Если мы дошли до конца дерева
    if p is None:
        # Создаем ячейку и рекурсивно прикрепляем к родителю
        return BinaryNode(key=key, value=value)
    if key < p.key:
        p.left = insert(p.left, key, value)
    else:
        p.right = insert(p.right, key, value)


def find_min(p: BinaryNode) -> BinaryNode:
    return find_min(p.left) if p.left is not None else p


def remove_min(p: BinaryNode) -> BinaryNode:
    # В какой-то момент, когда мы доходим до левого конца, мы родителю последней
    # левой ячейки цепляем его правую ветвь, если она есть
    if p.left is None:
        return p.right
    p.left = remove_min(p.left)


def delete(p: BinaryNode, key: int) -> Optional[BinaryNode]:
    # если ячейка не найдена
    if p is None:
        return None
    if key < p.key:
        p.left = delete(p.left, key)
    if key > p.key:
        p.right = delete(p.right, key)
    # Если мы нашли такую ячейку
    else:
        # Получаем ссылки на дочерние ячейки
        lf = p.left
        rt = p.right
        # Если правого ответвления не существует - возвращаем обычную ссылку на левый дочерний
        if rt is None:
            return lf
        # Если правый дочерний существует
        # Получаем минимальный в правом поддереве
        mini_item = find_min(rt)
        # Он будет указывать на то же поддерево, но без минимального
        mini_item.right = remove_min(rt)
        # Слева будет указывать на то же, что и раньше
        mini_item.left = lf
        # Возвращаем ссылку на мнимальный элемент(вместо найденного p)
        return mini_item


def search(p: BinaryNode, key: int) -> Optional[T]:
    if p is None:
        return None
    if p.key == key:
        return p.value
    return search(p.left, key) if key < p.key else search(p.right, key)


if __name__ == '__main__':
    pass
