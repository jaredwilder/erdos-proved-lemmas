# Erdős #727 — infinite `k=2` factorial-divisibility obstruction family

Author: Jared Wilder. Public release: 2026-09-11.

## Theorem

For every prime `p>=7`, put

`n=2p-2`.

Then

`((n+2)!)^2 ∤ (2n)!`.

Equivalently, the `k=2` divisibility demanded in the parent problem fails for infinitely many `n`.

## Proof

Here

`n+2=2p`,

so

`v_p((n+2)!)=v_p((2p)!)=2`.

Therefore the left-hand side has `p`-adic valuation

`v_p(((n+2)!)^2)=4`.

On the other hand,

`2n=4p-4`.

For `p>=7`, one has `p^2>4p-4`, so the multiples of `p` up to `4p-4` are exactly

`p, 2p, 3p`.

Hence

`v_p((2n)!)=3`.

Since `4>3`, the required divisibility fails.

## Scope / literature boundary

This is an exact infinite obstruction family for the `k=2` slice. The valuation observation is classical/publicly discoverable; historical novelty is not claimed. The larger parent problem remains separate.