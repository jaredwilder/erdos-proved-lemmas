# Erdős #727 — an infinite exact obstruction family for k = 2

**Author:** Jared Wilder  
**Public release:** 2026-09-14

## Theorem

For every prime `p >= 7`, set

\[
k=2,\qquad n=2p-2.
\]

Then

\[
\boxed{(n+2)!^2 \nmid (2n)!}.
\]

Equivalently, the fixed-`k=2` divisibility problem has the infinite explicit non-witness family

\[
\boxed{n=2p-2\quad(p\ge7\text{ prime}).}
\]

## Proof

Since `n+2=2p`, Legendre's formula gives

\[
v_p((n+2)!)=v_p((2p)!)=2,
\]

because the multiples of `p` up to `2p` are exactly `p` and `2p`, and `p^2>2p` for `p>=3`.

Therefore

\[
v_p((n+2)!^2)=4.
\]

On the other hand,

\[
2n=4p-4.
\]

For `p>=7`,

\[
p^2>4p-4,
\]

since `p^2-(4p-4)=(p-2)^2>0`. Thus there is no contribution from `p^2`, and the multiples of `p` not exceeding `4p-4` are exactly

\[
p,\ 2p,\ 3p.
\]

Hence

\[
v_p((2n)!)=3.
\]

Therefore

\[
v_p((2n)!)=3<4=v_p((n+2)!^2),
\]

so `(n+2)!^2` cannot divide `(2n)!`.

## Scope and correction history

This is an infinite obstruction family for the slice `k=2`. It does not by itself decide the full Erdős #727 question.

A historical campaign route briefly overclaimed a much stronger eventual-failure statement using prime-gap input. That route was not retained. The theorem above is independent of that failed route and uses only exact `p`-adic valuations.

No historical novelty claim is made.