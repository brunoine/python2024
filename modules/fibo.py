# módulo fibonacci

def fib_print(n):
    """ escreve a série de Fibonacci até 'n' """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib_list(n):
    """ retorna uma lista com a série de Fibonacci até 'n' """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":
    # código que é executado caso este ficheiro fibo.py seja
    # executado como um script (e não via "import")

    import sys
    print("fibo.py invocado via script.")
    fib_print(int(sys.argv[1]))
