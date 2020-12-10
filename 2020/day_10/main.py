import typing as tp

import collections
import functools

from lib import input_utils


def build_graph(adapters: tp.Iterable[int]):
    adapters = set(adapters)

    graph = {}

    adapters.add(0)

    for adapter in adapters:
        childs = []
        for i in range(1, 4):
            matched = adapter + i
            if matched in adapters:
                childs.append(matched)
        graph[adapter] = childs

    return graph



if __name__ == '__main__':
    def part_1():
        adapters = input_utils.read_ints(
            '/home/i2/projects/aoc/2020/day_10/puzzle.input'
        )

        input_rate = 0

        adapters = sorted(adapters)

        memo = collections.defaultdict(lambda: 0)

        for adapter_rate in adapters:
            diff = adapter_rate - input_rate
            assert 0 < diff <= 3
            memo[diff] += 1
            input_rate = adapter_rate

        memo[3] += 1

        print(memo[1] * memo[3])

    part_1()


    def part_2():
        adapters = input_utils.read_ints(
            '/home/i2/projects/aoc/2020/day_10/puzzle.input'
        )

        adapters = list(adapters)

        graph = build_graph(adapters)

        @functools.lru_cache(None)
        def count_paths(v) -> int:
            if not graph[v]:
                return 1

            n = 0
            for ch in graph[v]:
                n += count_paths(ch)
            return n

        print(count_paths(0))

    part_2()
