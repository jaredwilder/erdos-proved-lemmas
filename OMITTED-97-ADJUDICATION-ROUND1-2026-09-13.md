# Omitted 97 families — adjudication round 1

**Author:** Jared Wilder  
**Date:** 2026-09-13  
**Purpose:** contradiction-history court for the recovered `05-OMITTED-97-FAMILIES-LATEST-PROVED-282.csv` ledger.

The source ledger contains 282 rows whose local/latest recorded status was `PROVED` across 97 problem families that were absent from an earlier public index. **A `PROVED` label in that ledger is a mining lead, not publication authority.** Later retractions, source-definition mismatches, quantifier drift, indexing corrections, and explicit counterexamples control.

This file records proposition-level adjudications. It is updated cumulatively rather than spawning one status file per pass.

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

### Erdős #197 — finite beautiful-order theorem

**Disposition: RELEASED WITH FINITE/INFINITE BOUNDARY.**

Every finite `S⊂N` admits a linear order with no positional three-term arithmetic progression. The recursive construction places the recursively ordered odd elements before the recursively ordered even elements; a forbidden triple either has an impossible cross-parity equation, has its midpoint in the wrong top-level block, or descends after dividing by two.

Consequently every finite two-partition of `[N]` has both parts separately reorderable to avoid monotone 3-APs.

This does **not** settle canonical #197: the infinite problem requires genuine bijections `N≃A` and `N≃B`. The odds-before-evens recursion on an infinite set need not have order type `ω`, and finite avoiding orders do not automatically yield compatible infinite bijective enumerations.

Public writeup: `erdos197-finite-beautiful-orders.md`.

### Erdős #251 — exact dyadic denominators

**Disposition: RELEASED.**

For the origin-zero `N`-term partial sum

```text
S_N = sum_{j=0}^{N-1} p_j / 2^j,
```

with `p_0=2`, the reduced denominator is `1` at `N=1` and exactly `2^(N-1)` for every `N≥2`. The proof is the all-`N` parity observation that, after clearing the common denominator, only the final odd-prime term survives modulo 2.

The parent irrationality problem is not closed: the campaign has no tail/transference theorem turning the partial-sum denominator fact into irrationality of the infinite limit.

Public writeup: `erdos251-prime-dyadic-denominators.md`.

### Erdős #513 — exact Poisson-term maximizer

**Disposition: RELEASED AS CLASSICAL CHILD THEOREM.**

For `a_n(r)=r^n/n!`, the exact ratio

```text
a_{n+1}/a_n = r/(n+1)
```

shows that the unique maximizer is `floor(r)` when `r` is nonintegral, while positive integer `r=m` gives the unique tie `n=m-1,m`. The sequence is strictly decreasing for `n≥ceil(r)`, and Stirling gives

```text
max_n r^n/n! ~ e^r/sqrt(2*pi*r).
```

This cleanly implies the Erdős-513 functional has value `0` at `f(z)=e^z`, but does not determine its supremum over all transcendental entire functions.

Public writeup: `erdos513-poisson-term-argmax.md`.

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

### Erdős #996 — rational-alpha pointwise obstruction, corrected

**Disposition: RELEASED-CORRECTED AS SCOPE OBSTRUCTION.**

For

```text
n_k = 2^k,
f(x) = exp(2*pi*i*x),
alpha = 1/7,
```

the Fourier-tail hypothesis is satisfied with eventual error zero, while the sampled values cycle over `zeta,zeta^2,zeta^4` for `zeta=e^(2*pi*i/7)`.

The historical certificate claimed

```text
zeta + zeta^2 + zeta^4 = -1,
```

which is false. The correct exact identity is

```text
s = zeta + zeta^2 + zeta^4,
s^2+s+2=0,
```

so `s≠0` and the Cesàro limit is `s/3≠0`; in radical form it is `(-1+i*sqrt(7))/6` for the chosen root.

Thus the almost-everywhere qualifier in #996 is genuinely load-bearing: a pointwise-for-every-alpha strengthening is false. A single rational alpha has measure zero, so this does **not** refute the canonical a.e. statement.

Public writeup: `erdos996-rational-alpha-obstruction.md`.

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

### Erdős #943 — additive/Dirichlet convolution operation mismatch

**Disposition: REJECTED AS CLOSE / DO NOT PROMOTE MULTIPLICATIVE PROOF.**

The canonical problem uses the additive representation count for powerful numbers. Several historical green rows silently treated `1_A*1_A` as Dirichlet convolution and therefore used prime-power multiplicativity and divisor-count domination.

The later audit gives a direct interior counterexample to the load-bearing inequality: at `n=153` there are eight ordered powerful-sum representations, coming from

```text
(9,144), (81,72), (25,128), (32,121)
```

and their reversals, whereas `tau(153)=6`.

Thus the claimed universal bound `f(n)≤tau(n)` is false for the actual additive problem. The canonical `n^{o(1)}` question itself is not refuted by this counterexample; the old proof solved the wrong operation.

### Erdős #1203 — boundedness/negative close contradicted

**Disposition: REJECTED AS CLOSE.**

Historical rows claimed a uniform bound such as `F(n)≤2`, hence a negative resolution of the canonical divergence statement. Later exact state contradicts this. For

```text
n=510495,
k=15,
n+k=510510=2*3*5*7*11*13*17,
```

one has seven distinct prime factors and

```text
7*log(log 15)/log 15 > 2.575.
```

The later target state explicitly records `CASE NONE`: boundedness routes are false, while the surviving primorial construction supplies only subsequence unboundedness, a listed non-result for the full-tail limit `F(n)->infinity`.

No #1203 close is published.

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

## Non-close structural findings retained

Some rows are mathematically useful precisely because they explain why a tempting proof architecture cannot settle the parent problem.

- **#197:** every finite set is avoidably orderable, so finite-window search has zero discriminatory power; the missing object is a genuine infinite bijective-order construction/compactness theorem.
- **#996:** rational periodic orbits kill pointwise-for-all-alpha variants, but not an almost-everywhere statement.
- **#501:** hostile finite proxies can have independence number one even though the continuum clauses are measure-theoretic; the campaign's own closer refuses finite-to-continuum transfer. These rows remain forensic structure, not theorem promotion.

## Rule established by this court

For every remaining row in the omitted-97 ledger, publication requires all of:

1. recover the exact frozen statement / definition;
2. distinguish finite certificate from analytic transfer;
3. search later contradiction history for `FALSE`, `RETRACT`, scope corrections, and source-definition mismatch;
4. independently sanity-check the proof's load-bearing inference;
5. verify that overloaded notation denotes the same operation as in the canonical problem;
6. recompute exact algebra when a certificate depends on a symbolic identity;
7. publish the surviving proposition, not the campaign's confidence label.

This adjudication ledger will continue growing until all 282 rows have a public disposition.