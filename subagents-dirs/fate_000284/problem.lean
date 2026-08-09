/-- FATE Problem (id=35, source=FATE-X, tags=['Commutative Algebra', 'Ideal Theory', 'Ideals and Modules'] )
    Informal statement: A commutative ring whose prime ideals are finitely generated is Noetherian.
-/

import Mathlib

namespace Problem35

/--
A commutative ring whose prime ideals are finitely generated is Noetherian.
-/
theorem noetherian_of_prime_ideals_fg (R : Type) [CommRing R]
    (h_fg : ∀ (p : Ideal R), p.IsPrime → p.FG) : IsNoetherianRing R := by
  sorry

end Problem35