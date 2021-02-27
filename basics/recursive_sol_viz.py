from visualiser.visualiser import Visualiser as vs

hmap = {}

@vs()
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def main():
    print(fib(6))
    vs.make_animation("fibonacci.gif", delay=2)


if __name__ == "__main__":
    main()
