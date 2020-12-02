import typing as tp

T = tp.TypeVar('T')


def _read_input_file(
        filename: str,
        cast: tp.Callable[[str], T],
) -> tp.Iterable[T]:
    with open(filename, 'rt') as input_file:
        for line in input_file:
            yield cast(line)


def read_ints(filename: str) -> tp.Iterable[int]:
    return _read_input_file(filename, int)
