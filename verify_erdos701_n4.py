def is_downset(fmask: int, n: int) -> bool:
    for s in range(1 << n):
        if (fmask >> s) & 1:
            sub = s
            while True:
                if not ((fmask >> sub) & 1):
                    return False
                if sub == 0:
                    break
                sub = (sub - 1) & s
    return True


def largest_star(family, n: int) -> int:
    return max(
        (sum(1 for s in family if s & (1 << i)) for i in range(n)),
        default=0,
    )


def largest_intersecting(family) -> int:
    verts = [s for s in family if s != 0]
    L = len(verts)
    adj = []
    for i, s in enumerate(verts):
        mask = 0
        for j, t in enumerate(verts):
            if i != j and (s & t):
                mask |= 1 << j
        adj.append(mask)

    best = 0

    def expand(P: int, size: int) -> None:
        nonlocal best
        if size + P.bit_count() <= best:
            return
        while P:
            if size + P.bit_count() <= best:
                return
            bit = P & -P
            v = bit.bit_length() - 1
            P ^= bit
            expand(P & adj[v], size + 1)
            best = max(best, size + 1)

    expand((1 << L) - 1, 0)
    return best


def main() -> None:
    expected = {1: 3, 2: 6, 3: 20, 4: 168}
    counts = {}

    for n in range(1, 5):
        count = 0
        for fmask in range(1 << (1 << n)):
            if not is_downset(fmask, n):
                continue
            count += 1
            family = [s for s in range(1 << n) if (fmask >> s) & 1]
            assert largest_intersecting(family) <= largest_star(family, n)
        counts[n] = count

    assert counts == expected, counts
    assert sum(counts.values()) == 197
    print("Erdos 701 n<=4 exhaustive check: PASS", counts)


if __name__ == "__main__":
    main()
