import pathlib
import itertools
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from timeit import timeit

import isort
from isort import format

# target dir with modules
FILE = pathlib.Path("./test_files")


class SuppressionPrinter:
    def __init__(self, *_, **__):
        pass

    def success(self, *_):
        pass

    def error(self, *_):
        pass

    def diff_line(self, *_):
        pass


isort.format.BasicPrinter = SuppressionPrinter


# -----------------------------
# Test functions

def filelist_gen():
    """Chain directory list multiple times to get meaningful difference"""
    yield from itertools.chain.from_iterable([FILE.iterdir() for _ in range(1000)])


def isort_synchronous(path_iter):
    """Synchronous usual isort use-case"""

    # return list of results
    return [isort.check_file(file) for file in path_iter]


def isort_thread(path_iter):
    """Threading isort"""

    # prepare thread pool
    with ThreadPoolExecutor(max_workers=4) as executor:
        # start loading
        futures = [executor.submit(isort.check_file, file) for file in path_iter]

        # return list of results
        return [fut.result() for fut in futures]


def isort_multiprocess(path_iter):
    """Multiprocessing isort"""

    # prepare process pool
    with ProcessPoolExecutor(max_workers=4) as executor:
        # start loading
        futures = [executor.submit(isort.check_file, file) for file in path_iter]

        # return list of results
        return [fut.result() for fut in futures]


if __name__ == '__main__':
    # run once, no repetition
    n = 1

    # synchronous runtime
    print(f"Sync func : {timeit(lambda: isort_synchronous(filelist_gen()), number=n):.4f}")

    # threading demo
    print(f"Threading : {timeit(lambda: isort_thread(filelist_gen()), number=n):.4f}")

    # multiprocessing demo
    print(f"Multiproc : {timeit(lambda: isort_multiprocess(filelist_gen()), number=n):.4f}")

"""
Example Run Execution:

Sync func : 55.1276
Threading : 43.8236
Multiproc : 15.4720
"""