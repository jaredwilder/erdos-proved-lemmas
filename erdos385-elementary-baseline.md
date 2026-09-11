# Erdős #385 — elementary universal baseline

Author: Jared Wilder  
Public release: 2026-09-11

Define

`F(n)=max_{m<n, m composite} (m+p(m))`,

where `p(m)` is the least prime divisor of `m`.

## Theorem

For every `n>=5`,

`F(n)>=n`.

For every odd `n>=5`,

`F(n)>=n+1`.

## Proof

If `n` is odd and at least 5, take `m=n-1`. Then `m` is even and at least 4, hence composite with least prime factor 2. Therefore

`F(n) >= (n-1)+2 = n+1`.

If `n` is even and at least 6, take `m=n-2`. Again `m` is even and at least 4, hence composite with least prime factor 2. Therefore

`F(n) >= (n-2)+2 = n`.

These two cases prove the result.

## Scope

This baseline does not prove the canonical eventual strict inequality on all `n`, nor the divergence of `F(n)-n`. It isolates the residual difficulty to even inputs and shows that every odd input already has a one-unit surplus.

A historical route in the mine tried to upgrade this with a largest-prime argument to close the full problem; that upgrade was separately rejected in the Semantic Court. The elementary baseline above survives independently.

## License

Apache-2.0.
