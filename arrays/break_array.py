class RowCell:
    def __init__(self, number=None, next=None, row_sentinel=None):
        self.number = number
        self.next = next
        self.row_sentinel = row_sentinel


class ColumnCell:
    def __init__(self, number=None, value=None, next=None):
        self.number = number
        self.next = next
        self.value = value



class ArrayWithBreak:
    def __init__(self):
        self.main_sentinel = ColumnCell()

    def get_cell(self, row, col):
        prev_row = self.find_row(row)
        if (prev_row.next is None) or (prev_row.next.number != row):
            return None
        row = prev_row.next
        prev_col = self.find_column(row.row_sentinel, col)
        if (prev_col.next is None) or (prev_col.next.number != col):
            return None
        col = prev_col.next
        return col.value

    def set_cell(self, row, col, val):
        prev_row = self.find_row(row)
        if (prev_row.next is None) or (prev_row.next.number != row):
            new_row = RowCell(row, prev_row.next, ColumnCell())
            prev_row.next = new_row
        row = prev_row.next

        prev_col = self.find_column(row.row_sentinel, col)
        if (prev_col.next is None) or (prev_col.next.number != col):
            new_col = ColumnCell(col, val)
            new_col.next = prev_col.next
            prev_col.next = new_col

    def delete_cell(self, row, col):
        prev_row = self.find_row(row)
        if (prev_row.next is None) or (prev_row.next.number != row):
            return
        row = prev_row.next
        prev_col = self.find_column(row.row_sentinel, col)
        if (prev_col.next is None) or (prev_col.next.number != col):
            return
        prev_col.next = prev_col.next.next

    def find_row(self, num):
        sentinel = self.main_sentinel
        while(sentinel.next is not None) and (sentinel.next.number > num):
            sentinel = sentinel.next
        return sentinel


    @staticmethod
    def find_column(row_sent, num):
        sentinel = row_sent
        while(sentinel.next is not None) and (sentinel.next.number > num):
            sentinel = sentinel.next
        return sentinel


if __name__ == "__main__":
    array = ArrayWithBreak()
    array.set_cell(4, 4, 10)
    array.set_cell(1, 5, 1)
    array.set_cell(1, 4, 2)
    array.set_cell(1, 6, 5)
    array.delete_cell(1, 4)