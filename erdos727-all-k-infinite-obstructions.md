# Erdős #727 — an infinite obstruction family for every fixed k

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted theorem, independently rechecked

Fix an integer `k>=2`.

## Theorem

For every prime

\[
p>2k,
\]

put

\[
n=p-k.
\]

Then

\[
\boxed{((n+k)!)^2\nmid(2n)!.}
\]

Therefore every fixed `k>=2` has infinitely many values of `n` for which the divisibility in Erdős #727 fails.

## Proof

By construction

\[
n+k=p,
\]

so

\[
v_p(((n+k)!)^2)=v_p((p!)^2)=2.
\]

On the other hand, `p>2k` implies

\[
p<2(p-k)=2n<2p.
\]

Thus exactly one multiple of `p` occurs in `(2n)!`, namely `p`, and

\[
v_p((2n)!)=1.
\]

The left side requires two factors of `p` while the right side contains only one, proving the failure of divisibility.

Because there are infinitely many primes greater than `2k`, this yields infinitely many obstructions for every fixed `k`.

## Relation to the earlier k=2 packet

The previously released family `n=2p-2` gives an exact `k=2` obstruction by a different parametrization. The theorem above is the stronger fixed-`k` statement recovered in Pass 3.

## Scope

The parent problem asks whether, for fixed `k`, the divisibility nevertheless holds for infinitely many `n`. An infinite family of non-witnesses does **not** negate that possibility. This theorem is an exact obstruction family, not a negative solution of the parent problem.
