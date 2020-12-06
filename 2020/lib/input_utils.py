import typing as tp

T = tp.TypeVar('T')

def _strip_nl(value: str) -> str:
    return value.rstrip('\n')


def _identity(value: T) -> T:
    return value


def _read_input_file(
        filename: str,
        cast: tp.Callable[[str], T],
) -> tp.Iterable[T]:
    with open(filename, 'rt') as input_file:
        for line in input_file:
            yield cast(_strip_nl(line))


def read_str(filename: str) -> tp.Iterable[str]:
    return _read_input_file(filename, _identity)


def read_ints(filename: str) -> tp.Iterable[int]:
    return _read_input_file(filename, int)
