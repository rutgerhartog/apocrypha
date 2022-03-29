import numpy as np
from math import log


def shannon_entropy(text: bytes) -> float:
    """
    Computes the Shannon entropy of a sequence of bytes.
    :param bytes: a sequence of bytes
    :returns: the Shannon entropy, as a float between 0 and 8.
    """

    entropy = 0.0

    labels = [i for i in text]

    value, counts = np.unique(labels, return_counts=True)

    if len(counts) <= 1:
        return entropy  # ie. return 0

    probabilities = counts / len(labels)

    if np.count_nonzero(probabilities) <= 1:
        return entropy

    for item in probabilities:
        entropy -= item * log(item, 2)

    return entropy
