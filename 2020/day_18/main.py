import typing as tp
import operator

from lib import input_utils

OPS = {
    '+': operator.add,
    '*': operator.mul,
}

OP_SET = frozenset(OPS.keys())


def infix_to_polish(
        expression: str,
        priorities: tp.Dict[str, int],
) -> tp.List[tp.Union[int, str]]:
    result = []
    stack = []

    for token in expression.split():
        if token.isnumeric():
            result.append(int(token))
            continue

        if token == '(':
            stack.append(token)

        if token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # throw away '('

        if token in OP_SET:
            while stack:
                head = stack[-1]
                if head not in OP_SET:
                    break

                if priorities[head] < priorities[token]:
                    break

                result.append(stack.pop())
            stack.append(token)

    result.extend(reversed(stack))
    return result


def wrap_brackets(expression: str) -> str:
    return expression.replace('(', '( ').replace(')', ' )')


def evaluate(polish_expression: tp.List[tp.Union[int, str]]) -> int:
    stack = []

    for token in polish_expression:
        if token in OP_SET:
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(OPS[token](op1, op2))
            continue

        stack.append(token)

    if len(stack) != 1:
        raise RuntimeError(stack)

    return stack[0]


if __name__ == '__main__':
    def part_1():
        expressions = input_utils.read_str(
            '/home/i2/projects/aoc/2020/day_18/puzzle.input'
        )

        priorities = {
            '+': 1,
            '*': 1,
        }

        result = 0
        for e in expressions:
            result += evaluate(infix_to_polish(wrap_brackets(e), priorities))

        print(result)

    part_1()


    def part_2():
        expressions = input_utils.read_str(
            '/home/i2/projects/aoc/2020/day_18/puzzle.input'
        )

        priorities = {
            '+': 1,
            '*': 0,
        }

        result = 0
        for e in expressions:
            result += evaluate(infix_to_polish(wrap_brackets(e), priorities))

        print(result)

    part_2()