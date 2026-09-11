# Erdős #406 — 3-adic exponent sieve and quantitative counting theorem

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Pass-3 quantitative upgrade:** 2026-09-11

## Exact congruence theorem

Suppose every ternary digit of `2^n` is either `0` or `1`. Then

\[
\boxed{n\bmod18\in\{0,2,6,8\}.}
\]

More generally, modulo `3^r`, the admissible exponents form exactly

\[
\boxed{2^{r-1}}
\]

residue classes modulo

\[
\varphi(3^r)=2\cdot3^{r-1}.
\]

### Proof

A residue modulo `3^r` whose first `r` ternary digits lie in `{0,1}` has the form

\[
\epsilon_0+\epsilon_1 3+\cdots+\epsilon_{r-1}3^{r-1}.
\]

Exactly half of the `2^r` such residues are units, namely those with `epsilon_0=1`. Since 2 is a primitive root modulo every power of 3, exponentiation by 2 bijects exponent classes modulo `phi(3^r)` with the units modulo `3^r`. Hence exactly `2^(r-1)` exponent classes survive.

For `r=3`, the surviving classes are `0,2,6,8 mod 18`.

## Quantitative Pass-3 theorem

Let `A(N)` count exponents `n<=N` surviving this necessary 3-adic condition. Put

\[
\alpha=\log_3 2.
\]

Then

\[
\boxed{A(N)=O(N^\alpha)}
\]

and, explicitly for `N>=1`,

\[
\boxed{A(N)\le\frac52N^{\log_3 2}.}
\]

### Proof

Write `t=r-1`. At level `r=t+1`, the survivors occupy exactly `2^t` residue classes modulo `2·3^t`. Therefore

\[
A(N)
\le
2^t\left(\frac{N}{2\cdot3^t}+1\right)
=
\frac N2\left(\frac23\right)^t+2^t.
\]

Choose

\[
t=\lfloor\log_3N\rfloor.
\]

Then `3^t<=N<3^(t+1)`, so

\[
\frac N2\left(\frac23\right)^t
=
\frac{N}{2\cdot3^t}2^t
<\frac32\,2^t.
\]

Thus

\[
A(N)<\frac52\,2^t.
\]

Finally

\[
2^t=(3^t)^{\log_3 2}\le N^{\log_3 2},
\]

which proves the explicit bound.

## Meaning and scope

The necessary exponent set therefore has **zero density and polynomially sublinear counting growth**. This is substantially stronger than merely listing congruence classes.

It still does **not** prove finiteness of the target exponent set or close the parent problem. The historical campaign also contained a malformed Senge–Straus-based close; that route remains quarantined and is not used here.
