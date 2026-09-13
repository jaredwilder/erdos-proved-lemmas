# Erdős #943 — the divisor-count domination `f(n) <= tau(n)` is false

**Author:** Jared Wilder  
**Status:** exact negative theorem / counterexample  
**Purpose:** preserve a route-killing result from the recovered campaign

Call a positive integer **powerful** if every prime appearing in its factorization appears to exponent at least two; `1` is powerful by the usual vacuous convention.

Let

\[
f(n)=\#\{(a,b): a,b\text{ powerful positive integers and }a+b=n\},
\]

where ordered pairs are counted.

A recovered route toward Erdős #943 proposed the pointwise domination

\[
f(n)\le \tau(n),
\]

with the intention of composing it with the classical subpolynomial maximal-order bound for the divisor function. That domination is false.

## Exact counterexample

At

\[
\boxed{n=153},
\]

we have

\[
153=3^2\cdot17,
\qquad
\tau(153)=(2+1)(1+1)=6.
\]

The complete list of ordered powerful pairs summing to 153 is

```text
(9,144)
(25,128)
(32,121)
(72,81)
(81,72)
(121,32)
(128,25)
(144,9)
```

and every displayed summand is powerful:

```text
9   = 3^2
144 = 2^4 * 3^2
25  = 5^2
128 = 2^7
32  = 2^5
121 = 11^2
72  = 2^3 * 3^2
81  = 3^4
```

Hence

\[
\boxed{f(153)=8>6=\tau(153)}.
\]

## Completeness of the pair list

The powerful positive integers below 153 are exactly

```text
1, 4, 8, 9, 16, 25, 27, 32, 36, 49,
64, 72, 81, 100, 108, 121, 125, 128, 144.
```

Checking the complement `153-a` for each member leaves exactly the eight ordered pairs above. Thus this is not merely a lower bound `f(153)>=8`; it is the exact value.

## What this kills

The failed route was

\[
f(n)\le\tau(n)=n^{o(1)}
\]

and therefore `f(n)=n^{o(1)}`.

The first inequality is false, so that proof route cannot be used. The counterexample does **not** refute the weaker target `f(n)=n^{o(1)}` itself; it refutes only this proposed divisor-count domination mechanism.

The conceptual error is also worth recording: `f(n)` counts **additive** representations `a+b=n`. There is no injection of those summands into the divisors of `n` merely because `a` and `b` are powerful.

## Independent promotion-time replay

The complete powerful-number list below 153 and all ordered complements were independently recomputed from prime factorizations before publication of this note. The result agrees with the later boundary/falsifier records in the recovered Pass-3 campaign.
