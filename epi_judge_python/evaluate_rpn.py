from test_framework import generic_test


def evaluate(expression: str) -> int:

    def operate(x, y, op):
        if op == '+':
            return y + x
        elif op == '-':
            return y - x
        elif op == '*':
            return y * x
        elif op == '/':
            return y // x

    operators = ['+', '-', '*', '/']
    numbers = []

    for c in expression.split(','):
        if c in operators:
            numbers.append(operate(numbers.pop(), numbers.pop(), c))
        else:
            numbers.append(int(c))
    return numbers[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
