"""

A small collection of functions.

"""


def foo(a=1, b=2):
    c = a + b
    return c

def bar(d=3, e=4):
    print('Hello from biz.bar()!')
    return d

if __name__ == '__main__':
    bar()
