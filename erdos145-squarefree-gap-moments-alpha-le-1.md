# Erdős #145 — squarefree-gap moments for 0 <= alpha <= 1

**Author:** Jared Wilder  
**Public routing:** 2026-09-11  
**Source:** Pass-3 promoted theorem; citation-dependent on classical finite squarefree-pattern densities

Let

\[
s_1<s_2<s_3<\cdots
\]

be the squarefree positive integers and put

\[
g_j=s_{j+1}-s_j.
\]

For `0<=alpha<=1`, consider

\[
M_\alpha(x)=\frac1x\sum_{s_j\le x} g_j^\alpha.
\]

## Theorem

For every fixed

\[
0\le\alpha\le1,
\]

the limit

\[
\boxed{\lim_{x\to\infty}M_\alpha(x)}
\]

exists and is finite.

At the endpoints,

\[
\boxed{M_0(x)\to 6/\pi^2}
\]

and

\[
\boxed{M_1(x)\to1}.
\]

## Classical input

For each fixed `h>=1`, the event

> `n` and `n+h` are squarefree and no integer strictly between them is squarefree

has a natural density `rho_h`.

This is a standard consequence of finite squarefree-pattern correlation theory (Mirsky-type squarefree correlations, together with finite inclusion-exclusion/truncation for the intervening non-squarefree conditions). The release is therefore marked **citation-dependent**, not presented as a first-principles reproof of that classical input.

## Proof for 0 <= alpha < 1

Fix `G`. Restrict first to gaps `g_j<=G`. By the fixed-gap densities,

\[
\frac1x\sum_{\substack{s_j\le x\\g_j\le G}}g_j^\alpha
\longrightarrow
\sum_{h\le G}h^\alpha\rho_h.
\]

For the tail, if `g>G` and `alpha<1`, then

\[
g^\alpha\le G^{\alpha-1}g.
\]

Hence

\[
\frac1x\sum_{\substack{s_j\le x\\g_j>G}}g_j^\alpha
\le
G^{\alpha-1}\frac1x\sum_{s_j\le x}g_j.
\]

The sum of consecutive gaps telescopes. Since squarefree integers have positive asymptotic density, the first squarefree integer after `x` is `(1+o(1))x`; therefore

\[
\frac1x\sum_{s_j\le x}g_j=1+o(1).
\]

Thus the limsup tail is at most `G^{alpha-1}`, which tends to zero as `G->infinity`. The truncated limits therefore converge to a finite limit, proving existence.

For `alpha=0`, `M_0(x)` is the squarefree counting function divided by `x`, up to one harmless endpoint term, and the classical density of squarefree integers is `6/pi^2`.

## The alpha=1 endpoint

Here the sum telescopes directly:

\[
\sum_{s_j\le x}g_j=s_{N(x)+1}-s_1=x+o(x),
\]

where `N(x)` is the number of squarefree integers at most `x`. Hence

\[
M_1(x)\to1.
\]

## Scope

This closes the moment-existence question only on the range `0<=alpha<=1`. The regime `alpha>1` is not resolved by the tail estimate above and remains separate.
