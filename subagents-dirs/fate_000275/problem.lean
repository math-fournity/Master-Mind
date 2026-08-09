/-- FATE Problem (id=26, source=FATE-X, tags=['Commutative Algebra', 'Ideal Theory', 'Integral Dependence and the Nullstellensatz'] )
    Informal statement: Let $K/\mathbb{Q}$ be a finite extension. Let $H$ be a closed subgroup of the absolute Galois group $G(K)$ of $K$. If $H$ is finite, then the cardinality of $H$ is either one or two.
-/

import Mathlib

namespace Problem26

/--
Let $K/\mathbb{Q}$ be a finite extension.
Let $H$ be a closed subgroup of the absolute Galois group $G(K)$ of $K$.
If $H$ is finite, then the cardinality of $H$ is either one or two.
-/
theorem card_one_or_two_of_finite_closed_subgroup_of_absoluteGaloisGroup
    (K : Type) [Field K] [Algebra ℚ K] [Module.Finite ℚ K]
    (H : Subgroup (Field.absoluteGaloisGroup K))
    (h_closed : IsClosed (H : Set (Field.absoluteGaloisGroup K)))
    (h_fin : Finite H) : Nat.card H = 1 ∨ Nat.card H = 2 := by
  sorry

end Problem26