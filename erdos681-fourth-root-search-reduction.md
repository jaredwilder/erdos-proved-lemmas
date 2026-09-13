# Erdős #681 — exact `k=1` classification and fourth-root search window

**Author:** Jared Wilder  
**Status:** elementary reduction / exact subproblem  
**Parent problem:** open

Erdős #681 asks whether, for every sufficiently large integer `n`, there exists an integer `k` such that `n+k` is composite and

\[
p(n+k)>k^2,
\]

where `p(m)` denotes the least prime factor of the composite integer `m`.

The recovered estate contains a clean exact reduction that sharply separates the easy inputs from the genuinely difficult shifted-prime inputs.

## Theorem 1 — `k=1` works exactly when `n+1` is composite

For every `n>=2`, the choice `k=1` is a valid witness if and only if `n+1` is composite.

### Proof

For `k=1`, the required conditions are precisely

\[
n+1\text{ composite},\qquad p(n+1)>1.
\]

Every composite positive integer has least prime factor at least `2`, so whenever `n+1` is composite the inequality is automatic. Conversely, if `n+1` is prime, the required compositeness condition fails. ∎

Thus the only inputs not disposed of immediately by `k=1` are

\[
\boxed{n=p-1\quad\text{with }p\text{ prime}.}
\]

## Theorem 2 — every witness lies in a fourth-root window

Suppose `k` is any valid witness for `n`, and put

\[
m=n+k.
\]

Since `m` is composite, its least prime factor satisfies

\[
p(m)^2\le m.
\]

But the witness inequality gives

\[
p(m)>k^2.
\]

Therefore

\[
\boxed{k^4<n+k.}
\]

In particular, for `k>=2` we have `k<=n` (otherwise `k^4` is already much larger than `n+k`), hence

\[
n+k\le2n
\]

and so

\[
\boxed{k<(2n)^{1/4}.}
\]

Thus each fixed `n` has only a finite fourth-root-sized search window for possible witnesses.

## Parity pruning on the shifted-prime inputs

If `n` is even and `k>=2` is even, then `n+k` is even. When it is composite its least prime factor is `2`, so

\[
p(n+k)=2\le k^2.
\]

Hence no even `k>=2` can witness the inequality for an even `n`.

For the hard family `n=p-1` with odd prime `p`, `n` is even. Therefore any nontrivial witness must be **odd** and satisfy

\[
3\le k<(2n)^{1/4}.
\]

## What this accomplishes

The canonical question is not solved here. The reduction proves that:

1. every `n` with composite `n+1` is solved immediately by `k=1`;
2. only shifted primes `n=p-1` remain difficult;
3. every possible witness lies in an explicit fourth-root window;
4. on the shifted-prime family, even `k` are impossible.

This converts the parent question into a much narrower rough-number problem in short shifted-prime windows without pretending that the remaining existence theorem has been proved.

## Provenance

Recovered independently in multiple estate layers: theorem-union, Pass-3 fusion, Pass-6 synthesis, and kernel-shot records. The arithmetic proof above is self-contained and does not rely on the finite verifiers that accompanied those records.
