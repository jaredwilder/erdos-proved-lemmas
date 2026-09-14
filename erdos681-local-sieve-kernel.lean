import Mathlib

set_option autoImplicit false

/-- Small-modulus residue implications used in the #681 shift sieve. -/
theorem msl_erdos681_motif_k3_killers (p : Nat) :
    (p % 3 = 1 → (p + 2) % 3 = 0) ∧
    (p % 5 = 3 → (p + 2) % 5 = 0) ∧
    (p % 7 = 5 → (p + 2) % 7 = 0) ∧
    (p % 11 = 5 → (p + 6) % 11 = 0) ∧
    (p % 11 = 7 → (p + 4) % 11 = 0) ∧
    (p % 13 = 7 → (p + 6) % 13 = 0) ∧
    (p % 13 = 9 → (p + 4) % 13 = 0) := by
  omega

/-- Exact finite local density: among the 48 reduced classes modulo 105, 33 have a+2 sharing a factor with 105. -/
theorem msl_erdos681_delta3_exact_r2 :
    ((List.range 105).filter (fun a => Nat.gcd a 105 == 1 && Nat.gcd (a + 2) 105 != 1)).length = 33 ∧
    ((List.range 105).filter (fun a => Nat.gcd a 105 == 1)).length = 48 :=
  ⟨by rfl, by rfl⟩

/-- Concrete scale check for the quantitative exceptional-set architecture. -/
theorem msl_erdos681_N67_T1_modulus_instance :
    3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 = 111546435 ∧
    111546435 ≤ 1000000000 ∧
    111546435 * 29 * 31 * 37 * 41 * 43 * 47 > 1000000000 := by
  decide

/-- Concrete size trap killing the H=41 smooth-p-1 covering architecture. -/
theorem msl_erdos681_N49_size_trap_H41 :
    3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37 * 41 > 2 * 41 ^ 4 + 1 := by
  decide
