# Erdős #385 — universal baseline and exact strict-failure census through 6,000,000

Author: Jared Wilder  
Public release: 2026-09-11

Define

`F(n)=max_{m<n, m composite} (m+p(m))`,

where `p(m)` is the least prime divisor of `m`.

## Theorem 1 — universal baseline

For every `n>=5`,

`F(n)>=n`.

For every odd `n>=5`,

`F(n)>=n+1`.

### Proof

If `n` is odd and at least 5, take `m=n-1`. Then `m` is even and at least 4, hence composite with least prime factor 2. Therefore

`F(n) >= (n-1)+2 = n+1`.

If `n` is even and at least 6, take `m=n-2`. Again `m` is even and at least 4, hence composite with least prime factor 2. Therefore

`F(n) >= (n-2)+2 = n`.

These two cases prove the result.

## Exact finite census — equality failures of the strict inequality

The release-day archive seam recovered a much larger exact computation than the original compact file exposed.

For

`5 <= n <= 6,000,000`,

the strict inequality `F(n)>n` fails at exactly **100** values. Equivalently, there are exactly 100 values in that range with

`F(n)=n`.

The largest such value is

`267680`.

The recovered audit also records that every member of this finite failure set has `n-1` prime. The earlier visible certificate had captured only a small initial portion of this phenomenon; the six-million scan materially changes the finite picture.

This is a bounded exhaustive result. It does not by itself prove that there are only finitely many equality cases, nor the stronger asymptotic/divergence form of the parent problem.

The original large-scan implementation and full 100-value list should be routed into the canonical subject packet as a reproducibility asset; until then, this section records the recovered exact census rather than letting it remain only inside the archive-forensics repository.

## Structural interpretation

The elementary theorem above shows that strict failure can occur only at even `n`. The recovered census further concentrates every observed failure through six million on the arithmetic condition `n-1` prime. That makes the prime-predecessor slice the natural finite obstruction class to study rather than treating all even integers equally.

## Scope

The universal lower bounds are proved above. The 100-value statement is an exact finite computational census recovered in the release-day archive audit. Neither statement closes the canonical eventual strict inequality or the divergence of `F(n)-n`.

A historical route tried to upgrade the baseline with a largest-prime argument to close the full problem; that upgrade was separately rejected in the Semantic Court. The results retained here survive independently.

## License

Apache-2.0.
