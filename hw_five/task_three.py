import view


def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def gen_fib(interval):
    view.task_three()
    fib = fibonacci()
    for i in range(interval):
        print(next(fib))
