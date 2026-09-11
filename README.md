# erdos-proved-lemmas

**Proved lemmas sitting inside open Erdős problems — the parts that are finished, separated from
the parts that are not.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

A campaign on an open problem produces a mix: some steps get proved, most do not, and the whole
thing gets filed under "still open" where nobody looks again. These are the steps that got proved.

**No problem here is closed.** Every entry says what it establishes and stops.

Four of them were **re-verified independently on 2026-09-11** before publication and are marked
**[checked]**. The rest are reported with their arguments as recorded.

---

## Erdős 978 — `4 ∤ n⁴ + 2` for every integer n **[checked]**

Mod 16: `n⁴ ≡ 0` for even n and `n⁴ ≡ 1` for odd n, so `n⁴ + 2 ≡ 2` or `3 (mod 16)`. Neither is
divisible by 4.

**Consequence: `n⁴ + 2` is never a fourth power, nor any `4k`-th power, for any integer n.**

Verified over n ∈ [−500, 500]: no n with `4 | n⁴+2`.

## Erdős 126 — no three distinct positive integers have all pairwise sums powers of 2 **[checked]**

Suppose `a+b = 2^p`, `a+c = 2^q`, `b+c = 2^r` with `p < q < r`. Then

```
2a = 2^p + 2^q − 2^r  ≤  3·2^(q−1) − 2^(q+1)  <  0
```

so no such `a` exists.

Verified exhaustively over all triples `a < b < c < 600`: none.

## Erdős 1107 — 87 is not a sum of at most three squarefull numbers **[checked]**

The complete squarefull basis below 88 is

```
1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 72, 81
```

Exhaustive search over all sums of at most three of these (repeats allowed) finds no representation
of 87. At `r = 2` the conjecture asks for sums of at most `r+1 = 3`, so **87 is a genuine
exception**, extending the known gap set to `{7, 15, 23, 87}`.

## Erdős 893 — `τ(2^k − 1) ≥ τ(k)` for every k ≥ 1 **[checked]**

If `a | k` then `2^a − 1 | 2^k − 1`, by the geometric-sum identity
`2^k − 1 = (2^a − 1)·Σ_{i<m} 2^{ia}`. The map `a ↦ 2^a − 1` is injective, so it embeds the divisors
of `k` into the divisors of `2^k − 1`.

Verified for all k < 60: no counterexample.

A companion, same mechanism: `τ(2^{2k} − 1) ≥ 2·τ(2^k − 1)`, since
`2^{2k} − 1 = (2^k − 1)(2^k + 1)` with the two factors coprime (both odd) and `τ(2^k + 1) ≥ 2`.

---

## Erdős 396 — a construction disposing of all small primes at once

Let `M(k) = Π_{p ≤ 2k+1} p^{E_p}` with `E_p = ⌊log_p((k+1)!)⌋ + 1`, and impose `n ≡ −1 (mod M(k))`.

For each `p ≤ 2k+1` and `i ≤ k`, `n − i ≡ −(i+1) (mod p^{E_p})`, so
`v_p(Π(n−i)) = v_p((k+1)!) ≤ E_p − 1`. Meanwhile `n`'s low base-`p` digits are all `p−1`, so `n + n`
carries at every position below `E_p`, giving `v_p(C(2n,n)) ≥ E_p > v_p((k+1)!)`.

The supporting valuation lemma, for `q ∤ n` and `n ≡ i (mod q)` with `0 < i < q`:
`v_q(C(2n,n)) = ⌊2i/q⌋ + v_q(C(2s,s))` where `n = qs + i`.

## Erdős 373 — no solutions when n−1 is prime

If `p = n−1` is prime and `n ≥ 3`, then `n! = a₁!···a_k!` with `n−1 > a₁ ≥ ··· ≥ a_k ≥ 2` has no
solutions: every `aᵢ ≤ n−2 = p−1 < p`, so `p ∤ aᵢ!` for all i, hence `p` does not divide the product
— but `p | n!`.

The exhaustive companion over `2 ≤ n ≤ 36` finds exactly three solutions, all with `n−1` composite:
`9! = 7!·3!·3!·2!`, `10! = 7!·6!`, `16! = 14!·5!·2!`. These are the three known in the literature.

## Erdős 602 — every finite hypergraph with no 1-point edge intersections is 2-colourable

Let `H` be a minimal non-2-colourable finite hypergraph with all edge sizes ≥ 2 and no two distinct
edges meeting in exactly one vertex.

**H is Sperner.** If `f ⊊ e` with both in `H`, minimality gives a 2-colouring `c` of `H − e`. Then
`e` must be monochromatic under `c` (else `c` colours `H`), so `f ⊆ e` is monochromatic too — but
`f ∈ H − e`, contradiction.

The single-flip construction then completes it, and the only obstruction is an edge pair meeting in
exactly one vertex, which the hypothesis forbids. **The edge-size ≥ 2 condition is not even needed.**

## Erdős 774 — dissociated subsets of a dyadic block are logarithmically small

All `2^|D|` subset sums of a dissociated `D` are distinct, and each is at most `Σ_{d∈D} d ≤ |D|·2N`.
Distinct integers in an interval of that length force `2^|D| ≤ 2N|D| + 1`, hence

```
|D| ≤ log₂ N + O(log log N)
```

So a set with a dissociated subset of proportional size is extremely sparse inside a dyadic block.

## Erdős 1142 — a search reduction for "Good" numbers

`n` is Good if `n − 2^k` is prime for every `1 ≤ 2^k < n`. Forced-divisibility over primes where 2 is
a primitive root gives a congruence chain: `n > 21 ⟹ n ≡ 0, 45, 75 (mod 105)`, and
`n > 262165 ⟹ 4849845 | n` together with `n mod 23` in a 12-class set.

**Any counterexample beyond 105 must lie in one of exactly 288 residue classes mod 111,546,435.**
The record notes this refutes its own earlier count of 324.

The even case closes completely: `n` even forces `n = 2^k + 2`, and two exponents force `2^k`
composite, so **Good ∩ 2ℕ = {4}**. Exhaustively, `Good ∩ [3, 2^20] = {4, 7, 15, 21, 45, 75, 105}`.

## Erdős 289 — a p-adic generalisation of Kürschák 1918

If `S` is a finite set of integers ≥ 2 with `Σ_{n∈S} 1/n ∈ ℤ`, then for **every** prime `p`, writing
`A_p = {n/p : n ∈ S, p | n}`, we have `v_p(Σ_{m∈A_p} 1/m) ≥ 1`.

Only multiples of `p` carry negative `v_p`; factor out `1/p` and induct through `A_p`. The `p = 2`
instance is Kürschák's classical theorem. Confirmed on all 21 integer-sum subsets of `[2,20]`.
**Not kernel-checked.**

---

## Scope

Every entry is a lemma inside a problem that remains open, and several are elementary. The point is
not that any of them is hard — it is that they are finished, and they were invisible inside
campaigns filed under "still open".

Four are independently re-verified here. The others are recorded as their campaigns state them; a
reader should treat those as leads carrying an argument, not as certified results. This estate has
published a [refutation of one of its own claimed proofs](https://github.com/jaredwilder/erdos-findings-ledger/blob/main/ERDOS-1210-CLAIMED-PROOF-IS-FALSE.md)
that had been ranked first out of a 110-problem range, so that caution is not rhetorical.

## License

Apache-2.0.
