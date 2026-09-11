# Erdős #912 — primes occurring to exponent one in `n!`

**Author:** Jared Wilder  
**Release:** 2026-09-11

For a prime `p`,

\[
\boxed{v_p(n!)=1\iff n/2<p\le n.}
\]

Consequently the number of distinct primes appearing in `n!` with exponent exactly one is

\[
\boxed{\pi(n)-\pi(\lfloor n/2\rfloor).}
\]

## Proof

Legendre's formula gives

\[
v_p(n!)=\left\lfloor\frac np\right\rfloor+\left\lfloor\frac n{p^2}\right\rfloor+\cdots.
\]

If `n/2<p<=n`, then `floor(n/p)=1` and `p^2>n`, so all higher terms vanish and `v_p(n!)=1`.

Conversely, if `v_p(n!)=1`, then `p<=n`. If `p<=n/2`, the multiples `p` and `2p` both occur among `1,...,n`, forcing `v_p(n!)>=2`, contradiction. Hence `p>n/2`.

Counting primes in that interval gives the displayed formula.

## Scope boundary

This is exact Legendre bookkeeping. The parent problem concerns the number of distinct exponent values in the full prime factorization of `n!`; the theorem isolates the exponent-one stratum only.
