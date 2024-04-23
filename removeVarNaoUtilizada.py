import math
import sys


def foo():
    try:
        import multiprocessing
        print(multiprocessing.cpu_count())
    except ImportError as exception:
        print(sys.version)
    return math.pi