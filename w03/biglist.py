import sys
import timeit
import psutil


def main(n):
    numbers = [i + 1 for i in range(n)]
    total_sum = sum(numbers)
    print(f'Suma liczb od 1 do {n} wynosi: {total_sum}')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        print('Podaj wartość n jako argument programu.')
        sys.exit(1)

    time_taken = timeit.timeit(lambda: main(n), number=1)
    process = psutil.Process()
    memory_usage_kb = process.memory_info().rss / 1024

    print(f'{time_taken:.2f} sec. {memory_usage_kb:.2f} kB')
