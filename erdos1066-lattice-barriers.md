# Erdős #1066 — unit-distance / lattice barrier package

**Author:** Jared Wilder  
**Campaign date:** 2026-07-25  
**Human theorem-bank promotion:** 2026-09-11

Erdős #1066 asks for the asymptotic guaranteed independent-set fraction in unit-distance graphs induced by `n` planar points whose pairwise distances are at least one.

This note surfaces the proved barrier mathematics without conflating it with the still-open main problem.

## Proved formal barriers

The FormalConjectures-style Lean development in `jaredwilder/lean-contributions/erdos1066-first-formalization/` proves, among other supporting lemmas:

1. **Three-colouring barrier.** A proper 3-colouring of a finite admissible configuration gives

   `|P| <= 3 alpha(P)`.

   Thus any construction that remains 3-colourable cannot push the independent-set ratio below one third.

2. **Triangular-lattice arithmetic core.** For integers `x,y`,

   `x^2 + xy + y^2 = 1`

   implies `3 ∤ (x-y)`.

3. **Triangular-lattice geometric colouring.** Unit-distance neighbors in the triangular lattice receive different colors under `(a-b) mod 3`.

4. **Unit equilateral triangle circumradius.** The squared circumradius is exactly `1/3<1`.

5. **Definition-faithfulness theorem.** The formal `sInf` definition of `g(n)` really represents the largest independent-set size guaranteed across admissible `n`-point configurations.

The proved declarations were individually probed with `#print axioms`; the recorded footprint is the standard Mathlib base `{propext, Classical.choice, Quot.sound}` with no project-local axiom or `sorryAx` dependency in those proved theorems.

## Explicitly unfinished statements

The same Lean file deliberately leaves `sorry` on the open problem, published external bounds, and several not-yet-finished geometric bookkeeping steps. Those are not silently promoted here.

In particular, the source distinguishes the proved arithmetic/geometric cores from unfinished full-form statements such as lattice covering-radius bookkeeping.

## Additional exact computations

The research packet also records exact computational geometry checks for further lattice barriers and a normalization-specific falsification of importing the Moser spindle as a competing configuration. Those checks are evidence separate from the Lean theorem list.

## Repository status

The combination of a ~20KB problem formalization, a substantial clean proved theorem layer, explicit unfinished obligations, and a separate barrier packet makes #1066 larger than a one-lemma note. It should graduate to a dedicated problem repository when one is initialized.

Until then:

- ordinary mathematical reading: this file;
- first formalization and full proof-status table: `jaredwilder/lean-contributions/erdos1066-first-formalization/`;
- recovered barrier/provenance note: `jaredwilder/unpublished-math-papers/erdos1066-lattice-barriers/`.

No historical priority claim is made by this routing note.
