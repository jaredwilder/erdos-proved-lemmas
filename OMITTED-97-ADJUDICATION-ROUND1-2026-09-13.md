# Omitted 97 families — adjudication round 1

**Author:** Jared Wilder  
**Date:** 2026-09-13  
**Purpose:** contradiction-history court for the recovered `05-OMITTED-97-FAMILIES-LATEST-PROVED-282.csv` ledger.

The source ledger contains 282 rows whose local/latest recorded status was `PROVED` across 97 problem families that were absent from an earlier public index. **A `PROVED` label in that ledger is a mining lead, not publication authority.** Later retractions, source-definition mismatches, quantifier drift, indexing corrections, and explicit counterexamples control.

This file records the first proposition-level adjudications.

## Released survivors

### Erdős #156 — corrected maximal-Sidon blocking theorem

**Disposition: RELEASED-CORRECTED.**

The old recorded inclusion

```text
[N] ⊆ A ∪ (A+A-A)
```

for maximal full-convention Sidon sets is false. The exact counterexample is

```text
N=3, A={1,3}, x=2.
```

`A` is maximal because adjoining `2` creates `1+3=2+2`, but `2∉A∪(A+A-A)`.

The later boundary audit repairs the theorem by restoring the midpoint obstruction:

```text
A maximal in [N]
iff
[N] ⊆ A ∪ (A+A-A) ∪ (A+A)/2.
```

The corrected count still yields

```text
N ≤ m + (m^3+2m^2-m)/2 ≤ m+2m^3,
```

for `m=|A|`.

Public writeup: `erdos156-maximal-sidon-corrected-blocking.md`.

### Erdős #251 — exact dyadic denominators

**Disposition: RELEASED.**

For the origin-zero `N`-term partial sum

```text
S_N = sum_{j=0}^{N-1} p_j / 2^j,
```

with `p_0=2`, the reduced denominator is `1` at `N=1` and exactly `2^(N-1)` for every `N≥2`. The proof is the all-`N` parity observation that, after clearing the common denominator, only the final odd-prime term survives modulo 2.

The parent irrationality problem is not closed: the campaign has no tail/transference theorem turning the partial-sum denominator fact into irrationality of the infinite limit.

Public writeup: `erdos251-prime-dyadic-denominators.md`.

### Erdős #893 — Mersenne divisor identities

**Disposition: RELEASED-WITH-NEGATIVE-CORRECTION.**

Surviving exact identities include

```text
tau(2^k-1) >= tau(k),

tau(2^(2m)-1) >= 2 tau(2^m-1),
```

and the exact multiplicative-order double-counting formula for

```text
f(n)=sum_{k<=n} tau(2^k-1).
```

A stronger attempted inequality

```text
tau(2^(2n)-1) >= tau(2^n-1)^2
```

is false at `n=4`, since `tau(255)=8 < 16=tau(15)^2`.

The parent full-tail divergence target remains open in the estate.

Public writeup: `erdos893-mersenne-divisor-identities.md`.

## Rejected historical PROVED labels

### Erdős #891 — distinct-prime versus multiplicity drift

**Disposition: REJECTED / DO NOT PROMOTE.**

Several recorded transference rows argued with `Omega`, the number of prime factors **with multiplicity**, while the frozen formal source uses `omega`, the number of **distinct** prime factors.

The exact counterexample is

```text
k=2,
n=13,
m=18=2*3^2.
```

Then

```text
Omega(18)=3,
omega(18)=2.
```

So the least-multiple construction does not produce the required `omega>k` witness. Later audit records explicitly refute the earlier closure claim.

No #891 close is published from those rows.

### Erdős #1210 — invalid gcd inference in claimed all-n proof

**Disposition: REJECTED AS GLOBAL PROOF; FINITE CERTIFICATE RETAINED.**

The frozen main statement assumes only

```text
A ⊆ [1,n),
gcd(a,b)=1 for distinct a,b∈A.
```

A later campaign row claimed that for `B={n-a:a∈A}` one has

```text
gcd(n-a1,n-a2) | gcd(a1,a2)=1,
```

and therefore `B` is pairwise coprime. That divisibility is false under the actual hypotheses.

For example,

```text
n=5,
a1=1,
a2=3,
gcd(a1,a2)=1,
```

but

```text
gcd(n-a1,n-a2)=gcd(4,2)=2.
```

The source self-check made the invalid step `a_i ≡ n (mod d) => d|a_i`; no hypothesis in the frozen problem supplies `d|n`.

Therefore the claimed uniform `C=1` all-`n` proof is not released.

What survives from the campaign is the separately scoped exact finite enumeration through `n≤6` and the already-public endpoint constraint that any valid uniform additive constant must satisfy `C≥1`. Those do not settle the global proposition.

## Rule established by this round

For every remaining row in the omitted-97 ledger, publication requires all of:

1. recover the exact frozen statement / definition;
2. distinguish finite certificate from analytic transfer;
3. search later contradiction history for `FALSE`, `RETRACT`, scope corrections, and source-definition mismatch;
4. independently sanity-check the proof's load-bearing inference;
5. publish the surviving proposition, not the campaign's confidence label.

This adjudication ledger will grow by rounds until all 282 rows have a public disposition.