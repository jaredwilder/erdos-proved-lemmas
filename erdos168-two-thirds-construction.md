# Erdős #168 — two-thirds construction and exact `F(42)=34`

Author: Jared Wilder. Public release: 2026-09-11.

Let `F(N)` be the largest size of a subset of `[1,N]` containing no complete triple

`{n,2n,3n}`.

## Theorem 1 — uniform two-thirds construction

For every positive integer `N`, let

`A_N={1<=m<=N : 3∤m}`.

Then `A_N` contains no complete triple `{n,2n,3n}`, and

`|A_N| = N-floor(N/3) = ceil(2N/3)`.

Therefore

`F(N) >= ceil(2N/3)`.

### Proof

Every triple `{n,2n,3n}` contains `3n`, which is divisible by 3, while `A_N` contains no multiple of 3. The cardinality follows by deleting the `floor(N/3)` multiples of 3 from `[N]`.

## Theorem 2 — exact finite value `F(42)=34`

The release-day archive audit recovered two incompatible historical claims: one campaign record called `F(42)=30` exact, while a later audit exhibited a 34-element avoiding set.

The conflict is now settled by exact branch-and-bound:

`F(10)=8`, `F(20)=16`, `F(30)=24`, and

`F(42)=34`.

Equivalently, the minimum hitting set for the triples `{k,2k,3k}` contained in `[1,42]` has size exactly `8`.

The committed verifier `verify_erdos168_f42.py` performs an exhaustive minimum-hitting-set branch-and-bound and independently cross-checks the algorithm against brute-force subset enumeration at small `N`.

## Correction record

The historical `F(42)=30` claim is false. Any downstream statement whose proof used that value as an exact extremum must be re-evaluated. In particular, the archived claim that `F(42)=30` itself refuted a proposed `3/7` residue-periodic density law does not follow from that computation.

The exact `F(42)=34` result is finite. It does not supply a general formula or asymptotic value for `F(N)`.
