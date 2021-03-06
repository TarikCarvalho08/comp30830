import socket
import platform
import multiprocessing
import psutil
import timeit
import itertools

main():
t_default = 6.388216104
start_time = timeit.default_timer()
bench_pidigits(ndigits=1000, loops=100)
elapsed_time = timeit.default_timer() - start_time
print('relative elapsed:' + str(elapsed_time / t_default))


hostname = socket.gethostname()
print("Machine name = " + socket.gethostname())
print("Operating system name = " + platform.system())
print("Operating system version = " + platform.release())
print("Number of cpu's = " + str(multiprocessing.cpu_count()))
print("Amount of memory = " + str(psutil.virtual_memory().total))
print("IP address of machine = " + socket.gethostbyname(hostname))


def bench_pidigits(ndigits=1000, loops=100):
    def calc_ndigits(n):
        # Adapted from code on http://shootout.alioth.debian.org/
        def gen_x():
            return map(lambda k: (k, 4 * k + 2, 0, 2 * k + 1), itertools.count(1))

        def compose(a, b):
            aq, ar, as_, at = a
            bq, br, bs, bt = b
            return (aq * bq,
                    aq * br + ar * bt,
                    as_ * bq + at * bs,
                    as_ * br + at * bt)

        def extract(z, j):
            q, r, s, t = z
            return (q * j + r) // (s * j + t)

        def pi_digits():
            z = (1, 0, 0, 1)
            x = gen_x()
            while 1:
                y = extract(z, 3)
                while y != extract(z, 4):
                    z = compose(z, next(x))
                    y = extract(z, 3)
                z = compose((10, -10 * y, 0, 1), z)
                yield y

            return list(itertools.islice(pi_digits(), n))

        for _ in range(loops):
            calc_ndigits(ndigits)
        # print(âPi:â, ââ.join(map(str, calc_ndigits(ndigits))))
        return

        # return perf.perf_counter() - t0

if __name__ == '__main__':
    main()
