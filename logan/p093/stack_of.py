from itertools import *

class NotUnique(Exception): pass
class CannotEvaluate(Exception): pass

class Stack(object):
    """Represents an arithmatic stack."""
    def __init__(self, numbers=[1, 2, 3, 4]):
        self.stack = []
        self.numbers = [float(x) for x in numbers]

    def copy(self):
        new_stack = Stack(self.numbers)
        new_stack.stack = [x for x in self.stack]
        return new_stack

    def push_code(self, code):
        if code >= 8:
            raise CannotEvaluate("The code {0} is not recognized.".format(code))
        vals = [x for x in self.numbers] + [op for op in ['+', '-', '*', '/']]
        if code < 4:
            if self.numbers[code] in self.stack:
                raise NotUnique("{0} is in {1}".format(self.numbers[code],
                                                       self.stack))
            else:
                self.stack.append(self.numbers[code])
        else:
            self.stack.append(vals[code])

    def push(self, val):
        """Places an element on the stack.

        .. todo:: Check for non-evaluatable arguments.
        """
        try:
            self.stack.append(float(val))
        except:
            self.stack.append(val)

    def evaluate(self):
        """
        .. todo::
            This is a todo.

        """
        def red_func(a, b, op):
            if (op not in ['+', '-', '/', '*'] or
                not isinstance(a, float) or
                not isinstance(b, float)):
                raise CannotEvaluate(
                        "Cannot evaluate. a: {a} b: {b} op: {op}".format(
                                a=a, b=b, op=op))
            else:
                if op == '+':
                    return a + b
                elif op == '-':
                    return a - b
                elif op == '*':
                    return a * b
                else:
                    return a / b

        stack = [x for x in self.stack]
        while len(stack) >= 3:
            for i, val in enumerate(stack):
                if val in ['+', '-', '*', '/']:
                    a, b, op = stack[i - 2:i + 1]
                    stack[i - 2:i + 1] = [red_func(a, b, op)]
                    break
        return stack[0]

    def __str__(self):
        return str(self.stack)


def build(stack, collect):
    for numbers in permutations(stack.numbers):
        for ops in product(['+', '-', '*', '/'], repeat=3):
            new_stack = Stack(numbers)
            new_stack.push(numbers[0])
            new_stack.push(numbers[1])
            new_stack.push(numbers[2])
            new_stack.push(numbers[3])
            new_stack.push(ops[0])
            new_stack.push(ops[1])
            new_stack.push(ops[2])
            try:
                candidate = new_stack.evaluate()
                if candidate > 0 and int(candidate) == candidate:
                    collect.add(int(new_stack.evaluate()))
            except ZeroDivisionError:
                pass

    for numbers in permutations(stack.numbers):
        for ops in product(['+', '-', '*', '/'], repeat=3):
            new_stack = Stack(numbers)
            new_stack.push(numbers[0])
            new_stack.push(numbers[1])
            new_stack.push(ops[0])
            new_stack.push(numbers[2])
            new_stack.push(numbers[3])
            new_stack.push(ops[1])
            new_stack.push(ops[2])
            try:
                candidate = new_stack.evaluate()
                if candidate > 0 and int(candidate) == candidate:
                    collect.add(int(new_stack.evaluate()))
            except ZeroDivisionError:
                pass

    for numbers in permutations(stack.numbers):
        for ops in product(['+', '-', '*', '/'], repeat=3):
            new_stack = Stack(numbers)
            new_stack.push(numbers[0])
            new_stack.push(numbers[1])
            new_stack.push(ops[0])
            new_stack.push(numbers[2])
            new_stack.push(ops[1])
            new_stack.push(numbers[3])
            new_stack.push(ops[2])
            try:
                candidate = new_stack.evaluate()
                if candidate > 0 and int(candidate) == candidate:
                    collect.add(int(new_stack.evaluate()))
            except ZeroDivisionError:
                pass


def longest(collect):
    first = collect[0]
    count = 1
    for val in collect[1:]:
        if val == first + 1:
            count += 1
            first = val
        else:
            break
    return count


if __name__ == '__main__':
    max_len = 0
    for numbers in combinations(range(10), 4):
        collect = set()
        stack = Stack(numbers)
        build(stack, collect)
        collect = [a for a in collect]
        collect.sort()
        this_len = longest(collect)
        if this_len > max_len:
            max_len = this_len
            print(numbers)
            print(stack, max_len)
    print(max_len)

    """
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push("+")
    s.push("*")
    s.push("+")
    print s
    print s.evaluate()

    x = Stack()
    x.push_code(0)
    x.push_code(1)
    x.push_code(2)
    x.push_code(3)
    x.push_code(6)
    x.push_code(6)
    x.push_code(6)
    print x
    print x.evaluate()
    """

