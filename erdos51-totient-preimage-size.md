# Erdős #51 — elementary size bound for totient preimages

Author: Jared Wilder  
Public release: 2026-09-11

Let `phi(n)=a`, and let `r=omega(n)` be the number of distinct prime divisors of `n`. Define

`R(a)=max{r>=0 : r!<=a}`.

## Theorem

Every totient preimage `n` of `a` satisfies

`n <= a * 2^R(a)`.

In particular the least preimage `n_a`, whenever it exists, satisfies the same bound.

## Proof

Write the distinct prime divisors of `n` as

`p_1<...<p_r`.

Euler's product formula gives

`a=phi(n)=n product_{p|n}(1-1/p)`

and therefore

`n/a = product_{p|n} p/(p-1) <= 2^r`,

since `p/(p-1)<=2` for every prime.

Also `phi(n)` is divisible by `product_i (p_i-1)`. Since the `i`-th distinct prime satisfies `p_i>=i+1`,

`a >= product_i (p_i-1) >= r!`.

Thus `r<=R(a)`, and hence

`n <= a 2^r <= a 2^R(a)`.

Using the standard asymptotic inversion of `r!`, this also yields

`n <= a^(1+(log 2+o(1))/log log a)`

along totient values tending to infinity.

## Scope

This controls the size of every preimage but does not decide whether the ratio of the *least* preimage to `a` can tend to infinity along an infinite set, which is the canonical Erdős #51 question.

Historical novelty is not claimed; this is an elementary structural reduction reconstructed from the Day-One ore.

## License

Apache-2.0.
