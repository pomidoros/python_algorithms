from stacks_and_deques.stack_algorithms.stacks import StackArray


class AdvancedStacks(StackArray):
    def __init__(self, *args):
        super().__init__(*args)

    def reverse_stack(self):
        other_stack = AdvancedStacks(self.num)
        for i in range(self.next_index):
            item = self.pop()
            other_stack.push(item)
        return other_stack


if __name__ == "__main__":
    new_stack = AdvancedStacks()
    new_stack.push(3)
    new_stack.push(2)
    new_stack.push(1)
    print(new_stack)
    reversed_stack = new_stack.reverse_stack()
    print(reversed_stack)