from typing import Optional, Iterable
from query_commands import filter_query, map_query, unique_query, sort_query, limit_query

commands_to_functions = {
    "filter": filter_query,
    "map": map_query,
    "unique": unique_query,
    "sort": sort_query,
    "limit": limit_query
}


def read_file(file_name: str):
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]):
    if data is None:
        prepared_data = read_file(file_name)
    else:
        prepared_data = data

    return list(commands_to_functions[cmd](value=value, data=prepared_data))


