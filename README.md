# Erdős proved lemmas

**A compact catalog of finished mathematical lemmas, exact subcases, and structural reductions extracted from larger Erdős research projects.**

Author: Jared Wilder. First public timestamp: 2026-09-11.

This repository is the preferred home for a finished child theorem **until** the mathematics grows into a richer subject repository. When that happens, this bank keeps a concise statement and points to the fuller home rather than competing with it.

The status of a larger Erdős problem does not determine the status of a theorem proved inside its investigation. Entries are organized by the statement actually established.

## Reviewed-estate accounting

The table below is a **reader-facing selection**, not the exhaustive release ledger. For the reviewed 56-row canonical-gold tranche, see [`CANONICAL-GOLD-56-DISPOSITION.md`](CANONICAL-GOLD-56-DISPOSITION.md): all 56 reviewed rows have a terminal public disposition, with **47 routed / routed-corrected and 9 subsumed**.

That accounting closes only the reviewed 56-row tranche. It does **not** declare the larger ore estate saturated; the remaining latest-local `PROVED` states, contradiction histories, formalizer obligations and raw theorem-bearing archives are separate mining surfaces.

## Results

| problem | result | evidence / fuller home |
|---|---|---|
| **#51** | if `phi(n)=a` and `R(a)=max{r:r!<=a}`, then every preimage satisfies `n<=a 2^R(a)` | Euler product + factorial bound on distinct prime factors |
| **#52** | for `A_N={2^i3^j:0<=i,j<N}`, `|A_N+A_N| >= C(N,2)^2` and `|A_NA_N|=(2N-1)^2` | exact `v_2/v_3` decoding; fuller home: `additive-combinatorics-campaigns` |
| **#85** | `f(5)=f(6)=f(7)=3` for the minimum-degree/C4 function | elementary proof + exhaustive graph check |
| **#126** | no three distinct positive integers have all pairwise sums powers of 2 | elementary proof + exhaustive check; positivity is load-bearing |
| **#155** | `F(N+1)<=F(N)+1` for every `N` in the Sidon extremal function | exact deletion argument; this is only the `k=1` canonical slice |
| **#170** | sparse-ruler exact table through `N=20`, parity obstruction, corrected constant, and `F(10)=6` | exhaustive enumeration + analytic correction; see `erdos170-sparse-ruler-results.md` |
| **#276** | common divisors of a Fibonacci-type recurrence are exactly the common divisors of the two seeds | direct induction; seed-gcd reduction |
| **#289** | all-prime p-adic obstruction for finite integral reciprocal sums | elementary p-adic proof; finite head/tail lemma separately formalized |
| **#291** | corrected leading-`p` harmonic divisibility criterion using `q=floor(n/p^e)` | analytic proof + finite regression |
| **#295** | exact small slice `k(3)=5` for reciprocal representations of 1 | explicit five-denominator witness + four-term reciprocal upper bound |
| **#313** | for fixed `k`, only finitely many reciprocal-prime solutions exist | elementary finite-branching proof |
| **#359** | every reciprocal prefix of the true `n=1` greedy sequence has sum at least 1 | direct representation-capacity count |
| **#373** | no factorial-product solution when `n-1` is prime | elementary divisibility proof |
| **#385** | `F(n)>=n` for all `n>=5`, and `F(n)>=n+1` for odd `n>=5` | explicit even-composite predecessor witnesses |
| **#390** | every admissible factorization has largest factor at least `2p_*(n)` when `p_*(n)>n/2` | unique large-prime carrier argument |
| **#394** | for every prime `p>k`, `t_k(p)=p-k+1` | exact length-`k` interval argument |
| **#396** | construction simultaneously eliminating all small primes in the stated binomial-divisibility setting | valuation/carry argument |
| **#400** | `g_k(n)<=k(floor(log_2 n)+1)` and `g_k(m!)>=m+k-3` | Legendre binary digit sums + explicit factorial tuple; logarithmic upper order is classical |
| **#413** | the predecessor condition reduces exactly to an `O(log n)` terminal window | `omega(r)<=log_2 r` |
| **#456** | for every odd prime `p`, `m_(p-1)=p_(p-1)=p`; `p=2` is an endpoint exception | totient bound + residue-class minimum |
| **#477** | no integer quadratic image admits a unique additive complement in Z | [complete written reflection proof](erdos477-all-quadratics.md); square-case Lean layer linked separately |
| **#486** | summable forbidden residue mass implies ordinary natural density under the frozen activation rule | periodic truncation + tail bound + Kronecker lemma |
| **#489** | finite forbidden-divisor sets have an exact cyclic squared-gap mean | periodicity modulo `lcm(A)` + period averaging |
| **#495** | Littlewood's conclusion holds for every diagonal pair `(alpha,alpha)` and whenever either coordinate is rational | Dirichlet/continued-fraction approximation |
| **#579** | in a `K_{2,2,2}`-free graph, the common neighborhood of any two vertices is `K_{2,2}`-free | direct six-vertex obstruction; strengthens recovered nonadjacent-pair statement |
| **#602** | every countable family of infinite sets has a 2-colouring making every member bichromatic | fresh-point recursion; intersection hypotheses unnecessary in countable stratum |
| **#602 finite analogue** | finite hypergraphs with edge size at least 2 and no one-point edge intersections are 2-colourable | minimal-counterexample + single-flip proof; corrected hypothesis independently rechecked |
| **#677** | complete `k=2` slice: `M(n,2)=(n+1)(n+2)` is strictly increasing | consecutive coprimality; exact base case |
| **#681** | `k=1` works iff `n+1` is composite; every witness satisfies `k^4<n+k` | least-prime-factor bound `p(m)<=sqrt(m)` |
| **#700** | for semiprime `n=pq`, `f(pq)=p` for the binomial-gcd function | divisibility identity + Lucas theorem |
| **#701** | every finite hereditary family of rank at most 2 has maximum intersecting subfamily equal to a largest star | complete graph-structural proof; fuller home: `combinatorial-records` |
| **#774** | dissociated subsets of a dyadic block have logarithmic size | subset-sum counting |
| **#826** | for `k>sqrt(n)`, `tau(n+k)<3k`, reducing the remaining range to `k<=sqrt(n)` | divisor pairing `tau(m)<=2sqrt(m)` |
| **#890 ↔ #1093** | large-prime binomial identity, deficiency/excess accounting, and admissible LCM divisor-window reduction | exact identities + finite deficiency engine through `k<=45`; standalone-repo candidate |
| **#893** | `tau(2^k-1) >= tau(k)` and a doubling consequence | divisor injection; independently checked |
| **#930** | infinitely many length-2 square-product interval pairs; any `r=2` threshold must satisfy `k>=4` | Pell equation + explicit length-3 square witness |
| **#978** | `4 ∤ n^4+2` for every integer `n` | congruence proof; independently checked |
| **#1073** | if `u>1` divides `n!+1`, every prime factor of `u` exceeds `n`; composite `u>n^2` | elementary modular contradiction |
| **#1107** | 87 is not a sum of at most three squarefull numbers | exhaustive finite basis search |
| **#1142** | strong congruence compression for Good numbers, including exactly 288 residue classes modulo 111,546,435 beyond the stated threshold | arithmetic reduction + exhaustive check |
| **#1210** | any explicit uniform additive constant in the canonical inequality must satisfy `C>=1` | endpoint `n=2`, `A={1}`; constraint only, not existence proof |

## Full writeups for routed results

- [`CANONICAL-GOLD-56-DISPOSITION.md`](CANONICAL-GOLD-56-DISPOSITION.md) — terminal public disposition of the reviewed 56-row tranche
- [`erdos51-totient-preimage-size.md`](erdos51-totient-preimage-size.md)
- [`erdos52-multiplicative-box-sumset.md`](erdos52-multiplicative-box-sumset.md)
- [`erdos85-small-values.md`](erdos85-small-values.md)
- [`erdos155-k1-sidon-monotonicity.md`](erdos155-k1-sidon-monotonicity.md)
- [`erdos170-exact-f10.md`](erdos170-exact-f10.md)
- [`erdos170-sparse-ruler-results.md`](erdos170-sparse-ruler-results.md)
- [`erdos276-common-divisors.md`](erdos276-common-divisors.md)
- [`erdos289-padic-reciprocal-obstructions.md`](erdos289-padic-reciprocal-obstructions.md)
- [`erdos291-leading-p-harmonic-criterion.md`](erdos291-leading-p-harmonic-criterion.md)
- [`erdos295-exact-k3.md`](erdos295-exact-k3.md)
- [`erdos313-fixed-k-finiteness.md`](erdos313-fixed-k-finiteness.md)
- [`erdos359-reciprocal-prefix-invariant.md`](erdos359-reciprocal-prefix-invariant.md)
- [`erdos385-elementary-baseline.md`](erdos385-elementary-baseline.md)
- [`erdos390-largest-prime-carrier.md`](erdos390-largest-prime-carrier.md)
- [`erdos394-prime-window.md`](erdos394-prime-window.md)
- [`erdos400-elementary-log-bound.md`](erdos400-elementary-log-bound.md)
- [`erdos413-logarithmic-window.md`](erdos413-logarithmic-window.md)
- [`erdos456-odd-prime-anchor.md`](erdos456-odd-prime-anchor.md)
- [`erdos477-all-quadratics.md`](erdos477-all-quadratics.md)
- [`erdos486-summable-forbidden-mass.md`](erdos486-summable-forbidden-mass.md)
- [`erdos489-finite-periodic-gap-square.md`](erdos489-finite-periodic-gap-square.md)
- [`erdos495-diagonal-littlewood.md`](erdos495-diagonal-littlewood.md)
- [`erdos579-common-neighborhood.md`](erdos579-common-neighborhood.md)
- [`erdos602-countable-family-colouring.md`](erdos602-countable-family-colouring.md)
- [`erdos677-k2-lcm-slice.md`](erdos677-k2-lcm-slice.md)
- [`erdos681-fourth-root-window.md`](erdos681-fourth-root-window.md)
- [`erdos700-semiprime-binomial-gcd.md`](erdos700-semiprime-binomial-gcd.md)
- [`erdos701-rank2-hereditary-star.md`](erdos701-rank2-hereditary-star.md)
- [`erdos826-tail-elimination.md`](erdos826-tail-elimination.md)
- [`erdos890-1093-bridge.md`](erdos890-1093-bridge.md)
- [`erdos930-perfect-power-intervals.md`](erdos930-perfect-power-intervals.md)
- [`erdos1073-factorial-plus-one-barrier.md`](erdos1073-factorial-plus-one-barrier.md)
- [`erdos1210-additive-constant-endpoint.md`](erdos1210-additive-constant-endpoint.md)

Original extraction copies may remain in `unpublished-math-papers` as provenance. A richer subject repository, when one exists, is the preferred reading and citation surface.

## Selected older proofs

### Erdős 126

Suppose `a+b=2^p`, `a+c=2^q`, `b+c=2^r` with `p<q<r`. Then

`2a = 2^p+2^q-2^r < 0`,

contradicting positivity. Hence no three distinct positive integers have all pairwise sums powers of two.

### Erdős 893

If `a|k`, then `2^a-1 | 2^k-1`. The injective map `a -> 2^a-1` therefore sends divisors of `k` to divisors of `2^k-1`, proving

`tau(2^k-1) >= tau(k)`.

The same factorization gives `tau(2^{2k}-1) >= 2tau(2^k-1)`.

### Erdős 978

Modulo 16, `n^4` is 0 or 1, so `n^4+2` is 2 or 3 modulo 16. In particular it is never divisible by 4 and hence cannot be a fourth power or any `4r`-th power.

### Erdős 602 — corrected finite analogue

Let `H` be a finite hypergraph in which every edge has at least two vertices and no two distinct edges meet in exactly one vertex. Then `H` is 2-colourable.

Choose a counterexample with the minimum number of edges. Remove one edge `e` and colour the rest. If `e` is monochromatic, flip one vertex `v∈e`. Any other edge made monochromatic by that flip would have intersected `e` only in `v`, contradicting the hypothesis.

The edge-size condition is necessary: the one-edge hypergraph `{{v}}` is a counterexample without it. The earlier stronger sentence is therefore corrected locally rather than turned into a disclaimer for the rest of the repository.

## Verification and literature status

Some entries have independent finite checks, some have formal fragments, and some are ordinary proofs. Each writeup states its own evidence.

Historical novelty is a separate literature question. Corrections attach to the result they correct.

## License

Apache-2.0.
