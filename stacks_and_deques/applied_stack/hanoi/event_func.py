from math import ceil


def block_event(block, event):
    if block.index != block.parent_stack.next_index - 1:
        block = block.parent_stack.array[block.parent_stack.next_index - 1]
    # при нажатии на блок меняем его статус
    block.block_status += 1
    block.frame['highlightthickness'] = 5
    block.frame['highlightbackground'] = 'pink'
    # получаем список всех статусов блоков
    list_of_presses = [obj.block_status for obj in block.all_statuses]
    # если количество помеченных блоков больше 1 - очищаем все статусы
    if sum(list_of_presses) > 1:
        for block in block.all_statuses:
            block.block_status = 0
            block.frame['highlightthickness'] = 1
            block.frame['highlightbackground'] = 'black'


def layer_event(blocks, stacks, width, event):
    # получаем список всех статусов
    list_of_presses = [block.block_status for block in blocks]
    # если нажатий на блок не было
    if sum(list_of_presses) == 0:
        # генерируем исключение
        print("Fuck you")
    # если нажание было:
    else:
        parts = [ceil(width / 3 * i) for i in range(0, 3)]
        bias = event.widget.winfo_geometry().split('+')[1]
        # получаем индекс нужного стека
        index_of_stack = parts.index(int(bias))
        # получаем индекс нужного блока
        index_of_block = list_of_presses.index(1)

        # получаем выбранный блок
        selected_block = blocks[index_of_block]

        # в выбранный стек перемещаем наш блок
        stacks[index_of_stack].push(selected_block.parent_stack.pop())

        # зануляем все статусы
        for block in blocks[0].all_statuses:
            block.block_status = 0