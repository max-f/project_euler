limit = 200000
all_numbers = list()
primes = list()


def main():
    all_numbers.append(False)
    for i in range(2, limit):
        all_numbers.append(True)
    while all_numbers.count(True) > 0 and len(primes) < 10001:
        k = all_numbers.index(True)
        primes.append(k + 1)
        print(k + 1)
        all_numbers[k] = False
        i = 1
        while i * (k + 1) <= len(all_numbers):
            all_numbers[i * (k + 1) - 1] = False
            i = i + 1
    print(len(primes))

main()
