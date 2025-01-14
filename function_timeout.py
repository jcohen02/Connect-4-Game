'''Contains the definition of a decorator to timeout a function'''
from threading import Thread
import functools


def timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [TimeoutError('function [%s] timeout [%s seconds] exceeded!' % (func.__name__, timeout))]

            def newFunc():
                try:
                    res[0] = func(*args, **kwargs)
                except TimeoutError as e:
                    res[0] = e
            t = Thread(target=newFunc)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except TimeoutError as je:
                print('error starting thread')
                raise je
            ret = res[0]
            if isinstance(ret, BaseException):
                raise ret
            return ret
        return wrapper
    return deco
