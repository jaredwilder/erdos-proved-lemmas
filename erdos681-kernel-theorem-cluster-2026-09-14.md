# Erdős #681 — kernel theorem cluster recovered from the campaign

**Author:** Jared Wilder  
**Date:** 2026-09-14  
**Status:** exact reductions and local sieve lemmas; parent problem remains the target.

A second raw-byte mining pass found that the 100-round campaign formalized substantially more than its terminal narrative foregrounded. This note promotes the strongest kernel-checked pieces as mathematics in their own right and identifies how they constrain the remaining parent-close problem.

## 1. The parent is exactly equivalent to the prime-residual problem

The public Lean bundle [`erdos681-residual-equivalence.lean`](erdos681-residual-equivalence.lean) contains a single theorem

`msl_erdos681_bundle_equivalence`

proving the equivalence between:

1. the original eventual statement: for all sufficiently large `n`, there exists `k>0` such that `n+k` is composite and `k^2 < minFac(n+k)`;
2. the prime residual: for all sufficiently large primes `p`, there exists `h>=2` such that `p+h` is composite and `(h+1)^2 < minFac(p+h)`.

This is stronger than merely keeping the two reduction directions separately in prose: the parent close target can be frozen to the residual statement with no loss of scope.

## 2. Every fixed short shift is automatically inside the fourth-root window

The theorem

`msl_erdos681_fixed_K_in_window`

states that

\[
(K+1)^4<p,\qquad 1\le k\le K
\]

implies

\[
k^4<p-1+k.
\]

Thus once `p` is sufficiently large relative to a fixed shift budget, fourth-root admissibility is not the obstruction. The obstruction is arithmetic: finding a composite shift whose least prime factor exceeds `k^2`.

## 3. A divisor of `k-1` is unavailable as a killing factor

For primes `p,q` with `q<p`, the kernel theorem

`msl_erdos681_divisor_of_shift_is_free`

proves

\[
q\mid k-1 \quad\Longrightarrow\quad q\nmid p-1+k.
\]

The more general repaired theorem

`msl_erdos681_exempt_family_core_r2`

records the algebraic core: if `M | k-1`, `q | M`, and `q | p-1+k`, then `q | p`. The first formalization attempt exposed a truncated-natural subtraction hypothesis; the repaired version adds the needed positivity assumption and kernel-checks. The repair is retained as KBK rather than erased.

For a prime input `p>q`, divisors of `k-1` are therefore **exempt** from the small-prime factors that can kill the shift.

## 4. A prime larger than the window can hit at most one shift

The theorem

`msl_erdos681_large_prime_hits_one_shift`

proves that if

\[
k<k'\le K<r,
\]

then `r` cannot divide both `p+k` and `p+k'`.

Equivalently, every prime `r>K` is a one-shift resource inside a `K`-window. This is an exact collision restriction on any attempted covering of all candidate shifts by bad small factors.

Together with the exempt-family theorem, this turns a hypothetical bad prime into a constrained set-cover object rather than an arbitrary collection of divisibilities.

## 5. Exact small-modulus local data

The newly published [`erdos681-local-sieve-kernel.lean`](erdos681-local-sieve-kernel.lean) contains the kernel-checked finite arithmetic layer.

### Exact `k=3` density

Among the `48` reduced residue classes modulo `105`, exactly `33` satisfy

\[
\gcd(a+2,105)>1.
\]

Hence the exact local killing density is

\[
\boxed{33/48=11/16}.
\]

The original formal attempt used `rfl` directly on a conjunction and failed. The repaired theorem proves the two equalities separately and kernel-checks with no axioms from the theorem itself. This repair history is part of the authority trail.

### Residue decoding

The same Lean file checks the exact implications

- `p = 1 mod 3`, `3 mod 5`, or `5 mod 7` kills shift `+2`;
- `p = 7 mod 11` or `9 mod 13` kills shift `+4`;
- `p = 5 mod 11` or `7 mod 13` kills shift `+6`.

These are decoding facts only. Any statistical enrichment of those residues is a separate finite or analytic statement.

## 6. Quantitative-architecture scale check

The kernel instance

\[
3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot23
=111,546,435\le10^9,
\]

while multiplying additionally by

\[
29\cdot31\cdot37\cdot41\cdot43\cdot47
\]

exceeds `10^9`.

This is why the quantitative exceptional-set architecture reaches only tiny shift budgets at human/computational scales even if its asymptotics are valid. It is a theorem about the architecture's scale, not a refutation of the asymptotic theorem.

## 7. Smooth-covering size trap

The kernel theorem

\[
3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot19\cdot23\cdot29\cdot31\cdot37\cdot41
>
2\cdot41^4+1
\]

kills the specific `H=41` smooth-`p-1` covering architecture: forcing `p` into the required simultaneous congruence class already makes `p` too large for the intended fourth-root window to reach the full covering range.

Again, this is a route theorem, not a parent negative result.

## 8. What the parent close must now overcome

The campaign's strongest exact lessons can be combined as follows. If a sufficiently large prime `p` were residual-bad, then across a fourth-root-sized odd shift window:

- every composite candidate must acquire a least prime factor at most the shift square;
- divisors of `k-1` are unavailable as such factors;
- primes larger than the window can cover at most one shift;
- the available small factors therefore form a highly constrained residue-class covering system;
- shifts that escape that covering must be prime, because an escaping composite would be a witness.

This is the deterministic object the full close mission should attack. Density-zero results are valuable child theorems, but they are not terminal because the parent quantifier is `every sufficiently large prime`.

## Authority

- `erdos681-residual-equivalence.lean`: kernel-checked reduction bundle, including the parent/residual equivalence, fourth-root necessity, parity, divisor exemption, fixed-window lemma, least-prime-factor bridge, and one-shift collision lemma.
- `erdos681-local-sieve-kernel.lean`: kernel-checked finite residue arithmetic and size traps.
- `erdos681-prime-residual-kbk-2026-09-14.md`: finite atlas, witness factor geometry, and analytic KBK frontier.

The parent remains exactly the original parent. Nothing in this note substitutes an almost-all theorem, finite computation, conditional result, or weaker exponent for closure.
