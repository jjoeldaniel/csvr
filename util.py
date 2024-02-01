def convert_key(key: tuple[int, ...]) -> int | tuple[int, ...]:
    if len(key) == 1:
        return key[0]
    return key
