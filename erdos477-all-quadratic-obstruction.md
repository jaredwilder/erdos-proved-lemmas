# Erdős #477 — every quadratic polynomial is obstructed

**Public estate note:** 2026-09-14  
**Historical priority:** not claimed here. The current Erdős Problems record credits the simple all-quadratic argument to AlphaProof and Sarosh Adenwalla. This estate independently rediscovered the degree-2 obstruction during its campaign.

## Theorem

Let

\[
f(x)=ax^2+bx+c\in\mathbb Z[x],\qquad a\ne0.
\]

There is no set `A subset Z` for which every integer has a unique representation

\[
n=u+f(k),\qquad u\in A,\ k\in\mathbb Z.
\]

Thus the degree-2 slice of Erdős #477 is completely obstructed.

## Proof

First, `A` cannot be finite. A quadratic polynomial is bounded on one side: if `a>0`, then `f(Z)` is bounded below, while if `a<0` it is bounded above. A finite union of translates of `f(Z)` is therefore also bounded on that side and cannot cover all of `Z`.

So suppose `A` is infinite.

### Case 1: b != 0

By pigeonhole modulo `2|b|`, two distinct elements `u,v in A` lie in the same residue class. Hence

\[
u-v=2bk
\]

for some nonzero integer `k` (after choosing the sign of `k` appropriately).

But

\[
f(k)-f(-k)=2bk.
\]

Therefore

\[
u+f(-k)=v+f(k),
\]

which gives two distinct representations of the same integer. This contradicts uniqueness.

### Case 2: b = 0

Now `f(x)=ax^2+c`. By pigeonhole modulo `4|a|`, there are distinct `u,v in A` with

\[
u-v=4ak
\]

for some nonzero integer `k`.

Since

\[
f(k+1)-f(k-1)
=a\bigl((k+1)^2-(k-1)^2\bigr)
=4ak,
\]

we obtain

\[
u+f(k-1)=v+f(k+1),
\]

again contradicting uniqueness.

Hence no quadratic integer polynomial admits such a unique direct-sum complement.

## Scope and attribution

This settles the **quadratic slice only**. Erdős #477 asks whether some polynomial of degree at least 2 admits a unique complement; higher-degree cases are separate.

The current Erdős Problems page records this quadratic obstruction as a simple proof arising from the combined efforts of AlphaProof and Sarosh Adenwalla. Accordingly, this file is an estate-completeness / independent-rediscovery note, not a novelty claim.

Reference: https://www.erdosproblems.com/477
