"""A class to represent a monkey."""
import operator


class Monkey:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.worry_level = 0
        self.inspection_count = 0
        self.operation = ""
        self.operation_amount = 0
        self.test_amount = 0
        self.throw_true = 0
        self.throw_false = 0

    def __str__(self):
        return f"{self.name}: Carrying: {self.items}, Worry level: {self.worry_level}, Operation: {self.operation}, " \
               f"Operation amount: {self.operation_amount}, Test amount: {self.test_amount}"

    def add_items(self, items):
        for item in items:
            self.items.append(item)

    def calculate_worry(self, item):
        rel_ops = {
            '+': operator.add,
            '*': operator.mul
        }
        if self.operation_amount == "old":
            operation = int((rel_ops[self.operation](item, item)) / 3)
        else:
            operation = int((rel_ops[self.operation](item, self.operation_amount)) / 3)
        return operation

    def test_item(self, item):
        if item % self.test_amount == 0:
            throw_to = self.throw_true
        else:
            throw_to = self.throw_false
        return throw_to


if __name__ == "__main__":
    pass
