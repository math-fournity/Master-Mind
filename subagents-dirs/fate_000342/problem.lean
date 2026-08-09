/-- FATE Problem (id=93, source=FATE-X, tags=['Commutative Algebra', 'Ideal Theory', 'Localization and Decomposition of Ideals'] )
    Informal statement: There exists a field $k$ and a (not necessarily commutative) ring $A$ such that $A$ is integral and finitely generated over $k$ but $\dim_k A$ is not finite.
-/

import Mathlib

namespace Problem93

/--
There exists a field $k$ and a (not necessarily commutative) ring $A$
such that $A$ is integral and finitely generated over $k$ but $\dim_k A$ is not finite.
-/
theorem exists_integral_finiteType_not_finiteDimensional : ∃ (k A : Type) (_ : Field k)
    (_ : Ring A) (_ : Algebra k A),
    Algebra.IsIntegral k A ∧ Algebra.FiniteType k A ∧ ¬ FiniteDimensional k A := by
  sorry

end Problem93