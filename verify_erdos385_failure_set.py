#!/usr/bin/env python3
LIMIT = 1_000_000
EXPECTED_COUNT = 100
EXPECTED_LARGEST = 267680


def smallest_prime_factors(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


def main():
    spf = smallest_prime_factors(LIMIT)
    current = 0
    failures = []
    for n in range(2, LIMIT):
        m = n - 1
        if m >= 4 and spf[m] != m:  # composite
            current = max(current, m + spf[m])
        if current == n:
            failures.append(n)

    assert len(failures) == EXPECTED_COUNT, len(failures)
    assert failures[-1] == EXPECTED_LARGEST, failures[-1]
    assert all(spf[n - 1] == n - 1 for n in failures)

    print("PASS")
    print(f"limit={LIMIT}")
    print(f"count={len(failures)}")
    print(f"largest={failures[-1]}")
    print("all_n_minus_1_prime=true")
    print(",".join(map(str, failures)))


if __name__ == "__main__":
    main()
