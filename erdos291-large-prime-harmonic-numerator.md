# Erdős #291 — primes above n/2 do not divide the harmonic numerator

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted theorem, independently rechecked

Let

\[
H_n=\sum_{k=1}^n \frac1k,
\qquad
L_n=\operatorname{lcm}(1,2,\ldots,n),
\]

and write

\[
H_n=\frac{A_n}{L_n},
\qquad
A_n=\sum_{k=1}^n\frac{L_n}{k}.
\]

## Theorem

If `p` is prime and

\[
\frac n2<p\le n,
\]

then

\[
\boxed{p\nmid A_n.}
\]

Consequently `p` also does not divide the numerator of `H_n` in lowest terms.

## Proof

Because `p>n/2`, the only multiple of `p` in `{1,\ldots,n}` is `p` itself. Also `p^2>n`, so `p` occurs to exponent exactly one in `L_n`.

Reduce

\[
A_n=\sum_{k=1}^n L_n/k
\]

modulo `p`. If `k\ne p`, then the factor `p` remains in `L_n/k`, so that summand is `0 mod p`. The sole surviving term is

\[
\frac{L_n}{p},
\]

which is nonzero modulo `p` because `p` occurs only once in `L_n`. Hence

\[
A_n\equiv L_n/p\not\equiv0\pmod p.
\]

If the fraction `A_n/L_n` is reduced by a common divisor, division cannot introduce a factor `p` into the numerator. Thus the reduced numerator is also nonzero modulo `p`.

## Scope

This is a clean large-prime exclusion theorem for the numerator of a harmonic number. It is distinct from the separately released leading-`p` criterion using the largest power `p^e<=n`; neither statement alone resolves the parent problem.
