# Erdős #385 — complete finite failure set below `10^6`

**Author:** Jared Wilder  
**Status:** exact finite computation, independently re-derived during September 2026 promotion

Define

\[
F(n)=\max\{m+\operatorname{lpf}(m): m<n,\ m\text{ composite}\},
\]

where `lpf(m)` is the least prime factor of `m`.

The exact set

\[
\{n<10^6:F(n)=n\}
\]

has **100 elements**, the largest being

\[
\boxed{267680}.
\]

The complete list is

```text
6, 8, 12, 14, 18, 20, 24, 30, 32, 42, 44, 48, 60, 62, 72, 74, 84, 90, 102, 104, 108, 110, 114,
132, 140, 168, 182, 198, 200, 234, 240, 242, 270, 272, 282, 284, 312, 314, 318, 354, 360, 390,
420, 422, 434, 462, 464, 468, 510, 572, 648, 660, 662, 762, 840, 884, 888, 942, 1064, 1110,
1302, 1304, 1308, 1430, 1434, 1440, 1452, 1454, 1488, 1490, 1494, 1500, 1572, 2004, 2114, 2352,
2394, 2400, 2622, 2688, 2690, 2694, 2700, 2862, 2970, 2972, 3042, 3540, 3542, 4290, 4974, 5418,
5420, 5852, 5862, 5880, 5882, 8742, 267672, 267680
```

Every one of these 100 values is of the form

\[
n=p+1
\]

with `p` prime.

## Independent promotion-time replay

The table was re-derived from the definition using a smallest-prime-factor sieve through `10^6`. The replay found:

```text
count   = 100
largest = 267680
all n-1 prime = true
```

This corrects smaller historical dossiers in the estate that listed only a strict subset of the failures.

## Scope

This is a **finite census below `10^6`**. The observation that every failure in this range is one more than a prime is part of the exact finite record; it is not promoted here to an unrestricted theorem for all `n`.
