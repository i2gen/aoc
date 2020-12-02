import typing as tp

from lib import input_utils


def two_sum(
        stream: tp.Iterable[int],
        target: int,
) -> tp.Optional[tp.Tuple[int, int]]:
    cache = set()

    for e in stream:
        expected = target - e
        if expected in cache:
            return e, expected

        cache.add(e)

    return None


def three_sum(
        stream: tp.Iterable[int],
        target: int,
) -> tp.Optional[tp.Tuple[int, int, int]]:
    cache = set(stream)

    for e in cache:
        expected = target - e
        ts = two_sum(cache, expected)

        if ts is None:
            continue

        first, second = ts
        return first, second, e

    return None


if __name__ == '__main__':
    def part_1():
        data = input_utils.read_ints(
            '/home/i2/projects/aoc/2020/day_1/puzzle.input'
        )
        nums = two_sum(data, 2020)

        if nums is None:
            raise RuntimeError('aaargh')

        a, b = nums
        print(a, b, a * b)

    def part_2():
        data = input_utils.read_ints(
            '/home/i2/projects/aoc/2020/day_1/puzzle.input'
        )
        nums = three_sum(data, 2020)

        if nums is None:
            raise RuntimeError('aaargh')

        a, b, c = nums
        print(a, b, c, a * b * c)

    part_1()
    part_2()
