/-- FATE Problem (id=30, source=FATE-X, tags=['Commutative Algebra', 'Ideal Theory', 'Integral Dependence and the Nullstellensatz'] )
    Informal statement: Let \( A \) be a subring of a ring \( B \), such that the set \( B \setminus A \) is closed under multiplication. Show that \( A \) is integrally closed in \( B \).
-/

import Mathlib

namespace Problem30

/--
Let \( A \) be a subring of a ring \( B \), such that the set \( B \setminus A \) is closed under
multiplication. Show that \( A \) is integrally closed in \( B \).
-/
theorem integrallyClosedIn_of_complement_multiplicatively_closed (B : Type) [CommRing B] (A : Subring B)
    (h : ∀ (x y : B), x ∉ A → y ∉ A → x * y ∉ A) : IsIntegrallyClosedIn A B := by
  sorry

end Problem30