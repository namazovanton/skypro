from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def unique_query(data, *args, **kwargs):
    return set(data)


def limit_query(value: str, data: Iterable[str]):
    return list(data[:int(value)])


def map_query(value: str, data: Iterable[str]):
    return map(lambda x: x.split(' ')[int(value)], data)


def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)
