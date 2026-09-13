# Erdős #936 — square–cube normal form and mod-8 restrictions for powerful numbers

**Author:** Jared Wilder  
**Status:** exact structural child theorem / congruence sieve; parent problem remains open  
**Historical novelty:** not asserted

## Powerful-number normal form

Recall that an integer `m>=1` is **powerful** if every prime dividing `m` occurs to exponent at least `2`.

### Theorem 1

Every powerful integer `m` can be written

\[
m=a^2b^3
\]

with `b` squarefree.

### Proof

Write

\[
m=\prod_p p^{e_p},
\]

where every nonzero `e_p>=2`.

For each such exponent:

- if `e_p` is even, write `e_p=2\alpha_p`;
- if `e_p` is odd, then `e_p>=3`, so write `e_p=2\alpha_p+3`.

Let

\[
a=\prod_p p^{\alpha_p}
\]

and let `b` be the product of the primes whose exponents `e_p` are odd. Then `b` is squarefree and

\[
m=a^2b^3.
\]

---

## Theorem 2 — the squarefree cube-kernel remembers an odd powerful number modulo 8

If `m` is odd and powerful and

\[
m=a^2b^3
\]

with `b` squarefree as above, then

\[
\boxed{b\equiv m\pmod8.}
\]

### Proof

Since `m` is odd, both `a` and `b` are odd. Hence

\[
a^2\equiv1\pmod8.
\]

Also every odd integer satisfies `b^2≡1 (mod 8)`, so

\[
b^3\equiv b\pmod8.
\]

Therefore

\[
m=a^2b^3\equiv b\pmod8.
\]

---

## Corollary — restrictions for `2^n-1` and `2^n+1`

Let `n>=3`.

### Minus case

If

\[
2^n-1
\]

is powerful and

\[
2^n-1=a^2b^3
\]

with `b` squarefree, then

\[
\boxed{b\equiv7\pmod8.}
\]

Indeed `2^n≡0 (mod 8)` for `n>=3`, so `2^n-1≡7 (mod 8)`, and Theorem 2 applies.

### Plus case

If

\[
2^n+1
\]

is powerful and

\[
2^n+1=a^2b^3
\]

with `b` squarefree, then

\[
\boxed{b\equiv1\pmod8.}
\]

Here `2^n+1≡1 (mod 8)`.

---

## Companion exact modulo-9 periodicity

For every integer `n>=0`,

\[
\boxed{9\mid 2^n+1\iff n\equiv3\pmod6.}
\]

### Proof

Powers of `2` modulo `9` have period `6`:

\[
2,4,8,7,5,1.
\]

The unique residue equal to `-1 mod 9` is `8`, occurring at exponent `3 mod 6`.

---

## Boundary

These congruence restrictions are necessary conditions inside the powerful-number branches studied in Erdős #936. They do not prove that `2^n-1` or `2^n+1` is or is not powerful for infinitely many `n`, and they do not close the parent problem.

The recovered estate explicitly separated this surviving congruence package from stronger campaign routes that did not close. This release promotes only the exact structural statements above.

No novelty claim is made for the elementary square–cube representation or congruence observations.