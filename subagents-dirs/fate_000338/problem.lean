/-- FATE Problem (id=89, source=FATE-X, tags=['Commutative Algebra', 'Ideal Theory', 'Localization and Decomposition of Ideals'] )
    Informal statement: Prove that if $\#G = 336$ then $G$ is not simple.
-/

import Mathlib

namespace Problem89

/--
Prove that if $\#G = 336$ then $G$ is not simple.
-/
theorem not_isSimpleGroup_of_card_eq_336 (G : Type) [Group G]
    [Finite G] (h_card : Nat.card G = 336) : ¬ IsSimpleGroup G := by
  sorry

end Problem89