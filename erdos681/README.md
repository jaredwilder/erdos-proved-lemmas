# Erdős #681 — exact residual program, finite atlas, and parent-close frontier

**Author:** Jared Wilder  
**Status:** parent open; exact parent↔residual equivalence kernel-checked; substantial theorem/KBK estate established  
**Updated:** 2026-09-14

This page is the reader-facing index for the #681 work inside `erdos-proved-lemmas`. The campaign is treated as a theorem/obstruction/KBK program. The only terminal target remains the original eventual statement.

## Parent problem

For every sufficiently large integer `n`, does there exist an integer `k` such that `n+k` is composite and its least prime factor exceeds `k^2`?

## Exact parent ↔ prime-residual equivalence

The central formal object is [`../erdos681-residual-equivalence.lean`](../erdos681-residual-equivalence.lean). Its theorem `msl_erdos681_bundle_equivalence` kernel-checks the exact equivalence between the original parent and the residual statement:

> for every sufficiently large prime `p`, there exists an even shift `h>=2` such that `p+h` is composite and `(h+1)^2 < minFac(p+h)`.

Thus the parent close mission may work entirely on the prime residual **without weakening the problem**.

The elementary exposition is in [`../erdos681-fourth-root-search-reduction.md`](../erdos681-fourth-root-search-reduction.md).

## Kernel-checked bad integer near 10^12

The newest forensic pass recovered a formal theorem that the campaign narrative had buried:

\[
\boxed{n=999,997,304,512}
\]

has **no** admissible witness `k>0`.

See [`../erdos681-kernel-bad-n-999997304512.md`](../erdos681-kernel-bad-n-999997304512.md).

The exported Lean proof closes every positive shift: `k>=1001` is excluded by the fourth-root necessity, while every `1<=k<=1000` is certified either by primality of `n+k` or by an explicit divisor at most `k^2`. The 40 primality facts are established through Lucas/Pratt-style proofs. The cable receipt is `KERNEL_CHECKED`, and the source contains no `sorry`, `admit`, `native_decide`, or `ofReduceBool`.

Therefore any positive eventual threshold must satisfy

\[
N_0>999,997,304,512.
\]

This is an exact finite theorem, not a disproof of the eventual parent.

## Buried kernel theorem cluster

The raw campaign formalized more than its terminal narrative foregrounded. The recovered theorem cluster is published in:

- [`../erdos681-kernel-theorem-cluster-2026-09-14.md`](../erdos681-kernel-theorem-cluster-2026-09-14.md)
- [`../erdos681-local-sieve-kernel.lean`](../erdos681-local-sieve-kernel.lean)

Key exact facts include:

- fixed short shifts automatically satisfy the fourth-root size condition once `p>(K+1)^4`;
- if a prime `q<p` divides `k-1`, it cannot divide `p-1+k`;
- a prime `r>K` can divide at most one member of a `K`-shift window;
- among the 48 reduced classes modulo 105, exactly 33 kill the `k=3` residual shift, giving density `11/16`;
- exact small-modulus residue-decoding lemmas;
- a concrete modulus-growth receipt for the quantitative exceptional-set architecture;
- the `H=41` smooth-covering size trap.

## Witness geometry extracted from the campaign

If `m=n+k` is a witness endpoint, every prime factor of `m` exceeds `k^2`. Therefore

\[
m>k^{2\Omega(m)}.
\]

In particular,

\[
m<k^6\quad\Longrightarrow\quad \Omega(m)=2.
\]

So a witness near the fourth-root boundary is forced to be a semiprime or prime square. If `m=qr` with `q<=r`, then

\[
\frac rq<\frac{m}{k^4},
\]

forcing increasingly balanced factors as the endpoint approaches the boundary.

The full KBK note is [`../erdos681-prime-residual-kbk-2026-09-14.md`](../erdos681-prime-residual-kbk-2026-09-14.md).

## Finite atlas

The audited top-down campaign contains 85 clean chunks of width `10^10` covering

\[
1.5\times10^{11}\le p<10^{12}.
\]

Across those chunks:

- primes tested: **31,532,474,062**
- window-bad primes: **637,893**
- largest recorded window-bad prime: **999,997,304,513**

In the final chunk `[9.9e11,10^12]`, all 1,203 bad primes were also decomposed by certificate anatomy. Every one required prime exceptions; the observed minimum was 27, maximum 56, mean about 39.8. This is finite KBK about the parity obstruction, not a universal theorem.

## Analytic KBK frontier

The export went materially beyond the older density-zero notes. The repaired Gafni–Tao moment transfer now has an audited proof-sketch target

\[
\boxed{B(X)\ll \frac{X\log\log X}{\log^2X}},
\]

where `B(X)` counts bad residual primes in `(X,2X]`.

See [`../erdos681-exceptional-set-audited-sketch-2026-09-14.md`](../erdos681-exceptional-set-audited-sketch-2026-09-14.md).

Two hostile audits found and repaired several defects—wrong roughness threshold, an inadequate first-moment approximation, and a sliding-window constant—and found no fatal break in the final `K=log^2 X` architecture. The result is still labeled **audited sketch / source-binding debt**, not a finished theorem.

The forensic pass also found a stronger route that the internal campaign did not pursue: combine fixed higher moments of rough-number counts with factorial moments of the prime-rich case. The natural target is

\[
B(X)\stackrel{?}{\ll_r}\frac{X(\log\log X)^r}{\log^{r+1}X}
\]

for each fixed `r`, potentially giving `B(X)<<_A X/log^A X` for every fixed `A`. This is a **new research target**, not yet promoted.

## Parent-close bottleneck

The exact kernel facts convert a hypothetical bad prime into a constrained deterministic covering object. Across a fourth-root-sized shift window:

- every composite non-witness must have a small prime factor at most the shift square;
- divisors of `k-1` are unavailable to kill that shift;
- primes larger than the window can hit at most one shift;
- any shift escaping all such small factors must be prime, otherwise it is already a witness.

The new mission run quantified the obstruction rather than closing it. Near `10^12`, bad primes typically had about 500 candidate odd shifts, roughly 422 small-prime kills, about 36 one-off large-prime kills, and about 40 prime exceptions. Every bad prime in the final `10^10` chunk had at least 27 prime exceptions.

Several routes were shown to fail **in their tested forms**—ordinary sieve versus Brun–Titchmarsh constants, simple `k-1` divisor weighting, pure congruence propagation, and current short-interval bilinear methods. These are route-specific KBK, not a theorem that every possible parent-close mechanism is blocked.

The full close still needs a **universalization theorem**: show that the constrained covering-plus-prime-exception object cannot exist for all sufficiently large primes, or construct arbitrarily large bad primes and resolve the parent negatively.

No finite census, density-one theorem, conditional theorem, RH statement, weaker exponent, or declaration that known tools are insufficient is accepted as terminal closure.
