import numpy as np
import logging
from time import time

__author__ = 'gm'


def calc_limit(limit, num: int) -> int:
    """
    limits the number "num" based on the given limit
    :param limit: this is the limit to enforce on num, it may be an integer or a string. In case of an integer
    num is set to limit, or is left untouched if limit>num. In case of a string (eg format: %70) num is set to
    the percentage indicated by limit, in the example given it will be num * 0,7. If this is None the num is returned
    :param num: the number to limit
    :return: the num with the limit applied, this will be an int at all cases
    """
    ret = None
    if limit is None:
        ret = num
    elif isinstance(limit, int):
        ret = num if limit > num else limit
    elif isinstance(limit, str):
        if limit[0] == "%":
            l = float(limit[1:]) / 100
            assert 0 <= l <= 1
            ret = round(num * l)
        else:
            ret = num if int(limit) > num else int(limit)
    return ret


def euclidean_distance(l1: np.ndarray, l2: np.ndarray, k=None) -> float:
    """
    Calculate the euclidean distance between l1 and l2. Limit their size to k, if k is specified
    :return: the euclidean distance of l1[0:k] and l2[0:k] if k is given or of l1 and l2 if not
    """
    assert len(l1) == len(l2)
    s = 0
    if k is None or k > len(l1):
        k = len(l1)
    for i in range(k):
        s += np.power(np.abs(l1[i] - l2[i]), 2)  # np.abs is needed for complex numbers
    return np.sqrt(s)


def euclidean_distance_squared(l1: np.ndarray, l2: np.ndarray, k=None) -> float:
    """
    Calculate the squared euclidean distance between l1 and l2. Limit their size to k, if k is specified
    :return: the euclidean distance of l1[0:k] and l2[0:k] if k is given or of l1 and l2 if not
    """
    assert len(l1) == len(l2)
    if k is None or k > len(l1):
        k = len(l1)

    return np.linalg.norm(l1[:k] - l2[:k])**2


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time()
        ret = func(*args, **kwargs)
        stop = time()
        logging.debug("Function %s took %.3f min" % (func.__name__, (stop - start) / 60.))
        return ret
    wrapper.__name__ = func.__name__
    return wrapper

