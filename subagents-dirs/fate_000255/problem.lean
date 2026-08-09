/-- FATE Problem (id=6, source=FATE-X, tags=['Abstract Algebra', 'Group Theory', 'Group Actions and Sylow theorems'] )
    Informal statement: Prove that if $\#G = 396$ then $G$ is not simple.
-/

import Mathlib

namespace Problem6

/--
Prove that if $\#G = 396$ then $G$ is not simple.
-/
theorem not_isSimpleGroup_of_card_eq_396 (G : Type) [Group G]
    [Finite G] (h_card : Nat.card G = 396) : ¬ IsSimpleGroup G := by
  sorry

end Problem6