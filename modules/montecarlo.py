import numpy as np


def create_pair(
    tuple_list: list[np.float64], order_linearly: bool = True
) -> list[tuple]:
    """
    Takes a list and returns a list of pairs
    """
    result = []

    if not order_linearly:
        np.random.shuffle(tuple_list)

    for i in range(len(tuple_list)):
        try:
            result.append((tuple_list[i], tuple_list[i + 1]))
        except IndexError:
            break

    return result


def monte_carlo(text: bytes, order_linearly: bool = True) -> float:
    text_list = [i for i in text]
    text_array = np.array(text_list)

    text_array = text_array / 255

    print(text_array)

    pi = 0
    pairs = create_pair(text_array, order_linearly=order_linearly)

    print(pairs)

    for pair in pairs:
        if np.sqrt(np.square(pair[0]) + np.square(pair[1])) <= 1:
            pi += 1

    pi = 4 * float(pi) / len(pairs)

    return np.abs(np.pi - pi)
