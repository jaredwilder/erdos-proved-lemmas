# Erdős #238 — elementary `c_2<2` slice and the classical small-`c_1` theorem

**Author / reconstruction:** Jared Wilder  
**Public routing:** 2026-09-11; strengthened 2026-09-13  
**Priority note:** the small-`c_1` theorem below is classical. It is credited to Erdős (1949); no novelty claim is made.

## Frozen setting

The Erdős #238 formulation asks, for fixed `c_1,c_2>0` and all sufficiently large `x`, for a block of more than

\[
c_1\log x
\]

**consecutive primes**, all at most `x`, such that every pair of primes in the block differs by more than `c_2`.

For a consecutive prime block, the minimum pairwise difference is an adjacent gap. Thus the separation condition is equivalent to saying that every adjacent prime gap inside the block exceeds `c_2`.

---

## Theorem A — complete elementary slice `0<c_2<2`

Fix arbitrary `c_1>0` and `0<c_2<2`. Then the requested block exists for all sufficiently large `x`.

### Proof

Apart from the prime `2`, consecutive primes are odd. Any two distinct odd primes differ by an even positive integer and therefore by at least `2`. Thus when `c_2<2`, the separation condition is automatic inside any block of odd primes.

It remains only to have more than `c_1 log x` consecutive primes available below `x`. Since

\[
\pi(x)\sim\frac{x}{\log x},
\]

we have `pi(x) > c_1 log x + 1` for all sufficiently large `x`. Discard the initial prime `2` if necessary and take any consecutive block of the required length.

---

## Theorem B — classical small-`c_1` theorem for every fixed `c_2`

For every fixed `c_2>0`, there exists a constant

\[
\varepsilon(c_2)>0
\]

such that for every fixed

\[
0<c_1<\varepsilon(c_2),
\]

and all sufficiently large `x`, there are more than `c_1 log x` consecutive primes at most `x` whose adjacent gaps—and hence all pairwise differences—are greater than `c_2`.

This weaker quantifier order is classical; it is attributed to P. Erdős, **“On some applications of Brun’s method,”** *Acta Univ. Szeged. Sect. Sci. Math.* **13** (1949), 57–63, Theorem 3.

### Standard sieve input

Fix `c_2`. Let

\[
p_1<p_2<\cdots<p_n\le x
\]

be the primes up to `x`, so `n=pi(x)`. Call the position `i` **bad** if

\[
p_{i+1}-p_i\le c_2.
\]

Let `B_{c_2}(x)` be the number of bad positions. Brun/Selberg sieve gives, for each fixed `c_2`, a constant `C(c_2)` such that for all sufficiently large `x`,

\[
B_{c_2}(x)\le C(c_2)\frac{x}{\log^2x}.
\]

Only the existence of such a fixed constant is needed below.

### Exact window-covering lemma

Fix an integer `k>=2`. Among `n` ordered primes there are exactly

\[
n-k+1
\]

windows of `k` consecutive primes.

A single bad position `i` can lie inside at most `k` such windows. Therefore, if every length-`k` window contained a bad gap, then necessarily

\[
B_{c_2}(x)\ge\frac{n-k+1}{k}.
\]

Contrapositively,

\[
\boxed{
B_{c_2}(x)<\frac{n-k+1}{k}
\Longrightarrow
\text{some length-`k` consecutive-prime window has all gaps }>c_2.
}
\]

No independence assumption is used; this is a deterministic covering count.

### Completing the proof

By the prime number theorem,

\[
n=\pi(x)\sim\frac{x}{\log x}.
\]

Choose any sufficiently small positive `c_1` depending only on `c_2`, and take

\[
k=\lfloor c_1\log x\rfloor+1.
\]

Then `k>c_1 log x` and `k=O(log x)`. Using the sieve bound and PNT,

\[
B_{c_2}(x)
=O_{c_2}\!\left(\frac{x}{\log^2x}\right),
\]

while

\[
\frac{n-k+1}{k}
\asymp
\frac{x}{c_1\log^2x}.
\]

Taking `c_1` small enough relative to the chosen sieve/PNT constants makes

\[
B_{c_2}(x)<\frac{n-k+1}{k}
\]

for all sufficiently large `x`. The window-covering lemma then produces a block of `k>c_1 log x` consecutive primes with every adjacent gap greater than `c_2`.

That proves Theorem B.

### About the constant

The recovered campaign sometimes wrote the threshold schematically as `c_1<1/C(c_2)` and elsewhere used a conservative `1/(2C(c_2))`, depending on how PNT slack and the sieve constant were normalized. This public note deliberately states only the invariant mathematical conclusion:

> for each fixed `c_2`, some positive `epsilon(c_2)` exists.

No optimal or canonical explicit constant is claimed here.

---

## What remains open

The full Erdős #238 question has the stronger order of quantifiers:

\[
\forall c_1>0\ \forall c_2>0.
\]

Theorem B proves only

\[
\forall c_2>0\ \exists\varepsilon(c_2)>0\ \forall\,0<c_1<\varepsilon(c_2).
\]

So it does **not** close the parent problem for arbitrary large `c_1`.

The internal campaign independently reconstructed this classical small-`c_1` argument, passed it through its hostile audit, and correctly refused to promote it to a full #238 close. A later literature collision identified Erdős's 1949 priority, so this release records the result as an **independent rediscovery / public-surface repair**, not a new theorem.