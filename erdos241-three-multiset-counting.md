# Erdős #241 — exact elementary counting bound for distinct 3-multiset sums

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

Let `A⊂[N]` with `|A|=m`. Suppose all sums of three elements of `A`, with repetition allowed and order ignored, are distinct.

Then

`C(m+2,3) <= 3N-2`.

In particular,

`m^3 < 18N`.

## Proof

The number of unordered triples from `A` with repetition allowed is

`C(m+2,3)`.

By hypothesis they produce that many distinct integer sums.

Every such sum lies between `3` and `3N`, inclusive. That interval contains exactly

`3N-2`

integers. Therefore

`C(m+2,3) <= 3N-2`.

Since

`C(m+2,3)=m(m+1)(m+2)/6 > m^3/6`

and `3N-2<3N`, we obtain

`m^3 < 18N`.

## Correction boundary

Stronger constants such as 9 or 6 do not follow from this counting argument alone. The exact elementary output of the argument is the binomial inequality above and its consequence `m^3<18N`.

Historical novelty is not claimed.