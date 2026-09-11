# Erdős proved lemmas

**A compact catalog of finished mathematical lemmas, exact subcases, and structural reductions extracted from larger Erdős research projects.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

This repository is the preferred home for a finished child theorem **until** the mathematics grows into a richer subject repository. When that happens, this bank keeps a concise statement and points to the fuller home rather than competing with it.

The status of a larger Erdős problem does not determine the status of a theorem proved inside its investigation. Entries are organized by the statement actually established.

## Results

| problem | result | evidence / fuller home |
|---|---|---|
| **#52** | for `A_N={2^i3^j:0<=i,j<N}`, `|A_N+A_N| >= C(N,2)^2` and `|A_NA_N|=(2N-1)^2` | exact `v_2/v_3` decoding; fuller home: `additive-combinatorics-campaigns` |
| **#85** | `f(5)=f(6)=f(7)=3` for the minimum-degree/C4 function | elementary proof + exhaustive graph check |
| **#126** | no three distinct positive integers have all pairwise sums powers of 2 | elementary proof + exhaustive check |
| **#289** | all-prime p-adic obstruction for finite integral reciprocal sums | elementary p-adic proof; finite head/tail lemma separately formalized |
| **#291** | corrected leading-`p` harmonic divisibility criterion using `q=floor(n/p^e)` | analytic proof + finite regression |
| **#313** | for fixed `k`, only finitely many reciprocal-prime solutions exist | elementary finite-branching proof |
| **#359** | every reciprocal prefix of the true `n=1` greedy sequence has sum at least 1 | direct representation-capacity count |
| **#373** | no factorial-product solution when `n-1` is prime | elementary divisibility proof |
| **#396** | construction simultaneously eliminating all small primes in the stated binomial-divisibility setting | valuation/carry argument |
| **#413** | the predecessor condition reduces exactly to an `O(log n)` terminal window | `omega(r)<=log_2 r` |
| **#486** | summable forbidden residue mass implies ordinary natural density under the frozen activation rule | periodic truncation + tail bound + Kronecker lemma |
| **#602** | finite hypergraphs with edge size at least 2 and no one-point edge intersections are 2-colourable | minimal-counterexample + single-flip proof; corrected hypothesis independently rechecked |
| **#681** | `k=1` works iff `n+1` is composite; every witness satisfies `k^4<n+k` | least-prime-factor bound `p(m)<=sqrt(m)` |
| **#700** | for semiprime `n=pq`, `f(pq)=p` for the binomial-gcd function | divisibility identity + Lucas theorem |
| **#701** | every finite hereditary family of rank at most 2 has maximum intersecting subfamily equal to a largest star | complete graph-structural proof; fuller home: `combinatorial-records` |
| **#774** | dissociated subsets of a dyadic block have logarithmic size | subset-sum counting |
| **#826** | for `k>sqrt(n)`, `τ(n+k)<3k`, reducing the remaining range to `k<=sqrt(n)` | divisor pairing `τ(m)<=2sqrt(m)` |
| **#890 ↔ #1093** | large-prime binomial identity, deficiency/excess accounting, and admissible LCM divisor-window reduction | exact identities + finite deficiency engine through `k<=45`; standalone-repo candidate |
| **#893** | `τ(2^k-1) >= τ(k)` and a doubling consequence | divisor injection; independently checked |
| **#930** | infinitely many length-2 square-product interval pairs; any `r=2` threshold must satisfy `k>=4` | Pell equation + explicit length-3 square witness |
| **#978** | `4 ∤ n^4+2` for every integer `n` | congruence proof; independently checked |
| **#1107** | 87 is not a sum of at most three squarefull numbers | exhaustive finite basis search |
| **#1142** | strong congruence compression for Good numbers, including exactly 288 residue classes modulo 111,546,435 beyond the stated threshold | arithmetic reduction + exhaustive check |

## Full writeups for routed results

- [`erdos52-multiplicative-box-sumset.md`](erdos52-multiplicative-box-sumset.md)
- [`erdos85-small-values.md`](erdos85-small-values.md)
- [`erdos289-padic-reciprocal-obstructions.md`](erdos289-padic-reciprocal-obstructions.md)
- [`erdos291-leading-p-harmonic-criterion.md`](erdos291-leading-p-harmonic-criterion.md)
- [`erdos313-fixed-k-finiteness.md`](erdos313-fixed-k-finiteness.md)
- [`erdos359-reciprocal-prefix-invariant.md`](erdos359-reciprocal-prefix-invariant.md)
- [`erdos413-logarithmic-window.md`](erdos413-logarithmic-window.md)
- [`erdos486-summable-forbidden-mass.md`](erdos486-summable-forbidden-mass.md)
- [`erdos681-fourth-root-window.md`](erdos681-fourth-root-window.md)
- [`erdos700-semiprime-binomial-gcd.md`](erdos700-semiprime-binomial-gcd.md)
- [`erdos701-rank2-hereditary-star.md`](erdos701-rank2-hereditary-star.md)
- [`erdos826-tail-elimination.md`](erdos826-tail-elimination.md)
- [`erdos890-1093-bridge.md`](erdos890-1093-bridge.md)
- [`erdos930-perfect-power-intervals.md`](erdos930-perfect-power-intervals.md)

Original extraction copies may remain in `unpublished-math-papers` as provenance. A richer subject repository, when one exists, is the preferred reading and citation surface.

## Selected older proofs

### Erdős 126

Suppose `a+b=2^p`, `a+c=2^q`, `b+c=2^r` with `p<q<r`. Then

`2a = 2^p+2^q-2^r < 0`,

contradicting positivity. Hence no three distinct positive integers have all pairwise sums powers of two.

### Erdős 893

If `a|k`, then `2^a-1 | 2^k-1`. The injective map `a -> 2^a-1` therefore sends divisors of `k` to divisors of `2^k-1`, proving

`τ(2^k-1) >= τ(k)`.

The same factorization gives `τ(2^{2k}-1) >= 2τ(2^k-1)`.

### Erdős 978

Modulo 16, `n^4` is 0 or 1, so `n^4+2` is 2 or 3 modulo 16. In particular it is never divisible by 4 and hence cannot be a fourth power or any `4r`-th power.

### Erdős 602 — corrected hypothesis

Let `H` be a finite hypergraph in which every edge has at least two vertices and no two distinct edges meet in exactly one vertex. Then `H` is 2-colourable.

Choose a counterexample with the minimum number of edges. Remove one edge `e` and colour the rest. If `e` is monochromatic, flip one vertex `v∈e`. Any other edge made monochromatic by that flip would have intersected `e` only in `v`, contradicting the hypothesis.

The edge-size condition is necessary: the one-edge hypergraph `{{v}}` is a counterexample without it. The earlier stronger sentence is therefore corrected locally rather than turned into a disclaimer for the rest of the repository.

## Verification and literature status

Some entries have independent finite checks, some have formal fragments, and some are ordinary proofs. Each writeup states its own evidence.

Historical novelty is a separate literature question. Corrections attach to the result they correct.

## License

Apache-2.0.
