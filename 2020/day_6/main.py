import typing as tp

from lib import input_utils


def read_groups(filename: str) -> tp.List[str]:
    group = []
    for answer in input_utils.read_str(filename):
        if answer == '':
            yield group
            group = []
        else:
            group.append(answer)
    yield group


if __name__ == '__main__':
    def part_1():
        groups = read_groups(
            '/home/i2/projects/aoc/2020/day_6/puzzle.input'
        )
        result = 0

        for group in groups:
            unique_group_answers = set()
            for answer in group:
                unique_group_answers |= set(answer)

            result += len(unique_group_answers)

        print(result)

    part_1()


    def part_2():
        groups = read_groups(
            '/home/i2/projects/aoc/2020/day_6/puzzle.input'
        )
        result = 0

        for group in groups:
            common_group_answers = None
            for answer in group:
                if common_group_answers is None:
                    common_group_answers = set(answer)
                    continue

                common_group_answers &= set(answer)

            result += len(common_group_answers)

        print(result)

    part_2()
